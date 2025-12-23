import csv
from collections import Counter

with open("teszt3.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        rows = list(reader)

data_rows = rows[1:]

col_5 = [row[-1] for row in data_rows if row[-1].strip()]
col_4 = [row[-2] for row in data_rows if row[-2].strip()]
col_3 = [row[-3] for row in data_rows if row[-3].strip()]
col_2 = [row[-4] for row in data_rows if row[-4].strip()]
col_1 = [row[-5] for row in data_rows if row[-5].strip()]

most_common_5 = Counter(col_5).most_common(1)[0][0]
most_common_4 = Counter(col_4).most_common(1)[0][0]
most_common_3 = Counter(col_3).most_common(1)[0][0]
most_common_2 = Counter(col_2).most_common(1)[0][0]
most_common_1 = Counter(col_1).most_common(1)[0][0]

print("Leggyakoribb érték az 1. oszlopban:", most_common_1)
print("Leggyakoribb érték az 2. oszlopban:", most_common_2)
print("Leggyakoribb érték az 3. oszlopban:", most_common_3)
print("Leggyakoribb érték az 4. oszlopban:", most_common_4)
print("Leggyakoribb érték az 5. oszlopban:", most_common_5)

print(col_5)