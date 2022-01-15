print('\nhttps://pynative.com/python-object-oriented-programming-oop-exercise/\n')


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):

    def fare(self):
        return super().fare() * 1.1


school_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", school_bus.fare())
