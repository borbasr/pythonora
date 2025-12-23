import sys
import os

user_input=""
count_loop = 0
while not user_input.isdigit():
    os.system("cls")
    if count_loop > 0:
        print("Rossz imputot adtal meg te hulye")
    user_input = input("Irjon be számokat: (vagy exit ha ki akar lepni")
    if user_input.lower() == 'exit':
        sys.exit("Hibas adatot adtal meg  es kilepek")
    count_loop +=1
add_list = []
even_list = []

for i in user_input:
    if int(i) % 2 == 0 and  int(i) not in even_list:
        even_list.append(i)
    elif int(i) % 2 == 0 and int(i) not in add_list:
        add_list.append(i)

if not even_list:
    print("Nincs páros szám a bevitelben")
else:
    if len(even_list) == 1:
        print("A páros szám a bevitelben a következő %s" % even_list[0])
    else:
        print("A páratlan számok a bevitelbena következő %s" % even_list[0])
