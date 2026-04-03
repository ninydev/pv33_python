from wheel import Wheel
from engine import Engine
from car import Car
from truck import Truck
from bus import Bus

if __name__ == "__main__":
    # Демонстрация работы

    # 1. Создаем части для легкового авто
    car_engine = Engine(150, "Бензиновый")
    car_wheels = [Wheel("Michelin", 17) for _ in range(4)]
    my_car = Car("Toyota", "Camry", car_engine, car_wheels, "Седан")
    my_car.display_info()
    print()

    # 2. Создаем части для грузовика
    truck_engine = Engine(450, "Дизельный")
    truck_wheels = [Wheel("Continental", 22) for _ in range(6)]
    my_truck = Truck("Volvo", "FH16", truck_engine, truck_wheels, 25)
    my_truck.display_info()
    print()

    # 3. Создаем части для автобуса
    bus_engine = Engine(280, "Газовый")
    bus_wheels = [Wheel("Bridgestone", 20) for _ in range(4)]
    my_bus = Bus("Mercedes-Benz", "Conecto", bus_engine, bus_wheels, 100)
    my_bus.display_info()
