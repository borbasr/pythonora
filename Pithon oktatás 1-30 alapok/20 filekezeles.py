import csv
from csv import DictReader
from io import DictWriter

data =[
    [1,2,"cica3"],
    [4,5,6],
    [7,8,9]
]
file=open("test.csv", "w", encoding="utf-8")
writer=csv.writer(file)


with open("teszt.csv", "r", encoding="utf-8") as file:
    var=csv.reader(file)
    print(var)
    for irem in var:
        print(irem)


with open("test3.csv","r",encoding="utf-8",newline="") as file:
    dict_reader=DictReader(file)
    for row in dict_reader:
        print(row["GYumolcs"])

with open("test4.csv","w",encoding="utf-8",newline="") as file:
    header=["Nev","Email","Lakhely"]
    dict_writer=DictWriter(file,fieldnames=header, dialect="valami")
    dict_writer.writerow({
        "Nev": "Teszt Elek"
        "Email": "Teszt Elek"
        "Lakhely": "Teszt Elek"
    })

#Házi feladat - Googleben otos lotto csv letölteni, majd 'szerencse program' oazloponként melyek voltak a leggyakoribbak, oszloponként,
