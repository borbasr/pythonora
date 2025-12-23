import sys

print('argumentumok: ', sys.argv)
if len(sys.argv) > 1:
    print('Az elso argumentum: ', sys.argv[1])
else:
    print('Nem adtal meg argumentumot!')
