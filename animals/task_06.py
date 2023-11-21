"""
Задание №6.
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""

# В принципе ничто нам не мешает импортировать наши классы из прошлой задачи,
# но здесь мы их немного переделали


class Animal:
    """
    Конструктор класса Животное.

    :param name: Имя животного.
    :param kind: Тип животного
    :param habitat: Место обитания животного.
    :param age: Возраст животного.
    :param weight: Вес животного.
    :param lifespan: Средняя продолжительность жизни животного.
    """
    def __init__(self, kind, name, habitat, age, weight, lifespan):
        self.kind = kind
        self.name = name
        self.habitat = habitat
        self.age = age
        self.weight = weight
        self.lifespan = lifespan
        self.is_sleeping = False

    def get_kind(self):
        """Метод получения типа животного"""
        return self.kind

    def get_name(self):
        """Метод получения имени животного"""
        return self.name

    def get_habitat(self):
        """Метод получения среды обитания животного"""
        return self.habitat

    def sleep(self):
        """
        Выводит информацию о том что животное спит.
        """
        self.is_sleeping = True
        print(f"{self.kind} {self.name} спит.")

    def show_info(self):
        """
        Выводит общую информацию о животном.
        """
        print(f"Вид: {self.kind}\n"
              f"Имя: {self.name}\n"
              f"Место обитания: {self.habitat}\n"
              f"Возраст: {self.age} лет\n"
              f"Вес: {self.weight} кг\n"
              f"Средняя продолжительность жизни: {self.lifespan} лет\n"
              f"Животное {'спит' if self.is_sleeping else 'не спит'}")


class Fish(Animal):
    """
    Конструктор класса Рыба.

    :param fin_size: Размер плавников рыбы.
    """
    def __init__(self, kind, name, habitat, age, weight, lifespan, fin_size):
        # через super().__init__() мы обращаемся к конструктору класса-родителя
        super().__init__(kind, name, habitat, age, weight, lifespan)
        self.fin_size = fin_size
        self.is_swimming = False

    def get_fin_size(self):
        """Выводит информацию о размере плавников"""
        return self.fin_size

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

    # этот метод мы переопределяем в классах-наследниках
    def show_info(self):
        """Метод, выводящий общую информацию о рыбе"""
        # через super(). мы обращаемся к методу show_info() родительского класса и берем часть информации из него
        super().show_info()
        # self.get_fin_size() - здесь мы получаем информацию через метод класса, а не через обращение к атрибуту
        print(f"{self.kind} имеет размер плавников {self.get_fin_size()} см\n"
              f"{self.kind} {'плавает' if self.is_swimming else 'не плавает'}")


class Bird(Animal):
    """
    Конструктор класса Птица.

    :param wingspan: Размах крыльев птицы.
    """
    def __init__(self, kind, name, habitat, age, weight, lifespan, wingspan):
        super().__init__(kind, name, habitat, age, weight, lifespan)
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
        super().show_info()
        print(f"{self.kind} имеет размах крыльев {self.wingspan} м\n"
              f"{self.kind} {'летает' if self.is_flying else 'не летает'}")


class Mammal(Animal):
    """
    Конструктор класса Млекопитающее.

    :param color: Цвет меха млекопитающего.
    """
    def __init__(self, kind, name, habitat, age, weight, lifespan, color):
        super().__init__(kind, name, habitat, age, weight, lifespan)
        self.color = color
        self.is_licking = False

    def give_birth(self):
        """
        Выводит информацию о том что млекопитающие рождают потомство
        """
        print(f"{self.kind} {self.name} рождает детенышей")

    def nurse_young(self):
        """
        Выводит информацию о том что млекопитающее кормит своих детенышей.
        """
        print(f"{self.kind} {self.name} кормит своих детенышей молоком")

    def licking(self):
        """Выводит информацию о том что млекопитающее вылизывается"""
        self.is_licking = True
        print(f"{self.kind} {self.name} вылизывается, очищая шерсть окраса {self.color}")

    def show_info(self):
        """
        Метод, выводящий общую информацию о млекопитающем.
        """
        super().show_info()
        print(f"{self.kind} имеет окрас - {self.color}\n"
              f"{self.kind} {'вылизывается' if self.is_licking else 'не вылизывается'}")


# Пример использования классов
nemo = Fish("Рыба", "Немо", "тропический риф", 1, 0.2, 5, 15)
nemo.swim()
nemo.breathe_underwater()
nemo.spawn_eggs()
print('***************************************************************************************************')
nemo.show_info()
print('***************************************************************************************************')
robin = Bird("Птица", "Малиновка", "лес", 2, 0.1, 3, 0.25)
robin.fly()
robin.build_nest()
robin.lay_eggs()
print('***************************************************************************************************')
robin.show_info()
print('***************************************************************************************************')
lion = Mammal("Лев", "Пумба", "саванна", 5, 200, 15, "рыжий")
lion.licking()
lion.give_birth()
lion.nurse_young()
lion.sleep()
print('***************************************************************************************************')
lion.show_info()