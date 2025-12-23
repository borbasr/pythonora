print(list("abcdefghij"))
print(enumerate("abcdefghij"))

for (i,letter) in enumerate("abcdefghij"):
    print(i)

list1=[1,2,3,4,5]
lista2=["a","b","c","d","e"]

print(list(zip(list1, lista2)))

for i in range(0,6):
    print("{0:>{i}}".format("*",i))


