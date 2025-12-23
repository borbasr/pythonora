# 1 kiirni az első oldalt ott kivalassza mibol jatszik, allat, növeny, targy és kirajzolja a teljes akasztofat sargaval
# 2 kivalassza a kivalasztott listából veletlenszerüen egy szavat
# bekerni az egy betüt ami benne lehet a szóban
# állapitsa meg hogy a válasz helyes vagy helytelen, ha helyes akkor irja ki a mezőre, ha helytelen akkor adja hozzá a helytelen válaszhoz

# letrehozni a helytelen válaszok listáját és hozzárendelni az akasztófa szinteket, ugy hogy az összes legyen sárgával kijelölve, minél több a helytelen válasz annál több a feketével vastaggal sezdett rész az akasztófában
# bekerni az egy betüt ami benne lehet a szóban

# 3 szamolja mennyi helytelen valasz érkezett

import random
import string

def get_word_list() -> list[str]:
    return ['PYTHON', 'PROGRAM', 'LOGIKA', 'WEB', 'LAPTOP', 'SZINTAXIS', 'ALMAFA']

stages = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
r"""
  -----
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  -----
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  -----
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  -----
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  -----
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  -----
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]

def play():
    word = random.choice(get_word_list()).upper() # veletlenszeruen kivalasztott szó a szólitából
    lives = len(stages) - 1 # fennmaradó a rossz válaszok száma
    guessed: set[str] = set() # megadott betük litsája
    alphabet = set(string.ascii_uppercase + "ÁÉÍÓÖŐÚÜŰ")
    display = ["_" if ch in string.ascii_uppercase else ch for ch in word]# Megjelenítéshez kezdetben aláhúzások

    while lives > 0 and "_" in display:
        print(stages[(len(stages) - 1) - lives])
        print("Szó:", " ".join(display))
        print("Tippelt betűk:", " ".join(sorted(guessed)) or "-")
        guess = input("Adj meg egy betűt: ").strip().upper()

        if len(guess) != 1 or guess not in alphabet:
            print("Adj meg pontosan egy betűt!")
            continue
        if guess in guessed:
            print("Ezt már tippelted.")
            continue

        guessed.add(guess)

        if guess in word:
            for i, ch in enumerate(word):
                if ch == guess:
                    display[i] = ch
            print("Talált! ✅")
        else:
            lives -= 1
            print("Nem talált. ❌  Hátralévő életek:", lives)

    # Vége
    if "_" not in display:
        print(stages[(len(stages) - 1) - lives])
        print("Gratulálok! A szó:", word)
    else:
        print(stages[-1])
        print("Vesztettél! A szó:", word)

if __name__ == "__main__":
    play()
