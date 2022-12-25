"""
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    """
    класс работник
    """
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': float(wage),
            'bonus': float(bonus),
        }

class Position(Worker):
    """
    класс получения данных о сотруднике
    """
    def get_full_name(self):
        """
        метод получения полного имени сотрудника"""
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        """
        метод получения дохода сотрудника с учётом премии"""
        print(f'{self._income["wage"] + self._income["bonus"]}')

john = Position('John', 'Doe', 'doctor', 60000, 25000)
jane = Position('Jane', 'Doe', 'layer', '130000', '0')


john.get_full_name()
john.get_total_income()

jane.get_full_name()
jane.get_total_income()
