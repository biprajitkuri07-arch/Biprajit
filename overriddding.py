# Defining the parent class (optional, for structure)
class Vehicle:
    def move(self):
        pass

# Defining the Car class
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

# Defining the Cycle class
class Cycle(Vehicle):
    def move(self):
        print("The cycle is being pedaled.")

# Instantiating the objects as shown in your notes
c = Car()
c1 = Cycle()

# Calling the methods
c.move()   # Output: The car is driving on the road.
c1.move()  # Output: The cycle is being pedaled.