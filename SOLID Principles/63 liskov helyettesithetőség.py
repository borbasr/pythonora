# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     def set_width(self, width):
#         self.width = width
#         self.height = width

# ez igy helyes az előző nél pedig nem helyettesithető a gyerek a szülővel

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

