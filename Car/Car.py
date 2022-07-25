class Car:
    """Модель класу Car (автомобіль)"""

    def __init__(self, make, model, year):
        """Ініціалізація атрибутів класу Car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Getter повертає інформацію про авто"""
        long_name = f"{self.make} - {self.model} - {self.year}"
        return long_name

    def read_odometer(self):
        """Вивести повідомлення пробігу автомобіля"""
        print(f"Цей автомобіль має {self.odometer_reading} км. пробігу")

    def update_odometer(self, kmage):
        """Задати/Оновити значення одометра"""
        if kmage >= self.odometer_reading:
            self.odometer_reading = kmage
        else:
            print("Ти не можеш відмотати показник одометра назад")

    def increment_odometer(self, km):
        """Додати задане значення до показника одометра"""
        self.odometer_reading += km


class Battery:
    """"Модель класу Battery (акумулятор)"""

    def __init__(self, battery_size=75):
        """Ініціалізуємо атрибути"""
        self.battery_size = battery_size

    def get_range(self):
        """Вивести повідомлення про відстань, яку може подолати авто відповідно до ємності акумулятора"""
    if self.battery_size == 75:
        range = 260
    elif self.battery_size == 100:
        range = 315
    print(f"Це авто може долати до {range} км при повному заряді акумулятора")

    def describe_battery(self):
        """Вивести повідомлення про стан об'єму акумулятора"""
        print(f"Це авто має {self.battery_size} - KWh потужності")


class ElectricCar(Car):
    """Модель електроавтомобіля"""

    def __init__(self, make, model, year):
        """Ініціалізація атрибутів батьківського класу  Car"""
        # Car.__init__(self, make, model, year) 1 спосіб
        super().__init__(make, model, year)  # 2 спосіб
        self.battery = Battery()


my_car = ElectricCar("Tesla", "model x", "2020")
print(my_car.get_descriptive_name())

my_car.battery.describe_battery()
my_car.battery.get_range()
