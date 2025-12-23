# import minig azején és minden import külön sorban, mert lehet anotaciokat adni neki
from operator import truediv


# változó nevek - csak kisbetu, ha elvaalaszto akkor alulvonással

# ha hosszu akkor tördelni kell userAge = 33 ez igy helytelen
def long_method_name(variable_one, variable_two,
                     variable_three, variable_four):
    print(variable_two)


#a=b+c e igy helytelen mert eloiras hogy legyn szóköz az operatorok körül

# a fugvenyekhez kell dokstringeket

# tördelés ha van egy hosszu muvelet akkor  total = ((a * c) akkor itt is kell tördelni enterrel elote meg ezt \ hogy ne tegyen zarojelet
total = (b * c) + (a * b) + \
        (a * c) + (a - b) + (b + c)



# ha fugvenyben hasznalom az importot es egyszer kell hasznalnom akkkor mehet a fugvenybe, (ha tobb mint 1x haznlom akkkor az elejen kell feltuntetni) igy:
def fn1():
    import base64
    print('')

# a nem hasznalt vlo importoka el kell tavoitani

# ha logikai valtzokat hasznalunk kkor kerjk el a összehasonlitasok
some_var = True

if some_var == True:
    print('')

if some_var == None:
    print('ddd')

# ne legyenek a sor vegen ures szzokozok, ha sortores van akkor is ki kell torolni
# a sor hossza maximum 9 karakter lehet
# ne csinalj egysoros fugvenyeket helette legyen lambda
multiply_val = lambda x: x * 2

# kollekcio eseteben nem kell a zarojel utan szóköz

# sringeket hogy irunk: name = "Elek" vagy age = 33 vagy var = "Hello" + name +
var = 'Hello ' + name + ' kor: ' + str(age)
vagy
var = f'Hello {name} kor: {age}'
vagy
var = 'Hello {} kor: {}'.format(name, age)

# elagazasokban akkor lehet egy sorban ha egysoros

if some_var: print('gg')
#ez nem jo
if some_var and list1 and dic1 and var: print('gg')

if some_var and list1 and dic1 and var:
    print('gg')


# todo: valamit megcsianlni egy speci komment

