"""
Задание №5.
Создайте три (или более) отдельных классов животных.
Например, рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""


class Fish:
    def __init__(self, kind, name, habitat, age):
        self.kind = kind
        self.name = name
        self.age = age
        self.habitat = habitat
        self.is_swimming = False

    def swim(self):
        """Выводит информацию о том что рыба плавает"""
        self.is_swimming = True
        print(f'{self.kind} {self.name} плавает в {self.habitat}')

    def breathe_underwater(self):
        """Описывает что рыба дышит под водой"""
        print(f'{self.kind} {self.name} дышит под водой')

    def spawn_eggs(self):
        """Описывает что рыба откладывает икру"""
        print(f'{self.kind} {self.name} откладывает икру в {self.habitat}')

    def show_info(self):
        """Метод, выводящий общую информацию о рыбе"""
        print(f"{self.kind} по имени {self.name}, среда обитания - {self.habitat}\n"
              f"{self.kind} {'плавает' if self.is_swimming else 'не плавает'}")


class Bird:
    def __init__(self, kind, name, age, wingspan):
        self.kind = kind
        self.name = name
        self.age = age
        self.wingspan = wingspan
        self.is_flying = False

    def fly(self):
        """Выводит информацию о том что птица летает"""
        self.is_flying = True
        print(f'{self.kind} {self.name} парит в воздухе и имеет размах крыльев {self.wingspan} метра')

    def build_nest(self):
        """Выводит информацию о том что птица строит гнезда"""
        print(f'{self.kind} {self.name} строит гнездо для птенцов')

    def lay_eggs(self):
        """
        Выводит информацию о том что птица откладывает яйца
        """
        print(f'{self.kind} {self.name} откладывает яйца в гнезде')

    def show_info(self):
        """
        Метод, выводящий общую информацию о птице.
        """
        print(f"{self.kind} по имени {self.name}, размах крыльев {self.wingspan} м\n"
              f"{self.kind} {'летает' if self.is_flying else 'не летает'}")


class Mammal:
    def __init__(self, kind, name, age, color):
        self.kind = kind
        self.name = name
        self.age = age
        self.color = color
        self.is_licking = False

    def give_birth(self):
        """
        Выводит информацию о том что млекопитающие рождает потомство
        """
        print(f"{self.kind} {self.name} рождает детенышей")

    def nurse_young(self):
        """
        Выводит информацию о том что млекопитающие кормит своих детенышей.
        """
        print(f"{self.kind} {self.name} кормит своих детенышей молоком")

    def licking(self):
        """Выводит информацию о том что млекопитающее вылизывается"""
        self.is_licking = True
        print(f"{self.kind} {self.name} вылизывается очищая шерсть окраса {self.color}")

    def show_info(self):
        """
        Метод, выводящий общую информацию о млекопитающем.
        """
        print(f"{self.kind} по имени {self.name}, окрас - {self.color}\n"
              f"{self.kind} {'вылизывается' if self.is_licking else 'не вылизывается'}")


if __name__ == '__main__':

    nemo = Fish("Рыба", "Немо", "тропический риф", 4)
    nemo.swim()
    nemo.breathe_underwater()
    nemo.spawn_eggs()
    nemo.show_info()

    robin = Bird("Птица", "Малиновка", 1, 0.3)
    robin.fly()
    robin.build_nest()
    robin.lay_eggs()
    robin.show_info()

    lion = Mammal("Лев", "Рыжик", 5, "рыжий")
    lion.licking()
    lion.give_birth()
    lion.nurse_young()
    lion.show_info()