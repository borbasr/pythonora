def first_decorator(fn):
    def inner_fn():
        print("denkorator fgv vagyok")
        fn()

    return inner_fn

def simple_fn():
    print("Egy egy teljesen sima fgv")

d = first_decorator(simple_fn)
d()

@first_decorator
def simple_fn2():
    print("Egy egy teljesen sima fgv)  2")

simple_fn2()

print("_"*50)

def divide_decorator(fn):
    def inner(a, b):
        print(f"Elosztok egymással két számot az   {a} és {b} számot ")
        if b == 0:
            print('Nem lehet 0-val osztani!')
            return
        return fn(a, b)
    return inner

@divide_decorator
def divide(a, b):
    return a / b

print(divide(a=10, b=2))
print(divide(a=10, b=0))

def star(fn):
    def inner(*args, **kwargs):
        print('*' * 50)
        fn(*args, **kwargs)
        print('*' * 50)
    return inner


def equals(fn):
    def inner(*args, **kwargs):
        print('=' * 50)
        fn(*args, **kwargs)
        print('=' * 50)
    return inner


@star
@equals
def disp1(v1):
    print(v1)


@star
@equals
def disp2(v1, v2):
    print(v1)
    print(v2)


disp1('alma')
disp2(v1=1, v2=2)
