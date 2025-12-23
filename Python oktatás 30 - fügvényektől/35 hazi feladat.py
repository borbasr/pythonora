from math import pi

def gomb_terfogat(r):
    return (4/3) * pi * (r ** 3)

r = float(input("Add meg a gömb sugarát: "))

if r < 0:
    print("A sugár nem lehet negatív!")
else:
    terfogat = gomb_terfogat(r)
    print(f"A gömb térfogata: {terfogat:.2f}")

def globe_volume3(radius):
    return (4/3) * 3.14 * (radius ** 3)

print(globe_volume3(2))

def globe_volume2(radius: float) -> float:
    """
    This function is returning the globe volume
    :param radius: The globe radius (positive number)
    :return: The globe volume
    """
    if radius > 0:
        return (4 / 3) * 3.14 * (radius ** 3)
    if r <= 0:
        raise ValueError(f"The globe volume must be positive!")
    return (4/3) * 3.14 * (radius ** 3)
# duplikatio megszuntetes ista
def check_range(num: int, small_num: int, big_num: int) -> None:
    if num in range(small_num, big_num):
        print('{} szám benne van a tartományban: {} és a {} között'
              .format(num, small_num, big_num))
    else:
        print('A tartományon kívül esik!')

check_range(num=5, small_num=2, big_num=7)

def is_in_range(num: int, small_num: int, big_num: int) -> bool:
    """
    Check number is in the range of (small_num, big_num)
    :param num: The number to check
    :param small_num: The range lowest value
    :param big_num: The range biggest value
    :return: True, if the number is in the range of small and big number
    :raises ValueError: If the small_num is bigger than the big_num
    """
    if small_num > big_num:
        raise ValueError(f'The small_num {small_num} is bigger than the big_num {big_num}')
    return small_num <= num <= big_num


def display_is_in_range(num: int, small_num: int, big_num: int) -> None:
    if is_in_range(num, small_num, big_num):
        print('{} szám benne van a tartományban: {} és a {} között'
              .format(num, small_num, big_num))
    else:
        print('A tartományon kívül esik!')


display_is_in_range(num=5, small_num=2, big_num=7)

# duplikatio megszuntetes ista
def egyedi(lista):
    """Visszaadja a listát duplikációk nélkül, az eredeti sorrendben."""
    uj_lista = []
    for elem in lista:
        if elem not in uj_lista:
            uj_lista.append(elem)
    return uj_lista

# nagybetuk kisbetuk szama

def betuk_szama(szoveg):
    """Kiírja a kis- és nagybetűk számát a megadott szövegben."""
    kis = 0
    nagy = 0

    for karakter in szoveg:
        if karakter.islower():
            kis += 1
        elif karakter.isupper():
            nagy += 1

    print(f"Kisbetűk száma: {kis}")
    print(f"Nagybetűk száma: {nagy}")
# nagybetuk kisbetuk szama
def count_small_and_upper_case2(s: str) -> dict:
    s_norm = unicodedata.normalize(form='NFC', s)
    upper = sum(1 for c in s_norm if c.isupper())
    lower = sum(1 for c in s_norm if c.islower())

    return {
        'original': s,
        'normalized': s_norm,
        'upper_case': upper,
        'lower_case': lower
    }


print(count_small_and_upper_case2('Őláitó'))


# palindrom
def is_palindrome(szo):
    """Eldönti, hogy a megadott szó palindróm-e."""
    szo = szo.lower()  # kisbetűssé alakítjuk, hogy ne számítson a nagybetű
    if szo == szo[::-1]:
        print("Ez a szó palindróm.")
    else:
        print("Ez a szó nem palindróm.")

# palindrom
def is_palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]


print(is_palindrome('legeg'))
print(is_palindrome('géza kék az ég'))

# panngram
def is_pangram(text: str) -> bool:
    alphabet = string.ascii_lowercase + 'öüóőúéáűí'
    normalized = unicodedata.normalize(form='NFC', text).lower()
    letters_in_text = {ch for ch in normalized if ch in alphabet}
    return letters_in_text.issuperset(alphabet)


print(is_pangram("valiban mukoidk"))
