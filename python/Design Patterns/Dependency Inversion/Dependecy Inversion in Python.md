# Dependency Inversion in Python

> Dependency inversion design pattern help us to reduce coupling in our code.

To implement dependency inversion through abstract classes in python you have to use de abc module, where abc stands for Abstract  Base Class.

[Documentation.](https://docs.python.org/3/library/abc.html)

In this first example we can notice a tight dependency between the `Race` and `ConventionalCar` classes:

```python
from typing import List

class ConventionalCar:
    def start(self):
        print("* Noisy *")

    def fill_fuel_tank(self):
        print("Filling with fuel...")


class Race:
    def __init__(self, cars: List[ConventionalCar]):
        self.cars = cars

    def start_race(self):
        [c.start() for c in self.cars]


car1, car2 = ConventionalCar(), ConventionalCar()
race = Race(cars=[car1, car2])
race.start_race()
```

Depending in the situation, maybe we want to remove such dependency by implementing a abstract class  which is going to have the declarations of the methods that we need to implement in the concrete class:

```python
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


class Race:
    def __init__(self, vehicles: List[Vehicle]):
        self.vehicles = vehicles

    def start_race(self):
        [v.start() for v in self.vehicles]


v1, v2 = ConventionalCar(), ConventionalCar()
race = Race(vehicles=[v1, v2])
race.start_race()
```

Because we remove the dependency between `Race` and `ConventionalCar` classes, we can now attach others `Vehicle` types, for example:

```python
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
```



