# 3. Szavak elhelyezése a szórácsban
# 4. Üres cellák fel kell tölteni véletlenszerű betűkkel
# 5. Számozott rács megjelenítése
# 6. Felhasználói input (koordináták)
# 7. Ha megtalálta akkor a megtalált betűk "kiemelése" azaz jelen esetben színezése
import random

from colorama import init, Fore, Style

init(autoreset=True)

def get_word_list() -> list[str]:
    """
    The game word list
    :return: A list with the words
    """
    return ['PYTHON', 'PROGRAM', 'LOGIKA', 'WEB', 'LAPTOP', 'SZINTAXIS', 'ALMAFA']

def create_empty_grid(size=10):
    """
    Create empty grid

    Args:
        size (int): The grid size
    Returns:
        The empty grid
    """
    return [[' ' for _ in range(size)] for _ in range(size)]

def place_word_in_grid(grid, word):
    """
    Place word on grid

    Args:
    grid (list): The grid
    :param grid:
    :param word:
    :return:
    """
    size = len(grid)
    directions = ["horizontal", "vertical", "diagonal"]
    placed = False
    while not placed:
        good_position = True
        direction = random.choice(directions)
        start_row, start_col = random.randint(0, size - 1), random.randint(0, size - 1)

        if direction == 'horizontal' and start_col + len(word) <= size:
            for i in range(len(word)):
                if grid[start_row][start_col + i] != ' ':
                    good_position = False
                    break
            if not good_position:
                continue
            for i in range(len(word)):
                if grid[start_row][start_col + i] == ' ' and good_position:
                    grid[start_row][start_col + i] = word[i]
                    placed = True
        elif direction == 'vertical' and start_row + len(word) <= size:
            for i in range(len(word)):
                if grid[start_row + i][start_col] != ' ':
                    good_position = False
                    break
            if not good_position:
                continue
            for i in range(len(word)):
                if grid[start_row + i][start_col] == ' ' and good_position:
                    grid[start_row + i][start_col] = word[i]
                    placed = True
        elif direction == 'diagonal' and start_col + len(word) <= size and start_row + len(word) <= size:
            for i in range(len(word)):
                if grid[start_row + i][start_col + i] != ' ':
                    good_position = False
                    break
            if not good_position:
                continue
            for i in range(len(word)):
                if grid[start_row + i][start_col + i] == ' ' and good_position:
                    grid[start_row + i][start_col + i] = word[i]
                    placed = True

def fill_empty_cells(grid):
    """
    Fill the empty grid cells with random values

    Args:
        grid (list): The grid
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ' ':
                grid[row][col] = chr(random.randint(65, 90))

def display_grid(grid):
    """
    Display the grid with coordinates

    Args:
        grid (list): The grid
    """
    print('\nJátékrács (sor és oszlopszámokkal)')
    header = '   ' + ' '.join(f'{i}' for i in range(len(grid)))
    print(header)
    print("    " + '--' * len(grid))
    for idx, row in enumerate(grid):
        print(f'{idx} | ' + ' '.join(f'{Fore.GREEN}{cell}{Style.RESET_ALL}'
                                     if cell.islower() else cell for cell in row))

def get_number_input(user_str, size):
    """
    Handle user input and validate

    Args:
        user_str (str): The input string
        size (int): The grid size

    Returns:
        The choosed coordinate
    """
    while True:
        input_str = input(user_str)
        if input_str.isdigit() and 0 <= int(input_str) < size:
            return int(input_str)

def get_word_selection(grid):
    """
    Get word selection

    Args:
        grid(list): The grid
    Returns:
        Coordinates
    """
    print('\nSegítség a koordináták megadásához:')
    print('- Sor és oszlopszámot adjon meg (pl.: kezdő sor: 2 oszlop: 3)')
    print("- Végpontként adja meg a koordinátákat (pl.: vég sor: 2 oszlop: 7)")
    print("Példa a 'SZINTAXIS' szóhoz a kezdő koordináta (1, 1) vég koordináta: (1, 8)")
    size = len(grid)
    start_row = get_number_input(user_str=f'Adja meg a szó kezdősorának a számát (0-{size - 1}): ', size=size)
    start_col = get_number_input(user_str=f'Adja meg a szó kezdőoszlopának a számát (0-{size - 1}): ', size=size)
    end_row = get_number_input(user_str=f'Adja meg a szó végsorának a számát (0-{size - 1}): ', size=size)
    end_col = get_number_input(user_str=f'Adja meg a szó végoszlopának a számát (0-{size - 1}): ', size=size)

    return start_row, start_col, end_row, end_col

def check_and_mark_word_in_grid(grid, word, start_row, start_col, end_row, end_col):
    """
    Check and mark a given word in the grid

    Args:
        grid(list): The grid
        word(str): The given word
        start_row(int): The start row coordinate
        start_col(int): The start col coordinate
        end_row(int): The end row coordinate
        end_col(int): The end col coordinate

    Returns:
        (boolean): Finded
    """
    word_length = len(word)
    # vízszintes
    if start_row == end_row:
        if abs(start_col - end_col) + 1 == word_length:
            for i in range(word_length):
                if grid[start_row][start_col + i] != word[i]:
                    return False
            for i in range(word_length):
                grid[start_row][start_col + i] = grid[start_row][start_col + i].lower()
            return True
    # függőleges
    elif start_col == end_col:
        if abs(start_row - end_row) + 1 == word_length:
            for i in range(word_length):
                if grid[start_row + i][start_col] != word[i]:
                    return False
            for i in range(word_length):
                grid[start_row + i][start_col] = grid[start_row + i][start_col].lower()
            return True
    # atlos
    elif abs(start_row - end_row) + 1 == word_length and abs(start_col - end_col) + 1 == word_length:
        for i in range(word_length):
            if grid[start_row + i][start_col + i] != word[i]:
                return False
        for i in range(word_length):
            grid[start_row + i][start_col + i] = grid[start_row + i][start_col + i].lower()
        return True
    return False
def main():
    grid = create_empty_grid()
    word_list = get_word_list()

    for word in word_list:
        place_word_in_grid(grid, word)

    fill_empty_cells(grid)
    display_grid(grid)

    print('\nRejtett szavak: ', ', '.join(word_list))

    found_words = []

    while len(found_words) < len(word_list):
        print('\nTalált szavak: ', ', '.join(found_words))
        selection = get_word_selection(grid)

        start_row, start_col, end_row, end_col = selection
        found = False
        for word in word_list:
            if word not in found_words and check_and_mark_word_in_grid(
                grid, word, start_row, start_col, end_row, end_col
            ):
                print(f'Megtaláltad a szót: {word}')
                found_words.append(word)
                found = True
                break
        if not found:
            print('Nincs a megadott szavak egyike sem a megadott helyen!')

        display_grid(grid)

main()