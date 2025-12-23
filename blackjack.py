from random import shuffle


class CardData:
    def __init__(self):
        raise RuntimeError('Az osztaly statikus, nem peldanyosithato!')

    # statikus adatok
    colors = ('Kor', 'Karo', 'Treff', 'Pikk')
    ranks = (
        'Ketto', 'Harom', 'Negy', 'Ot', 'Hat', 'Het', 'Nyolc', 'Kilenc',
        'Tiz', 'Bubi', 'Dama', 'Kiraly', 'Asz'
    )

    # jatek allapota
    is_playing = True

    @staticmethod
    def get_value(item: str) -> int:
        values = {
            'Ketto': 2, 'Harom': 3, 'Negy': 4, 'Ot': 5, 'Hat': 6,
            'Het': 7, 'Nyolc': 8, 'Kilenc': 9, 'Tiz': 10, 'Bubi': 10,
            'Dama': 10, 'Kiraly': 10, 'Asz': 11
        }
        if item not in values:
            raise ValueError('A megadott érték nem található')
        return values[item]


class Card:
    def __init__(self, color: str, rank: str):
        self.color = color
        self.rank = rank

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        if len(color) >= 3:
            self.__color = color
        else:
            raise ValueError("Az ertek nem kartyaszin")

    @property
    def rank(self) -> str:
        return self.__rank

    @rank.setter
    def rank(self, rank: str) -> None:
        if len(rank) >= 2:
            self.__rank = rank
        else:
            raise ValueError("Az ertek nem kartyarank")

    def __str__(self) -> str:
        return self.__rank + ' - ' + self.color


class Deck(list):
    def __init__(self):
        super().__init__()
        for color in CardData.colors:
            for rank in CardData.ranks:
                self.append(Card(color, rank))

    def __str__(self) -> str:
        tmp = ''
        for card in self:
            tmp += str(card) + '\n'
        return tmp

    def mix(self) -> None:
        shuffle(self)

    def div(self) -> Card:
        return self.pop()

    def append(self, card) -> None:
        if not isinstance(card, Card):
            raise TypeError('Csak kartya tipust lehet hozzaadni!')
        super().append(card)


class Hand(list):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.ace = 0

    def append(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError('Csak kartya tipust lehet hozzaadni!')
        super().append(card)
        self.value += CardData.get_value(card.rank)
        if card.rank == 'Asz':
            self.ace += 1

    def set_aces(self) -> None:
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1


class Chips:
    def __init__(self, sum: int = 100):
        self.sum = sum
        self.bet = 0

    @property
    def sum(self) -> int:
        return self.__sum

    @sum.setter
    def sum(self, value: int) -> None:
        if value > 0:
            self.__sum = value
        else:
            raise ValueError('Az ertek nem lehet negativ vagy 0!')

    @property
    def bet(self) -> int:
        return self.__bet

    @bet.setter
    def bet(self, value: int) -> None:
        if value >= 0 and self.sum - value >= 0:
            self.__bet = value
        else:
            raise ValueError(
                'A tet csak pozitiv egesz szam lehet, '
                'es nem adhat meg tobbet, mint amennyi zsetonja van!'
            )

    def win_bet(self) -> None:
        self.sum += self.bet

    def loose_bet(self) -> None:
        self.sum -= self.bet


class Rules:
    def __init__(self):
        raise RuntimeError('Az osztaly statikus, nem peldanyosithato!')

    @staticmethod
    def betting(chips: Chips) -> None:
        while True:
            try:
                chips.bet = int(input('Mennyi zsetont szeretne feltenni> '))
            except ValueError as error:
                print(error)
            else:
                break

    @staticmethod
    def draw(card_deck: Deck, hand: Hand) -> None:
        hand.append(card_deck.div())
        hand.set_aces()

    @staticmethod
    def draw_or_stop(card_deck: Deck, hand: Hand) -> None:
        while True:
            var = input('Húzni szeretne vagy megállni? Nyomj "h"-t vagy "m"-t: ')
            if var and var[0].lower() == 'h':
                Rules.draw(card_deck, hand)
            elif var and var[0].lower() == 'm':
                print('A játékos megállt! Az osztó játszik!')
                CardData.is_playing = False
            else:
                print('Ilyen opció nincs')
                continue
            break

    @staticmethod
    def player_cards(card_player: Hand) -> None:
        print('A jatekos kezeben van:\n', *card_player, sep='\n')
        print('A jatekos kezeben levo lapok osszerteke: ', card_player.value)

    @staticmethod
    def not_show_all(card_player: Hand, card_dealer: Hand) -> None:
        print('Az oszto kezeben van:')
        print('<Kartyalap rejtve>')
        print(card_dealer[1])
        Rules.player_cards(card_player)

    @staticmethod
    def show_all(card_player: Hand, card_dealer: Hand) -> None:
        print('Az oszto kezeben van:\n', *card_dealer, sep='\n')
        Rules.player_cards(card_player)

    @staticmethod
    def player_loose(chips: Chips) -> None:
        print('A jatekos eluszott!')
        chips.loose_bet()

    @staticmethod
    def player_win(chips: Chips) -> None:
        print('A jatekos nyert!')
        chips.win_bet()

    @staticmethod
    def dealer_loose(chips: Chips) -> None:
        print('Az oszto eluszott!')
        chips.win_bet()

    @staticmethod
    def dealer_win(chips: Chips) -> None:
        print('Az oszto nyert!')
        chips.loose_bet()

    @staticmethod
    def equals() -> None:
        print('Az allas dontetlen!')


# ===== main =====

chips = Chips()
CardData.is_playing = True

while True:
    print('Udvozlom a jatekost! A cel a 21 elerese!\n'
          'Az oszto addig huz amig el nem eri a 17-t\n'
          'Az Asz a szabalyok alapjan 11-t vagy 1-t er!')

    deck = Deck()
    deck.mix()
    Rules.betting(chips)

    player = Hand()
    dealer = Hand()

    Rules.draw(deck, player)
    Rules.draw(deck, player)
    Rules.draw(deck, dealer)
    Rules.draw(deck, dealer)

    Rules.not_show_all(player, dealer)

    while CardData.is_playing:
        Rules.draw_or_stop(deck, player)
        Rules.not_show_all(player, dealer)

        if player.value > 21:
            Rules.player_loose(chips)
            break
        elif player.value <= 21:
            while dealer.value < 17:
                Rules.draw(deck, dealer)
            if dealer.value > 21:
                Rules.dealer_loose(chips)
            elif dealer.value > player.value:
                Rules.dealer_win(chips)
            elif dealer.value < player.value:
                Rules.player_win(chips)
            else:
                Rules.equals()
            break

    Rules.show_all(player, dealer)
    print('\nA jatekos egyenlege: ', chips.sum)
    new_game = input('Szeretne meg 1x jatszani? Nyomj i-t vagy n-t: ')
    if new_game and new_game[0].lower() == 'i':
        CardData.is_playing = True
        continue

    print('Koszonjuk a jatekot!')
    break
