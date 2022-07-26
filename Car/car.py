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