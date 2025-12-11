# halmaz, rendezetlen, változtatható,
s1=set()
s1.add(1)
s1.add(2)
print(s1)
s2={4,"alma",44}
print(s2)
list1=[1,1,1,2,2,3]
list2=list(set(list1))
print(list2)
s2.discard("alma")
print(s2)
s2.remove(44)
print(s2)


#Sorozat, range,
print(range(10))
print(range(2, 10).count(2))
print(range(2,10,2)[2])
print(range(0,1000000)) #végtelen számú számot tudunk letárolni a véges memóriában
#Verérlési szerkezetek
