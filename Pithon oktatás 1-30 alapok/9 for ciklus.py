# for ciklus változó in lpééelcoó:
    #CM
lista1=[1,2,3,4,5,]
for item in lista1:
    if item % 2 == 0:
        print(item)

# for ciklus változó in lpééelcoó:
    #CM
sum=0
for item in lista1:
    sum=sum+item
print("Az usszes" +str(sum))#stringe kell elsonek alakitani

for item in "ez egy szoveg":
    print(item)

print("-"*50)

t1=(1,2,3,4,5,)
for t in t1:
    print(t)

print("t"*50)
lista2=[(1,2),(3,4)]
for tup in lista2:#minek lesz ez a for ciklus, törlődeik, tudok kesobb ra hivatkozni
    print(tup)

for (t1,t2) in lista2:#a zárójel az opcionális, nem szükséges,
    print("Első értéke"+str(t1))
    print("Második értéke"+str(t2))
    print(t2)

print("d"*50)
dict1={1:2,3:4,5:6,7:8 }
for item in dict1.items():
    print(item)
for (k, v) in dict1.items():
    print(k)
    print(v)

