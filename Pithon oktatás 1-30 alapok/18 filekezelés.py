# filek megnyitása open parancsal, le kell irni hogy mire sezretnénk megnyitni, olvasás, irás,
import csv

file_read=open("test.txt", "r", encoding="utf-8")
print(file_read.read())
file_read.close()

with open("test.txt", "r", encoding="utf-8") as var:
    print(var.read())

with open("test.txt", "w", encoding="utf-8") as file:
    file.write("alma\r\n")
    file.write("körte\r\n")
    file.write("dió\r\n")

with open("test.txt", "a", encoding="utf-8") as file:
    file.write("teszt\n")

#r+ módositás a 0. poziciotol kezdve
#az r+ m d lerehozni mint a write
#with open("test.txt","r+",encoding="utf-8") as file:#ki tudom valasztani hogy melyik pozicio modositsa a
#    file.seek(6)
#    file.write("####")

with open("teszt.csv", "r", encoding="utf-8") as file:
    var=csv.reader(file)
    print(var)
    for irem in var:
        print(irem)

print("-"*20)

print("-"*20)
csv.register_dialect("valami", delimiter=";", quoting=csv.QUOTE_NONE)
with open("teszt2.csv", "r", encoding="utf-8") as file:
    var=csv.reader(file, delimeter="valami")
    for irem in var:
        print(irem)