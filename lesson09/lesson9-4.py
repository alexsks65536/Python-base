'''Lesson 9 - 4'''

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Новая машина: {self.name} (цвет {self.color}) машина полиции - {self. is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала.")

    def stop(self):
        print(f"{self.name}: Машина остановилась.")

    def turn(self, direction):
        print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}.")

    def show_speed(self):
        return f"{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"

class SportCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

class TownCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

class WorkCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

police_car = PoliceCar('"Полиция ГИБДД"', 'белый', 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Большегруз"', 'синий', 40)
work_car.go()
print(work_car.show_speed())
work_car.turn(1)
work_car.stop()
print()

sport_car = SportCar('"СпортКар"', 'красный', 120)
sport_car.go()
print(sport_car.show_speed())
sport_car.turn(1)
sport_car.stop()
print()

town_car = TownCar('"Городской"', 'жёлтый', 40)
town_car.go()
print(town_car.show_speed())
town_car.turn(0)
town_car.stop()
print()