v1=2
v2=3
v4=4
v5=5
v6=6
v7=7
l1=[v1,v2,v4]
l2=[v5,v6,v7]
print("{0:12} | {1:^12} | {2:12}" .format("Kosar","Mennyiség","Bolt"))
print("{0:12} | {1:^12} | {2:12}" .format("Paradicsom",1,"Dpst"))
print("{0:12} | {1:^12} | {2:12}" .format("Dinye",3,"Suvhsn"))
print("{0:12} | {1:^12} | {2:12}" .format("Paprika",3,"Trdzz"))
print("{0:12} | {1:^12} | {2:12}" .format("Mandarin",4,"Bolt"))
print("_"*50)



l1=["alma","körte","barack","diszno"]
print(len(l1))
print(l1[1][2])
l1.append("vanilia")
print(l1)
l1.pop(3)
print(l1)