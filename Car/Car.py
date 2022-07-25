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


class ElectricCar(Car):
    """Модель електроавтомобіля"""

    def __init__(self, make, model, year):
        """Започатковуємо атрибути батьківського класу"""
        super().__init__(make, model, year)





my_car = ElectricCar("Tesla", "model x", "2020")
print(my_car.get_descriptive_name())

# Внесення даних одометра
my_car.update_odometer(192000)
# Зчитування даних одометра
my_car.read_odometer()

my_car.increment_odometer(250)
my_car.read_odometer()

