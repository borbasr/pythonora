try:
    f = open('test.txt', 'r')
    f.write('valami')
except FileNotFoundError:
    print('Nincs meg a fajl')
except IOError:
    print('Iras hiba')
except:
    print('Kritikus hiba tortent')
else:
    print('Siker eseten hajtodik vegre')
    f.close()
finally:
    print('Minden esetben lefut')

# cegeknel lehet no exeption policy ahol nem lehet hasznalni wxcept
