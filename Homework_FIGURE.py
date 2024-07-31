import math # модуль дл вычичсления квадратного уравнения

class Figure: # основной главный клас для всех фигур
    def __init__(self): # метод для базового конструктора
        pass
        # оператор-заполнитель

    def area(self):  # метод для вычисления площади
        pass


    def perimeter(self): # метод для вычисления периметрам
        pass


    def __str__(self):
        pass
        # метод для строкового представления

class Triangle(Figure): # подкласс для объекта Треугольник
    def __init__(self, a, b, c): # принимаем три стороны треугольника
        super().__init__() # вызов конструктора базового класса (для наследования и расширения, поддержки иерархии
        if not all(isinstance(side, (int)) and side > 0 for side in [a, b,c]): # проверка что стороны фигуры целые числа и положительные
            raise Error("Значения сторон должны быть целфми положительными числами")
        self.a = a
        self.b = b
        self.c = c


    def area(self):
        pp = (self.a + self.b + self.c) / 2 # вычисляем полупериметр
        return math.sqrt(pp * (pp - self.a) * (pp - self.b) * (pp - self.c)) # вычисляем площадь

    def perimeter(self):
        return self.a + self.b + self.c # вычисляем периметр

    def __str__(self):
        return f"Стороны треугольника {self.a}, {self.b}, {self.c}"

class Rectangle(Figure): # подкласс для объекта Прямоугольник
    def __init__(self, length, width):
        super().__init__()
        if not all(isinstance(value, (int)) and value > 0 for value in [length, width]):
            raise Error("Значения сторон должны быть целыми положительными числами")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length * self.width)

    def __str__(self):
        return f"Стороны прямоуголника: длина {self.length }, ширина {self.width}"

class Circle(Figure): # подкласс для объекта Круг
    def __init__(self, radius):
        super().__init__()
        if not isinstance(radius, (int)) and radius >= 0:
            raise Error("Радиус должен быть полоительным значением")
        self.radius = radius

    def area(self):
        return math.pi * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Радиус круга {self.radius}"

tirangle = Triangle(5, 3, 6)
rectangle = Rectangle(5, 8)
circle = Circle(5)

print(tirangle)
print(f"Площадь треугольника: {tirangle.area()}, периметр треугольника: {tirangle.perimeter()}")

print(rectangle)
print(f"Площадь прямоугольника: {rectangle.area()}, периметр прямоугольника: {rectangle.perimeter()}")

print(circle)
print(f"Площадь круга: {circle.area()}, периметр круга: {circle.perimeter()}")
