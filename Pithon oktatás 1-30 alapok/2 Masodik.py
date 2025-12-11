s1 = "Teszt Elek"
s2=6
s3=5
print(s1,s2,s3)

name="Bela"

print (name)
print(s1[2])
print(s1[:3])
print(s1[:-1])
print(s1[-1])
print(s1[::2])#minden masodikat irja ki
print(s1[::-1])#visszafelé irja
print(s1+" a nevem")# kibőviti a változót
print(s1*10)# 10x irja kia valtozót
print(s1.upper())#nagybetüsitit a valtozót
s1=s1+" a nevem amit leirok"#felülirja a változót
print(s1)
print(s1.split())#feldarabolja a szóközök mentén alapból
print(s1.split("e"))#e betuk mentén darabolja fel a szöveget
#Halyőrzők
print("ez egy teszt szöveg berakok valamit ide{}".format("alma"))#ez egy helyorzo az almanak
print("ez egy teszt szöveg berakok valamit ide%s" % "alma")
print("első %s Masodik: %s %s" %("alma", "alma2","alma3"))
print("első %s Masodik: %s %s" %("alma", "alma2","alma3"))
print("Egy %s" %"alma")
print("Egy %r" %"alma")#Xreprezentativ erteket ad vissza
print("A szám %s" %4.75)
print("A szám %d" %4.75)#levágja a decimalt
print("A szám %2.3f" %4.75452)#kerekit 2 minimum szama a karaktereknek a szam előtt, kitölti szüközökkel ha nem éri el a megadott karakterszámot  a 3 azt jelenti hogy mennyi decimalis erteket tartalmazzon
print("Első: %s Masodik  %6.3f Marmadik %r" %("almava", 1.1123546, "citrom"))
print("A szöveg {} {} {}".format("alma", "barack","citrom"))
print("A szöveg {1} {2} {2}".format("alma", "barack","citrom"))
print("A szöveg {a} {b} {c}".format(c="alma",b="barack",a="citrom"))
#
print("{0:10} | {1:^10} | {2:10}" .format("Kosar","Mennyiség","Bolt"))
print("{0:10} | {1:^10} | {2:10}" .format("Alma",3,"Spar"))
print("{0:10} | {1:^10} | {2:10}" .format("Citromr",2,"Tesco"))
print("{0:10} | {1:^10} | {2:10}" .format("Paradicsom",2,"Auchan"))
print("-"*50)
#
print("{0:10} | {1:^10} | {2:10}" .format("Kosar","Mennyiség","Bolt"))
print("{0:10} | {1:^10} | {2:10}" .format("Alma",3,"Spar"))
print("{0:10} | {1:^10} | {2:10}" .format("Citromr",2,"Tesco"))
print("{0:10} | {1:^10} | {2:10}" .format("Paradicsom",2,"Auchan"))
print("-"*50)
#
print("a szam {0:10.2f}" .format(12.1234567))
name="\tjakab"
#print(f"a nevem"{name!r})#valami itt rossz megnezni
#
print(300>100)
print(300<100)
print(300==100)
#
#
#
lista1=["alma","barack",1]
print(len(lista1))
print(lista1[0])
print(lista1[1:])
print(lista1 + ["új elem"])
lista1=lista1+["új elem"]
lista1.append("citrom")
print(lista1)
pop_valtozo=lista1.pop()# pop lista elemet törölje, mindne ami a listahoz hozzanyul ovatosan kezelendő
print(pop_valtozo)
print(lista1)
lista1.reverse() #megforditja a lista sorrendjet, ez vegleges, hozzanyul a listahoz,
print(lista1)
#lista1.sort()
print(lista1)
print(lista1)
l1=[2,3,4]
l2=[5,6,7]
l3=[8,9,10]
matrix=[l1,l2,l3]
print(matrix)
print(matrix[1][1])
#
string_list=["alma","barack","citrom"]
print(string_list[2][-3:])
col1=[cv[0]for cv in matrix] #matrix listanak az első elemeit
print(col1)
#gyakorolni a kijelöléseket a listában, stringekből és számokból