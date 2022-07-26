class Battery:
    """"Модель класу Battery (акумулятор)"""

    global range

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
