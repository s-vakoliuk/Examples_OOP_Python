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
        print(f" Цей автомобіль має {self.odometer_reading} км. пробігу")


my_car = Car("FIAT", "Grande Punto", "2007")
print(my_car.get_descriptive_name())

my_car.read_odometer()
