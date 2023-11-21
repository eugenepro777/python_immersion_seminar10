from math import pi, pow

"""
Задание №1.
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""


class Circle:
    """Класс для создания окружностей"""
    # a = 1

    def __init__(self, radius):
        """
        Конструктор класса
        :param radius: радиус окружности
        """
        self.radius = radius

    def calculate_length_of_circle(self):
        circle_length = 2 * pi * self.radius
        return round(circle_length)

    def calculate_area_of_circle(self):
        circle_area = pi * pow(self.radius, 2)
        return round(circle_area, 2)


if __name__ == '__main__':
    circle_first = Circle(4)
    circle_second = Circle(10)

    print(f'Площадь первой окружности {circle_first.calculate_area_of_circle() = }')
    print(f'Длина второй окружности {circle_second.calculate_length_of_circle() = }')
    # print(Circle.__dict__)