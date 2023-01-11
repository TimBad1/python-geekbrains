"""
4) Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
к атрибутам, выведите результат. Выполните вызов методов и также покажите
результат.
"""

class Car:
    """
    class Car
    """
    def __init__(self, speed, color, name, is_police = False):

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """сообщение что машина начала движение"""
        print('машина поехала')

    def stop(self):
        """сообщение о том что машина остановилась"""
        print('машина остановилась')

    def turn(self, direction):
        """сообщение о направлении поворота машины"""
        print(f'машина повернула {direction}')

    def show_speed(self):
        """сообщение о скорости движение машины"""
        print(f'скорость автомобиля {self.speed}км/ч')

class TownCar(Car):
    """подкласс TownCar"""
    def show_speed(self):
        print(f'скорость автомобиля {self.speed}км/ч')
        if self.speed > 60:
            print('вы превысили скорость')

class WorkCar(Car):
    """подкласс WorkCar"""
    def show_speed(self):
        print(f'скорость автомобиля {self.speed}км/ч')
        if self.speed > 40:
            print('вы превысили скорость')

class PoliceCar(Car):
    """подкласс WorkCar"""
    is_police = True


class SportCar(Car):
    """подкласс class SportCar"""
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


car1 = PoliceCar(60, 'red', 'Porsche', True)
car2 = WorkCar(50, 'white', 'Ford')
car3 = TownCar(70, 'black', 'vaz')
car4 = SportCar(120, 'blue', 'lamborghini')
car5 = Car(75, 'blue', 'BMW')

car2.show_speed()
car3.show_speed()
car4.show_speed()
car5.show_speed()

print(car5.color)
car1.turn('налево')
