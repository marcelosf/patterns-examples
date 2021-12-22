from __future__ import annotations
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> str:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass


class Car(Vehicle):
    def start_engine(self) -> str:
        return 'Car engine started'

    def get_type(self) -> str:
        return 'land vehicle'


class Boat(Vehicle):
    def start_engine(self) -> str:
        return 'Boat engine started'

    def get_type(self) -> str:
        return 'marine vehicle'


class Truck(Vehicle):
    def start_engine(self) -> str:
        return 'Truck engine started'

    def get_type(self) -> str:
        return 'land vehicle'


class AbstractFactory(ABC):
    def create_vehicle(self) -> Vehicle:
        pass


class CarFactory(AbstractFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()


class BoatFactory(AbstractFactory):
    def create_vehicle(self) -> Vehicle:
        return Boat()


class TruckFactory(AbstractFactory):
    def create_vehicle(self) -> Vehicle:
        return Truck()


def start_vehicle(factory: AbstractFactory) -> None:
    vehicle = factory.create_vehicle()

    print(vehicle.start_engine())
    print(vehicle.get_type())
    print(10 * '=')


if __name__ == '__main__':
    start_vehicle(CarFactory())
    start_vehicle(BoatFactory())
    start_vehicle(TruckFactory())
