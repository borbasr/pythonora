import csv
from collections import Counter

list1 =[]
list2 = []
list3 = []
list4 = []
list5 = []
csv.register_dialect("lotto",delimeter=";", quoting=csv.QUOTE_NONE)
with open("teszt3.csv", "r", encoding="utf-8", newline="") as file:
    csv_reader = csv.reader(file, dialect="lotto")
    for row in csv_reader:
        list1.append(row[-5])
        list2.append(row[-4])
        list3.append(row[-3])
        list4.append(row[-2])
        list5.append(row[-1])

first=Counter(list1)
second = Counter(list2)
third = Counter(list3)
fourth = Counter(list4)
fifth = Counter(list5)
print(first.most_common(1)[0][0])
print(second.most_common(1)[0][0])
print(third.most_common(1)[0][0])
print(fourth.most_common(1)[0][0])
print(fifth.most_common(1)[0][0])
