class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} начала движение"

    def stop(self):
        return f"{self.name} прекратила движение"

    def turn_left(self):
        return f"{self.name} совершила поворот налево"

    def turn_right(self):
        return f"{self.name} совершила поворот направо"

    def show_speed(self):
        return f"{self.name} движется со скоростью {self.speed}. Скорость в пределах нормы."


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            speed_now = self.speed - 60
            return(f"{self.name} движется со скоростью {self.speed}. Скорость превышена на {speed_now} км/час!")
        else:
            return f"{self.name} движется со скоростью {self.speed}. Скорость в пределах нормы."


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            speed_now = self.speed - 40
            return(f"{self.name} движется со скоростью {self.speed}. Скорость превышена на {speed_now} км/час!")
        else:
            return f"{self.name} движется со скоростью {self.speed}. Скорость в пределах нормы."


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


tc = TownCar(70, "Blue", "Mercedes", False)
sc = SportCar(180, "Green", "Lamborghini", False)
wc = WorkCar(40, "Red", "Zil", False)
pc = PoliceCar(100, "Black", "Ford", True)
print(tc.show_speed())
print(sc.show_speed())
print(wc.show_speed())
print(pc.show_speed())
print(tc.go())
print(sc.turn_right())
print(wc.turn_left())
print(pc.stop())
