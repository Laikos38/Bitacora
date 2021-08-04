from typing import List
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def fill_fuel_tank(self):
        ...


class ConventionalCar(Vehicle):
    def start(self):
        print("* Noisy *")

    def fill_fuel_tank(self):
        print("Filling with fuel...")


class ElectricCar(Vehicle):
    def start(self):
        print("* Quietly *")

    def fill_fuel_tank(self):
        print("Charging batteries...")


class Race:
    def __init__(self, vehicles: List[Vehicle]):
        self.vehicles = vehicles

    def start_race(self):
        [v.start() for v in self.vehicles]


v1, v2 = ConventionalCar(), ElectricCar()
race = Race(vehicles=[v1, v2])
race.start_race()