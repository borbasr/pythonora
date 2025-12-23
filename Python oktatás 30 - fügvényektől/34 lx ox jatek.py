# Van 2 jatekos
# Kijelzo torlese
# A tabla megrajzolasa
# A jeloloket le kell rakni
# Nyertes ellenorzese
# Ellenorizni kell hogy tele van e a tabla
import os
import random
from platform import system

PLAYER1_NAME = 'Jatekos 1'
PLAYER2_NAME = 'Jatekos 2'

def clear_screan():
    command = 'clear'
    if system().lower().startswith('win'):
        command = 'cls'
    os.system(command)

def show_table(table):
    clear_screan()
    print('   |   |')
    print(' ' + table[7] + ' | ' + table[8] + ' | ' + table[9])
    print('   |   |')
    print('-' * 11)
    print('   |   |')
    print(' ' + table[4] + ' | ' + table[5] + ' | ' + table[6])
    print('   |   |')
    print('-' * 11)
    print('   |   |')
    print(' ' + table[1] + ' | ' + table[2] + ' | ' + table[3])
    print('   |   |')

def input_player():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input(PLAYER1_NAME + ' mivel szeretnel jatszani X vagy O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    return ('O', 'X')

def check_winning(table, marker):
    return (
    (table[7] == marker and table[8] == marker and table[9] == marker) or # Felso sor
    (table[4] == marker and table[5] == marker and table[6] == marker) or # Kozepso sor
    (table[1] == marker and table[2] == marker and table[3] == marker) or # Also sor
    (table[7] == marker and table[4] == marker and table[1] == marker) or # Bal oszlop
    (table[8] == marker and table[5] == marker and table[2] == marker) or # Kozepso oszlop
    (table[9] == marker and table[6] == marker and table[3] == marker) or # Jobb oszlop
    (table[7] == marker and table[5] == marker and table[3] == marker) or # Bal atlo
    (table[9] == marker and table[5] == marker and table[1] == marker) # Jobb atlo
    )

def set_marker(table, marker, pos):
    table[pos] = marker

def random_player():
    if random.randint(0, 1) == 0:
        return PLAYER1_NAME
    return PLAYER2_NAME


def check_whitespace(table, pos):
    return table[pos] == ' '


def is_table_full(table):
    for i in range(1, 10):
        if check_whitespace(table, i):
            return False
    return True

def choose_player_position(table):
    pos = 0

    while pos not in range(1, 10) or not check_whitespace(table, pos):
        user_input = input('Kerem adjon meg egy poziciot (1-9): ')
        if user_input.isdigit():
            pos = int(user_input)
            clear_screan()
    return pos

def run_player_logic(marker, table, next_player):
    global game_on
    global who
    show_table(table)
    position = choose_player_position(table)
    set_marker(table, marker, position)

    if check_winning(table, marker):
        show_table(table)
        print('Gratulalunk, megnyerte a jatekot!')
        game_on = False
    else:
        if is_table_full(table):
            show_table(table)
            print('A jatek dontettlen! enki sem nyert!')
            game_on = False
        else:
            who = next_player


while True:
    table = [' '] * 10
    player1_marker, player2_marker = input_player()
    who = random_player()

    start_game = input('Keszen allsz a jatekra? Igen vagy Nem: ')

    if start_game.lower().startswith('i'):
        game_on = True
    else:
        game_on = False

    while game_on:
        if who == PLAYER1_NAME:
            run_player_logic(player1_marker, table, PLAYER2_NAME)
        else:
            run_player_logic(player2_marker, table, PLAYER1_NAME)

    repeat_game = (input('Szeretne ujra jatszani? Irja be hogy igen, vagy nem: ')
                   .lower().startswith('i'))
    if not repeat_game:
        break