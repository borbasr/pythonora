# nagym ennyisegu adatok felhasznalasanal nagyon fontos, mert sorba allitja a feladatot sé def simple_gen_fn():
    n = 1
    print('Ezt írjuk ki először')
    yield n

    n += 1
    print('Ezt írjuk ki másodjára')
    yield n

    n += 1
    print('Ezt írjuk ki harmadjára')
    yield n


#print(simple_gen_fn())
v1 = simple_gen_fn()
print(v1)
print(next(v1))
print(next(v1))
print(next(v1))
# print(next(v1))


for item in simple_gen_fn():
    print(item)

test_list = [1,3,6,10]
print([x**2 for x in test_list])

v2 = (x ** 2 for x in test_list)
print(next(v2))
print(next(v2))
print(next(v2))
print(next(v2))

print(sum(x ** 2 for x in test_list))
print(max(x ** 2 for x in test_list))

print("_"*50)

class Sample1:
    def __init__(self, max = 0):
        self.max = max

def __iter__(self):
    self.n = 0
    return self

def __next__(self):
    if self.n <= self.max:
        result = 2 * self.n
        self.n += 1
        return result
    else:
        raise StopIteration

a = Sample1(4)
i = iter(a)

print(next(i))
print(next(i))
print(next(i))

