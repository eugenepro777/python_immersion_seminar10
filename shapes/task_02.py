"""
Задание №2.
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    """Класс для создания прямоугольников"""

    def __init__(self, length=0, width=0):
        """
        Конструктор класса
        :param length: длина
        :param width: ширина
        """
        self.length = length
        self.width = width

    def calculate_perimeter_of_rectangle(self):
        rectangle_perimeter = 2 * (self.length + self.width)
        return rectangle_perimeter

    def calculate_area_of_rectangle(self):

        if self.length == 0:
            rectangle_area = self.width ** 2
            return rectangle_area
        elif self.width == 0:
            rectangle_area = self.length ** 2
            return rectangle_area
        rectangle_area = self.length * self.width

        return rectangle_area


if __name__ == '__main__':
    r1 = Rectangle(4, 2)
    r2 = Rectangle(0, 4)
    r3 = Rectangle(4)

    print(f'first rectangle: {r1.calculate_perimeter_of_rectangle() = } {r1.calculate_area_of_rectangle() = }')
    print(f'second rectangle: {r2.calculate_perimeter_of_rectangle() = } {r2.calculate_area_of_rectangle() = }')
    print(f'second rectangle: {r3.calculate_perimeter_of_rectangle() = } {r3.calculate_area_of_rectangle() = }')