import re
from datetime import datetime
from task_03 import Human

"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""


class Employee(Human):

    __max_access_level = 7
    __BONUS_PERCENTAGE = 15
    __EXPERIENCE_PAYMENT = 3

    def __init__(self, employee_id, company, salary, *args, **kwargs):
        self._employee_id = self.validate_employee_id(employee_id)
        self._access_level = self.calculate_access_level()
        self.company = company
        self.hire_date = datetime.now()
        self._salary = salary
        super().__init__(*args, **kwargs)

    def get_company(self):
        return self.company

    def get_access_level(self):
        return self._access_level

    def get_employee_id(self):
        return self._employee_id

    def get_salary(self):
        return self._salary

    @staticmethod
    def validate_employee_id(employee_id):
        """
        Проверка на предоставление шестизначного ID сотрудника
        :param employee_id: ID сотрудника
        :return: ID сотрудника
        """
        if not (isinstance(employee_id, int) and 100000 <= employee_id <= 999999):
            raise ValueError("Идентификационный номер только шестизначный!")
        return employee_id

    def calculate_access_level(self):
        """
        Вычисление уровня доступа сотрудника по его ID
        :return: Уровень доступа сотрудника
        """
        sum_digits = sum(int(digit) for digit in str(self._employee_id))
        return sum_digits % 7

    def _check_access_level(self):
        """
        Проверка возможности увеличения уровня доступа сотрудника
        :return: да или нет
        """
        return self._access_level < self.__max_access_level

    def promote_up(self):
        """
        Повышение уровня доступа сотрудника, если у него не максимальный уровень доступа
        :return: Уровень доступа сотрудника
        """
        if self._check_access_level():
            self._access_level += 1
        else:
            self._access_level = self.__max_access_level

    def year_of_service(self):
        """
        Вычисление рабочего стажа сотрудника (в годах)
        :return: Рабочий стаж в годах
        """
        current_date = datetime.now()
        years_of_service = (current_date - self.hire_date).days // 365
        return years_of_service

    def calculate_service_bonus(self):
        """
        Вычисление доплаты за стаж работы
        :return: Сумма доплаты
        """
        years_of_service = self.year_of_service()
        bonus_years = max(0, years_of_service - self.__EXPERIENCE_PAYMENT)
        total_bonus = (self.__BONUS_PERCENTAGE / 100) * self._salary * bonus_years

        return total_bonus

    def award_service_bonus(self):
        """
        Вычисление оклада с учётом доплаты за стаж
        :return: Новый оклад
        """
        service_bonus = self.calculate_service_bonus()
        self._salary += service_bonus
        return self._salary

    def work_overtime(self, hours):
        """
        Показывает переработку сотрудника в часах
        :param hours: Часы переработки
        :return: Часы переработки для конкретного сотрудника
        """
        return f'Сотрудник {self.get_full_name()} имеет переработку в часах: {hours}'

    def get_info(self):
        """
        Показывает полную информацию о сотруднике
        :return: Название компании, ID, уровень доступа, зарплату
        """
        return (f'Сотрудник компании: {self.get_company()}\n'
                f'Полное имя: {self.get_full_name()}, возраст: {self.get_age()}, пол: {self.gender}\n'
                f'Номер ID: {self._employee_id}\nУровень доступа: {self._access_level}\n'                
                f'Зарплата: {self._salary}')

    # def is_check_id(self):
    #     pattern = r'\A\d{6}\Z'
    #     if re.match(pattern, self._employee_id):
    #         return True
    #     else:
    #         return False


employee1 = Employee(223456, 'Max', 10000, 'Nice', 34, gender='M')
print(employee1.get_info())