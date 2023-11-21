"""
Задание №3.
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.

"""


class Human:

    def __init__(self, full_name, age, weight=0, height=0, gender='reptile'):
        self.full_name = full_name
        self.gender = gender
        self.weight = weight
        self.height = height
        self._age = age

    def birthday(self):
        if self._age < 150:
            self._age += 1
        else:
            print(f'Люди до такого возраста не доживают')
            self._age = 150

    def get_age(self):
        return self._age

    def get_full_name(self):
        return self.full_name

    def get_gender(self):
        return self.gender

    def get_anthropometric_data(self):
        return self.weight, self.height

    def get_info(self):
        return (f'Полное имя: {self.get_full_name()}, пол: {self.gender}\n'
                f'вес: {self.weight}, рост: {self.height}, возраст: {self.get_age()}')


if __name__ == '__main__':

    human_first = Human('Билл Гейтс', 67, 75, 170)

    print(f'{human_first.get_info()}')
    print(f'вес и рост: {human_first.get_anthropometric_data()}')
    print(f'пол: {human_first.get_gender()}')
    human_first.birthday()
    print(f'Билли исполнилось {human_first.get_age()}')