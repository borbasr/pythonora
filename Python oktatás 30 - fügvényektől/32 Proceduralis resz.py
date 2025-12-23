# a fógvényt a dec fvg_neve(paraméter): ozzuk létre
# utasitások

def first(name):
    """
    Ez a fugvény köszön
    """
    print('Hello ' +name)
first('Bob')

print(first.__doc__)

def second(num):
    if num %2 ==0:
        return "Paros a szam"
    return "A szam nem paros"
print(second(2))
print(second(3))

#anonim fügvények vagy lambda fügvény
def third(num):
    return num * num
var1=lambda num: num * num
print(third(3))
print(var1(3))

var2 = lambda a, b: a + b
print(var2(1, 2))

users = [
    {'username': 'elek', 'email': 'teszt@elek.hu', 'orders': ['T1', 'T2', 'T3']},
    {'username': 'jakab', 'email': 'teszt@jakab.hu', 'orders': []},
    {'username': 'feri', 'email': 'teszt@feri.hu', 'orders': []},
    {'username': 'pista', 'email': 'teszt@feri.hu', 'orders': ['T4', 'T5', 'T6']},
    {'username': 'bela', 'email': 'teszt@bela.hu', 'orders': []},
    {'username': 'mari', 'email': 'teszt@mari.hu', 'orders': ['T1', 'T2', 'T3']},
]

#nincs rendeles
wo_users = list(filter(lambda u: not u['orders'], users))
print(wo_users)

user_names = list(map(lambda user: user['username'].upper(), users))
print(user_names)

user_names2 = list(map(lambda user: user['username'].upper(), filter(lambda u: not u['orders'], users)))
print(user_names2)

#lista segitsegevel ugyanaz int az elző, ha sok az adat akkor optimalisabb az előző, ha keves az adat akkor mind1, mert akkor a map fugveny egy szurt listan meg vegig
user_names3 = [user['username'].upper() for user in users if not user['orders']]
print(user_names3)




