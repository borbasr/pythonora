#HF kerjunk be a felhasznalotol szamokat, pl egybe 2332225665 a paros szamok a bevitelben a paratlan szamok a bevitelben
# HF2 usev irjon be egy szamot pl6, output ******, majd 5*, majd 4 *
# irjon ki faktorialist ciklusasal pl az 5 faktorialis, 5! = 5*43*2*1 a vegen pedig kiirni a szamot

szamok = input("Adj meg számokat egybe írva (pl. 2332225665): ")

paros = set()
paratlan = set()

for szam in szamok:
    if szam.isdigit():
        if int(szam) % 2 == 0:
            paros.add(szam)
        else:
            paratlan.add(szam)

print("A páros számok a bevitelben:", " ".join(sorted(paros)))
print("A páratlan számok a bevitelben:", " ".join(sorted(paratlan)))

# Csillag-piramis program

n = int(input("Adj meg egy számot: "))

for i in range(n, 0, -1):   # n-től indul, 1-ig megy visszafelé
    print("*" * i)

# Faktoriális számítás ciklussal

n = int(input("Adj meg egy számot: "))

eredmeny = 1
lepesek = []

for i in range(n, 0, -1):
    eredmeny *= i
    lepesek.append(str(i))

# Az összes szorzási lépést kiírjuk
print(f"{n}! = " + "*".join(lepesek))
print("Eredmény:", eredmeny)

