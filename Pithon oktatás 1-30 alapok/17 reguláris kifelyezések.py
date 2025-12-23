# re mulud segitsegevel fogjuk a szintaktikajak fehasználni
# a legjobb iromany a regularis kifelyezesekben: a microsoft keszitette,
# https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference

import re
import unicodedata
var="Elemezzük ki ezt a mondatot pythonban"
m = re.match(r"(.*) ezt (.*)",var)
if m:
    print(m.group())
    print(m.group(1))
    print(m.group(2))

s = re.search(r"(pythonban)",var)
if s:
    print(s.group())
else:
    print("nincs találat")

email = "info@t_rosz_est.com"
m = re.match(r"(.*) rosz (.*)",email)


telefon="kerem hivja ezt a szamot # +36203561546"
t_number=re.sub(r"\D","",telefon)
print(t_number)

# Hafi feladat a microsoftos oldalt nezegenti, és átnézni a regularis kifelyezeseket
# megtanulni a microsoftos oldalt mert a ai es a deep learning területén nagyon fontos lesz későtt

#ékezetek eltüntetése

text = "árvíztűrő tükrófúrógép"
#text = re.sub(r"[Áá]","a",text) egy valtozat manualisan kiurjuk 1 változat és kicseréli az ékezetes karatereket arra amit megadunk
nfd = unicodedata.normalize("NFD",text)
clean=re.sub(r"[\u0300-\u036f]","",nfd)
print(clean)

#