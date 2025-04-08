
#Assignment 1

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} to check if {self.model} is available")

    def take_photo(self):
        print(f"Taking a photo with {self.brand} ,{self.model} device")
class tablet(Smartphone):
    def __init__(self, brand, model, storage, screen_size):
        super().__init__(brand, model, storage)
        self.screen_size = screen_size

    def watch_video(self):
        print(f"Watching video on {self.brand} {self.model} with a {self.screen_size} inch screen")
    def make_call(self, number):
        print(f"Making a video call to {number} from {self.brand} {self.model} tablet")
class1 = Smartphone("Apple", "iPhone 14", "128GB")
class1.make_call("093664345")
class1.take_photo()
class2 = tablet("Samsung", "Galaxy Tab S8", "256GB", 12.4)
class2.make_call("093664345")

#Assignment 2
class Animal:
    def move(self):
        print("Moving to the river")
class Car:
    def move(self):
        print("Driving 🚗")
class Plane:
    def move(self):
        print("Flying ✈️")

for object in [Animal(), Car(), Plane()]:
    object.move()
    