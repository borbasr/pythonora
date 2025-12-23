import shelve

s = shelve.open('shelve_data')
s['name'] = ['Elek', 'Jakab', 'Feri']
s['tup1'] = (1, 2, 3, 4, 5, 6)
s['num'] = 12345
s.close()

r = shelve.open('shelve_data')
for key in r:
    print(r[key])
s.close()
#pickle egy objektumra mert fontos a sorrend
#shelve töb objektumra mert nem fontos a sorrend

