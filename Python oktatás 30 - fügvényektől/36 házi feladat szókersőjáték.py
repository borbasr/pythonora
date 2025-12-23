#szókereső játék, rács benne egy csomó betüvel, megv és alatta van egy lista amiben benn e vann aava amet meg kell keresni, alapbl egy matrix
# az elejen valassza ki a felhasznalo hogy milyen nagy tablat akar, majd azt hogy mennyi szót
# 1 jatekos
# veletlenszeruen legeneralni a tablat veletlen betukkel
# veletlenszeruen kivalasztani az xml listabol annyi szót emennyit kivalasztott a felhasznalo
# ezeket a szavakat listakka alakitani
# összeszamaloni mennyi elem van az egyes listakban
# veletlenszerüen kivalasztani a tablabol a lista első elemének a helyét
# ezutan a mellette lévő pozicióban kijelölni a következő listaelem helyét
# ezután a következő elem helyét

# majd felulirni az xmlbol a veletlenszeruen valasztott kockaba
# regisztralni egy listaban azt hogy hol vannak a betuk
# list alapjan visszakeresni melyik az a lista
# ha a beutott lista megegyezik valamelyik listaval akkor szamoljon pontot a felhasznalonak
import random
import string
import xml.etree.ElementTree as ET
from pathlib import Path

# --- Beállítások ---
FILLER_LATIN = list("AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ")  # töltőbetűk készlete
MAX_PLACEMENT_TRIES = 2000  # elhelyezési próbálkozások a szavakhoz

# 8 lehetséges irány (sor, oszlop): vízszintes, függőleges, átlók
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def normalize(s: str) -> str:
    """Összehasonlításhoz nagybetűsít, környezettől független."""
    return s.strip().upper()

def load_words_from_xml(path: str) -> list[str]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Nem találom az XML-t: {path}")
    root = ET.parse(p).getroot()
    # <words><word>szó</word>...</words>
    words = [w.text for w in root.findall(".//word") if w.text]
    # trimm + üresek kiszűrése + duplikátumok kiszűrése
    cleaned = []
    seen = set()
    for w in words:
        w2 = w.strip()
        if not w2:
            continue
        key = normalize(w2)
        if key not in seen:
            cleaned.append(w2)
            seen.add(key)
    return cleaned

def pick_words(word_pool: list[str], how_many: int, max_len: int) -> list[str]:
    """Véletlenül kiválaszt 'how_many' szót, melyek max_len hosszúak."""
    candidates = [w for w in word_pool if len(w) <= max_len]
    if len(candidates) < how_many:
        how_many = len(candidates)
    return random.sample(candidates, how_many)

def make_empty_board(n: int) -> list[list[str]]:
    return [["" for _ in range(n)] for _ in range(n)]

def fill_empty_with_random(board: list[list[str]]):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == "":
                board[r][c] = random.choice(FILLER_LATIN)

def in_bounds(n: int, r: int, c: int) -> bool:
    return 0 <= r < n and 0 <= c < n

def can_place(board: list[list[str]], word: str, r: int, c: int, dr: int, dc: int) -> bool:
    n = len(board)
    for i, ch in enumerate(word):
        rr = r + dr * i
        cc = c + dc * i
        if not in_bounds(n, rr, cc):
            return False
        cell = board[rr][cc]
        if cell not in ("", ch):  # üres vagy egyező betű felülírás megengedett
            return False
    return True

def place_word(board: list[list[str]], word: str) -> list[tuple[int,int]] | None:
    """Megpróbálja elhelyezni a szót; siker esetén visszaadja a koordináta-útvonalat."""
    n = len(board)
    tries = 0
    cells = [(r, c) for r in range(n) for c in range(n)]
    while tries < MAX_PLACEMENT_TRIES:
        tries += 1
        random.shuffle(cells)
        r, c = random.choice(cells)
        dirs = DIRECTIONS[:]
        random.shuffle(dirs)
        for dr, dc in dirs:
            if dr == 0 and dc == 0:
                continue
            if can_place(board, word, r, c, dr, dc):
                path = []
                for i, ch in enumerate(word):
                    rr = r + dr * i
                    cc = c + dc * i
                    board[rr][cc] = ch
                    path.append((rr, cc))
                return path
    return None

def render_board(board: list[list[str]]) -> str:
    n = len(board)
    lines = []
    header = "   " + " ".join(f"{c:2d}" for c in range(n))
    lines.append(header)
    for r in range(n):
        row = " ".join(f"{ch or '.' :2s}" for ch in board[r])
        lines.append(f"{r:2d} {row}")
    return "\n".join(lines)

def render_word_list(words: list[str], found: set[str]) -> str:
    parts = []
    for w in words:
        if normalize(w) in found:
            parts.append(f"[✔] {w}")
        else:
            parts.append(f"[ ] {w}")
    return "Keresendő szavak:\n" + "\n".join(parts)

def game_loop(board, targets: list[str], paths: dict[str, list[tuple[int,int]]]):
    found: set[str] = set()
    score = 0
    while True:
        print()
        print(render_board(board))
        print()
        print(render_word_list(targets, found))
        print(f"\nPontszám: {score}   (írj be egy szót; 'quit' = kilép)")
        guess = input("> ").strip()
        if not guess:
            continue
        if guess.lower() == "quit":
            print("Kiléptél. Köszi a játékot!")
            break
        key = normalize(guess)
        if key in found:
            print("Ezt a szót már megtaláltad!")
            continue
        # célok normalizált halmaza
        target_keys = {normalize(w): w for w in targets}
        if key not in target_keys:
            print("Nincs ilyen a listában. Próbáld újra!")
            continue
        # jó találat
        found.add(key)
        score += len(key)
        print(f"✔ Talált! +{len(key)} pont")
        if len(found) == len(targets):
            print("\nMinden szót megtaláltál! 🎉")
            print(render_board(board))
            print(f"Végső pontszám: {score}")
            break

def prepare_game():
    # --- Bemenetek ---
    while True:
        try:
            n = int(input("Tábla méret (pl. 12): ").strip())
            if n < 5 or n > 50:
                print("5 és 50 között add meg.")
                continue
            break
        except ValueError:
            print("Adj meg egy egész számot.")
    while True:
        try:
            k = int(input("Hány szó legyen (pl. 8): ").strip())
            if k < 1:
                print("Legalább 1 szó legyen.")
                continue
            break
        except ValueError:
            print("Adj meg egy egész számot.")

    # --- XML fájl automatikus betöltése ---
    xml_path = "werbs.xml"
    print(f"XML fájl betöltése innen: {xml_path}")

    # --- Szólista betöltése ---
    if xml_path:
        try:
            pool = load_words_from_xml(xml_path)
        except Exception as e:
            print(f"XML betöltési hiba: {e}")
            pool = []
    else:
        pool = ["alma", "körte", "python", "program", "adat", "mátrix",
                "lista", "függvény", "szám", "kód", "szöveg", "robot"]

    if not pool:
        print("Nincs szó a szólistában. Kilépek.")
        return

    # --- Cél szavak kiválasztása és normalizálása a táblához ---
    targets_raw = pick_words(pool, k, max_len=n)
    # a táblába nagybetűsen tesszük, de a felhasználónak tökmindegy (normalizálunk)
    targets = [w.strip() for w in targets_raw]
    targets_up = [normalize(w) for w in targets]

    # --- Tábla és elhelyezés ---
    board = make_empty_board(n)
    paths: dict[str, list[tuple[int,int]]] = {}  # norm. szó -> koordináta lista

    # szavak véletlen sorrendben
    order = list(range(len(targets_up)))
    random.shuffle(order)

    for idx in order:
        word_up = targets_up[idx]
        placed = place_word(board, word_up)
        if not placed:
            # ha nem fér be, kihagyjuk (ritka, de előfordulhat kis táblán)
            print(f"Figyelem: nem tudtam elhelyezni: {targets[idx]}")
            # töröljük a célok közül is
            continue
        paths[word_up] = placed

    # esetleges kiesettek kiszűrése
    final_targets = [t for t in targets if normalize(t) in paths]

    # töltőbetűk
    fill_empty_with_random(board)

    print("\n--- SZÓKERESŐ ---")
    print("A szavak a rácsban egyenes vonalban, 8 lehetséges irányban vannak elrejtve.\n")
    if len(final_targets) == 0:
        print("Nem maradt elhelyezett szó. Próbáld nagyobb táblával vagy kevesebb szóval.")
        return

    game_loop(board, final_targets, paths)

if __name__ == "__main__":
    prepare_game()
