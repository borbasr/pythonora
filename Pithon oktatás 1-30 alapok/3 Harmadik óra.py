#Dictionery, kulcsérték kollekció, létrehozáshoz kapcsos zarojel{}
dict1={"kulcs1":"ertek1","kulcs2":"ertek2"}
print(dict1["kulcs1"])
#print(dict1["kulcs22"])
dict2={"k1":123,"k2":[12,34,46],"k3":["alma","körte","eper"]}
print(dict2["k3"][0].upper())
dict2["k2"].append(55)
print(dict2)
#dict3 = {"k1": 'alma", "k2": {"ak1": {"aak1" : "citrom"}}}
#print(dict3["k2"]["ak1"]["aak1"])
print(dict2.keys())
print(dict2.values())
print(dict2.items())
print(dict2.get("k2"))#ugyanaz mint az items csak nincs hiaüzenet
#kulcsok legyenek homogének, hasonóak, ne legyen benne szóköz,
dict4={}
dict4.update(dict2)
dict4.update(dict1)
print(dict4)
dict2.clear()
print(dict2)
print(dict2.get("k2","ez a kulcs nem szerepel a szotarban"))
#Tuple majdnem olyan mint a lista, nem lehet megvaltoztatni a tartalmat, legygyorsabb kolleklciotipus, keves metodusa van
t1=(1,2,3)
print(len(t1))
t2=("ey,2")
print(t2 in t1)
print(t2.index("ey"))
#t2[0]="ketto"
t3=(50,)#egy elemü tuple
print(t3)
# halmaz, rendezetlen, változtatható,
s1=set()
s1.add(1)
s1.add(2)
pint(s1)
print(dict2.keys())
print(dict2.values())
print(dict2.items())


