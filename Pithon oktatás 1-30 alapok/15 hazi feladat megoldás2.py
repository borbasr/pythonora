n = int(input("Adj meg egy számot: "))

str1 = ""
fac = 1
original_value=n
while n != 0:
    str1 = str1 + str(n) + "*"
    fac = fac * n
    var -= 1

print("A faktorialis a %s szamnak (%s! =%s) az %s" % (original_value, str1, fac, str1, fac))
