var=input("Irj be egy szöveget:")
list1=var.split(" ")
list1.reverse()
string1="".join(list1)
output=" "
for c in string1:
output += c
print(output)

