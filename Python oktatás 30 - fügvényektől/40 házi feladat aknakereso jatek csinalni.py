print("\u2B1B \u25CB \U0001F4A3 \U0001F4A5")

import random
from typing import Iterable, Tuple, List, Union

Coord = Tuple[int, int]
Cell = Union[int, str]  # szám = szomszéd bomba darabszám, 'B' = bomba

def user_start():
# Táblaméret bekérése
    while True:
        try:
            sizeoftable = int(input("Add meg a tábla méretét, egész számmal 10 és 30 között: "))
            if 10 <= sizeoftable <= 30:
                break  # ha jó az érték, kilépünk a ciklusból
            else:
                print("❌ Adj meg 10 és 30 közötti egész számot, te ökör!😄")
        except ValueError:
            print("❌ Számot adj meg, ne szöveget!")

    print("\nVálaszd ki a játék nehézségét:")
    print("1 - Kezdő")
    print("2 - Középhaladó")
    print("3 - Haladó")
    print("4 - Profi")
    print("5 - Űberprofi")

    while True:
        try:
            difficulty = int(input("Ird be a nehézségi szint számát 1 és 5 között:"))
            if 1 <= difficulty <= 5:
                break
            else:
                print("❌ Adj meg 1 és 5 közötti számot, te ökör!😄")
        except ValueError:
            print("❌ Számot adj meg, ne szöveget!")

    print(f"A tábla mérete {sizeoftable} x {sizeoftable}. ")
    print(f"A játék nehézsége {difficulty}.")
    return sizeoftable, difficulty

def get_number_of_bombs(difficulty:int, sizeoftable:int) -> int:
    numberofbombs = (int(difficulty * 0.05 * sizeoftable ** 2))
    return numberofbombs

def bombs_positions(numberofbombs: int, sizeoftable: int) -> list[int]:
    """
    Véletlenszerűen bombapozíciókat generál egy négyzetes táblához.
    Visszaad egy listát, amiben (sor, oszlop) koordináták vannak.
    """
    all_cells = [(r, c) for r in range(sizeoftable) for c in range(sizeoftable)]
    bombs = random.sample(all_cells, numberofbombs)
    return bombs

def make_minesweeper_board(sizeoftable: int, bombs: Iterable[Coord]) -> List[List[Cell]]:
    """
    Létrehoz egy táblát ahol a bombák 'B'-vel vannak jelölve,
    és minden más cella egy egész szám, ami a szomszédos bombák számát adja.
    bombs: iterable of (row, col)  -- feltételezzük 0-indexelt koordinátákat
    """
    bombs_set = set(bombs)  # gyors keresés + duplikátum eltávolítás
    # inicializálás 0-val
    board: List[List[Cell]] = [[0 for _ in range(sizeoftable)] for _ in range(sizeoftable)]

    # bombák elhelyezése (ha out-of-bounds bombát adtál, figyelmen kívül hagyjuk)
    for r, c in bombs_set:
        if 0 <= r < sizeoftable and 0 <= c < sizeoftable:
            board[r][c] = 'B'

    # 8 szomszéd irány
    neighbors = [(-1,-1), (-1,0), (-1,1),
                 ( 0,-1),         ( 0,1),
                 ( 1,-1), ( 1,0), ( 1,1)]

    # minden cellához megszámoljuk a szomszéd bomba darabszámot (ha nem bomba)
    for r in range(sizeoftable):
        for c in range(sizeoftable):
            if board[r][c] == 'B':
                continue
            count = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < sizeoftable and 0 <= nc < sizeoftable and board[nr][nc] == 'B':
                    count += 1
            board[r][c] = count
    return board

# be kell kerni a felhasznalotol azt hogy melyik a tippje, majd ezt beirni egy listaba,
# ha ebbeen a lsitaban szerepel egy b akkor vege a jateknak es ki kell irni az összes bomba poziciojat

#kkirni a tablat ugy hogy az összes cella nincs felfedve csak a felhasznalo listaja van
# felfedve azt pedig töltse be a boadr listabol

def user_decision(board: List[List[Cell]], user_moves: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Bekéri a játékostól a következő lépés pozícióját (sor, oszlop),
    ellenőrzi, hogy érvényes-e, majd elmenti a lépést a listába.
    """
    size = len(board)  # a tábla mérete

    while True:
        user_input = input("Írd be a lépés pozícióját (pl. 3,4): ")

        # próbáljuk feldolgozni a bevitt adatot
        try:
            row_str, col_str = user_input.split(",")
            row, col = int(row_str.strip()), int(col_str.strip())

            # ellenőrzés: a lépés a táblán belül van-e
            if not (0 <= row < size and 0 <= col < size):
                print("❌ Ez a pozíció kívül esik a táblán! Próbáld újra.")
                continue

            # ellenőrzés: ezt a lépést már megtette-e a játékos
            if (row, col) in user_moves:
                print("⚠️ Erre a mezőre már léptél! Válassz másikat.")
                continue

            # ha minden rendben, hozzáadjuk a listához
            user_moves.append((row, col))
            print(f"✅ Lépés elfogadva: ({row}, {col})")
            break

        except ValueError:
            print("❌ Hibás formátum! Kérlek, így add meg: sor,oszlop (pl. 2,3)")

    return user_moves

def print_game_board(board: List[List[Cell]], user_moves: List[Tuple[int, int]]) -> None:
    """
    Kiírja a játék aktuális állapotát:
    - ahol a játékos még nem lépett: '■'
    - ahol már lépett: a board valódi értéke (szám vagy 'B')
    """
    size = len(board)
    print("\n🎯 Aktuális tábla állapota:")

    for r in range(size):
        row_display = []
        for c in range(size):
            if (r, c) in user_moves:
                cell = board[r][c]
                # 0 helyett szebb, ha pontot írunk
                if cell == 0:
                    row_display.append(".")
                else:
                    row_display.append(str(cell))
            else:
                row_display.append("■")  # még nem felfedett mező
        print(" ".join(row_display))

def final_print_board(board: List[List[Cell]]) -> None:
    """Konzolra szépítés: minden oszlop egyforma széles."""
    width = 5  # minden cella szélessége (tetszőlegesen állítható)

    for row in board:
        formatted_row = []
        for cell in row:
            if cell == 'B':
                symbol = 'B'  # bomba
            elif cell == 0:
                symbol = '-'  # üres (kör)
            else:
                symbol = str(cell)
            formatted_row.append(f"{symbol:^{width}}")
        print("".join(formatted_row))

def main() -> None:
    # 1) Paraméterek bekérése
    sizeoftable, difficulty = user_start()

    # 2) Bombaszám kiszámítása (nehézség alapján)
    numberofbombs = get_number_of_bombs(difficulty, sizeoftable)

    # 3) Véletlen bombapozíciók generálása
    bombs = bombs_positions(numberofbombs, sizeoftable)

    # 4) Tábla felépítése bombákkal és számolt szomszédszámokkal
    board = make_minesweeper_board(sizeoftable, bombs)

    # 5) Játékciklus: lépések gyűjtése és állapot kirajzolása
    user_moves: List[Tuple[int, int]] = []

    while True:
        # aktuális állapot kirajzolása (csak a felfedett mezők)
        print_game_board(board, user_moves)

        # felhasználói lépés bekérése és eltárolása
        user_moves = user_decision(board, user_moves)
        r, c = user_moves[-1]  # az utolsó (friss) lépés

        # 5/a) Bomba-e a lépés?
        if board[r][c] == 'B':
            print("\n💥 Bomba! Vége a játéknak.\nÖsszes bomba és számok felfedése:")
            final_print_board(board)
            break

        # 5/b) Győzelem-ellenőrzés: minden biztonságos mező fel van fedve?
        total_safe = sizeoftable * sizeoftable - numberofbombs
        revealed_safe = sum(1 for (rr, cc) in user_moves if board[rr][cc] != 'B')
        if revealed_safe >= total_safe:
            print_game_board(board, user_moves)
            print("\n🏆 Nyertél! Minden biztonságos mezőt felfedtél.")
            # opcionálisan a teljes tábla is:
            print("\nTeljes tábla:")
            final_print_board(board)
            break


if __name__ == "__main__":

    main()