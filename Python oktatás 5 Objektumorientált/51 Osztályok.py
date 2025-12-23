
# mi az a "framework"
class ValamilyenNev:
    v1 = 'alma'

    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

    def osszead(self, a, b):
        return a + b

print(ValamilyenNev.v1)
obj1 = ValamilyenNev(nev='Elek', kor=33)
print(obj1.v1)
print(obj1.nev)
print(obj1.kor)
print(obj1.osszead(1, 2))

class Counter:
    def __init__(self, start=0):
        self.start = start

    def __call__(self, step=1):
        self.start += step
        return self.start

c = Counter(10)
print(c())
print(c(6))
print(c)

lass Madar:
    def __init__(self, szine):
        self.szine = szine


class Sas(Madar):
    def __init__(self, szin, hus_napi_mennyisege):
        super().__init__(szin)
        self.hus = hus_napi_mennyisege

    def fn2(self):
        print(self.szine)
        print(self._v1)
        # print(self.__v2)

sas1 = Sas(szin='barna', hus_napi_mennyisege=5)
print(sas1.szine)
print(sas1.hus)

print('#' * 10)
sas1.fn1()
print('-' * 10)
sas1.fn2()

print(sas1._v1)
print(sas1.__v2)



