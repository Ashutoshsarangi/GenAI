class Robot:
    population = 0  # Class variable static
    def __init__(self, name, year):
        # Constructor
        self.name = name
        self.year = year
        Robot.population += 1
    
    def __del__(self):
        print('This is used for garbase collection')

    def __str__(self): #magic Methods
        return f'Robot name: {self.name} from __str__' #this will override the default __str__ method
    
    def __add__(self, other): #magic Methods
        print(f'Robot name: {self.name} {other.name}from __add__') # this will override the default __add__ (+) method
        return self.name + other.name


robot = Robot("Robo", 2023)
print(robot.name)
print(getattr(robot, 'year', 'Year not found'))
print(robot.__dict__)

print(robot)  # This will call the __str__ method

robot1 = Robot("Robo1", 2023)
robot2 = Robot("Robo2", 2023)

print(robot1 + robot2)  # This will call the __add__ method




# Example:-

class Car:
   total_cars = 0
 
   def __init__(self, make, built_year=None):
       self.make = make
       self.built_year = built_year
       Car.total_cars += 1
 
my_car = Car('Audi', 2019)
your_car = Car('VW')
my_car.total_cars += 5
print(my_car.total_cars) # This will print 7
print(Car.total_cars) # This will print 2
#my_car.total_cars += 5 creates a new instance attribute total_cars for my_car
#  and does not affect the class attribute Car.total_cars.
