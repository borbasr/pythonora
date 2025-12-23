from typing import Protocol, runtime_checkable


@runtime_checkable
class Greeting(Protocol):
    def greet(self, name: str) -> str: ...


class EnglishGreet:
    def greet(self, name: str):
        return f'Hello {name}'


class HunGreet:
    def greet(self, name: str):
        return f'Szia {name}'

def test_greet(g: Greeting, who: str):
    print(g.greet(who))


test_greet(EnglishGreet(), who='Elek' )
test_greet(HunGreet(), who='Elek' )

obj = HunGreet()
print(isinstance(obj, Greeting))
print(isinstance(obj, HunGreet))