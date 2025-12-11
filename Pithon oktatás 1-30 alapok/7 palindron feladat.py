var=input("Irj be egy szót:")
if var.lower() == var[::-1].lower():#kisbetusse kell alakitani
    print("Palindron")
else:
    print("te punci")