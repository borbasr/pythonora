import pickle

number_data = int(input('Mennyi adatot akar megadni: '))
data = []

for i in range(number_data):
    val = input(f'{i}. adat megadása: ')
    data.append(val)

with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)