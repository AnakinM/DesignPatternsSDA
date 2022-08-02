from abc import ABC, abstractmethod
from typing import Union


class Vehicle(ABC):

    @abstractmethod
    def get_brand(self) -> str:
        pass

    @abstractmethod
    def get_wheels_count(self) -> int:
        pass

    @abstractmethod
    def get_seats_count(self) -> int:
        pass

    @abstractmethod
    def get_vehicle_type(self) -> str:
        # air, land, water
        pass

    @abstractmethod
    def get_engine_type(self) -> str:
        # petrol, diesel, gas, electric, no engine
        pass


class Car(Vehicle):
    def __init__(self, brand: str, engine_type: str, wheels_count: int = 4,
                 seat_count: int = 5, vehicle_type: str = "land"):
        self._brand = brand
        self._engine_type = engine_type
        self._wheels_count = wheels_count
        self._seat_count = seat_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_seats_count(self) -> int:
        return self._seat_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def get_engine_type(self) -> str:
        return self._engine_type

    def __str__(self):
        return f"Car({self._brand}, {self._engine_type})"


class Bike(Vehicle):
    def __init__(self, brand: str, engine_type: str = "no engine", wheels_count: int = 2,
                 seat_count: int = 1, vehicle_type: str = "land"):
        self._brand = brand
        self._wheels_count = wheels_count
        self._seat_count = seat_count
        self._vehicle_type = vehicle_type
        self._engine_type = engine_type

    def get_brand(self) -> str:
        return self._brand

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_seats_count(self) -> int:
        return self._seat_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def get_engine_type(self) -> str:
        return self._engine_type


class Boat(Vehicle):
    def __init__(self, brand: str, engine_type: str = "petrol",
                 wheels_count: int = 0, seat_count: int = 2,
                 vehicle_type: str = "water"):
        self._brand = brand
        self._wheels_count = wheels_count
        self._seat_count = seat_count
        self._vehicle_type = vehicle_type
        self._engine_type = engine_type

    def get_brand(self) -> str:
        return self._brand

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_seats_count(self) -> int:
        return self._seat_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def get_engine_type(self) -> str:
        return self._engine_type


class Airplane(Vehicle):
    def __init__(self, brand: str, engine_type: str, wheels_count: int = 6,
                 seat_count: int = 300, vehicle_type: str = "air"):
        self._brand = brand
        self._engine_type = engine_type
        self._wheels_count = wheels_count
        self._seat_count = seat_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_seats_count(self) -> int:
        return self._seat_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def get_engine_type(self) -> str:
        return self._engine_type


class VehicleFactory(ABC):

    @abstractmethod
    def create(self) -> Vehicle:
        pass


class BMWCarCreator(VehicleFactory):
    def create(self) -> Car:
        return Car("BMW", "petrol")


class RometBikeCreator(VehicleFactory):
    def create(self) -> Bike:
        return Bike("Romet")


class AirbusAirplaneCreator(VehicleFactory):
    def create(self) -> Airplane:
        return Airplane("Airbus", "petrol")


class BoeschBoatCreator(VehicleFactory):
    def create(self) -> Boat:
        return Boat("Boesch")


if __name__ == '__main__':
    vehicle_type: str = input("Select vehicle type [bike, car, airplane, boat]: ")
    vehicle_factory: Union[VehicleFactory, None] = None
    if vehicle_type.lower() == 'bike':
        vehicle_factory = RometBikeCreator()
    elif vehicle_type.lower() == 'car':
        vehicle_factory = BMWCarCreator()
    elif vehicle_type.lower() == 'airplane':
        vehicle_factory = AirbusAirplaneCreator()
    elif vehicle_type.lower() == 'boat':
        vehicle_factory = BoeschBoatCreator()

    if vehicle_factory:
        vehicle: Vehicle = vehicle_factory.create()
        print(vehicle)
    else:
        print("Not implemented.")
