Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from abc import ABC, abstractmethod
import math

class Vehicle:
    def __init__(self, make='', model=''):
        self.make = make
        self.model = model
    def description(self):
        return f"{self.__class__.__name__}: {self.make} {self.model}"
    def move(self):
        return "The vehicle moves."

class Car(Vehicle):
    def move(self):
        return "The car drives on roads."

class Bike(Vehicle):
    def move(self):
        return "The bike is pedalled along paths."

class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def total_area(shapes):
    return sum(s.area() for s in shapes)

class ShapeBase:
    def __init__(self, name='ShapeBase'):
        self.name = name
    def calculate_area(self):
        return 0

class RectangleDerived(ShapeBase):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        super().__init__(name='RectangleDerived')
        return self.width * self.height

def process_sound(sound_object):
    return sound_object.make_sound()

class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class FileHandler(ABC):
    @abstractmethod
    def read(self, path):
        pass
    @abstractmethod
    def write(self, path, data):
        pass

class TextFileHandler(FileHandler):
    def read(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    def write(self, path, data):
...         with open(path, 'w', encoding='utf-8') as f:
...             f.write(data)
... 
... class BinaryFileHandler(FileHandler):
...     def read(self, path):
...         with open(path, 'rb') as f:
...             return f.read()
...     def write(self, path, data):
...         with open(path, 'wb') as f:
...             f.write(data)
... 
... if __name__ == "__main__":
...     v = Vehicle("GenericMake", "ModelX")
...     c = Car("Toyota", "Corolla")
...     b = Bike("Giant", "Escape")
...     print(v.description())
...     print(v.move())
...     print(c.description())
...     print(c.move())
...     print(b.description())
...     print(b.move())
... 
...     shapes = [Circle(1), Rectangle(2, 3), Circle(2.5)]
...     print("Total area:", total_area(shapes))
... 
...     rd = RectangleDerived(3, 4)
...     print("RectangleDerived area:", rd.calculate_area())
...     print("RectangleDerived name after super init:", rd.name)
... 
...     print("Dog says:", process_sound(Dog()))
...     print("Cat says:", process_sound(Cat()))
... 
...     tf = TextFileHandler()
...     bf = BinaryFileHandler()
...     text_path = "demo_text.txt"
...     bin_path = "demo_bin.bin"
...     tf.write(text_path, "Hello, TextFileHandler!")
...     print("Text read:", tf.read(text_path))
...     bf.write(bin_path, b"\x00\x01\x02\x03")
