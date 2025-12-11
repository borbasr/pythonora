var=input("Irj be valamit:")
count=0
for character in var:
    if character.lower in ["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű","A","Á","E","É","I","Í","O","Ó","Ö","Ő","U","Ú"]:
       count+=1
    print("A szöveg %s hosszu"%len(var))
    print("a szövegben %s maganhangzo szerepel" %count)