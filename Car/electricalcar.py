class ElectricCar(Car):
    """Модель електроавтомобіля"""

    def __init__(self, make, model, year):
        """Ініціалізація атрибутів батьківського класу  Car"""
        # Car.__init__(self, make, model, year) 1 спосіб
        super().__init__(make, model, year)  # 2 спосіб
        self.battery = Battery()  # Атрибуту battery присвоюємо всі атрибути взяті з класу Battery