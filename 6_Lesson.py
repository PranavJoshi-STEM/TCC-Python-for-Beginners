# 1. Functions and Optional Arguments

# Define a function with an optional argument
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Call the function with and without optional argument
greet("Alice")
greet("Bob", "Hi")

# 2. Classes

# Define a class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Create an instance of the class
my_dog = Dog("Buddy", "Labrador")

# Access instance attributes
print(my_dog.name)
print(my_dog.breed)

# 3. Scope and Global Keyword

# Define a variable in global scope
global_var = 10

# Access global variable within a function
def print_global():
    print(global_var)

print_global()

# 4. Lambda Functions

# Define a lambda function
double = lambda x: x * 2

# Call the lambda function
print(double(5))

# 5. Recursion

# Define a function using recursion to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Call the factorial function
print(factorial(5))

# 6. Inheritance and Decorators

# Define a base class
class Animal:
    def speak(self):
        pass

# Define a subclass inheriting from the base class
class Dog(Animal):
    def speak(self):
        return "Woof!"

# 7. DRY: Don't Repeat Yourself

# Define a function to avoid repetition
def add(a, b):
    return a + b

# Call the function
result = add(3, 5)
print(result)

# 8. Return Keyword

# Define a function with return statement
def add_and_multiply(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

# Call the function and unpack the returned values
sum_result, product_result = add_and_multiply(3, 4)
print("Sum:", sum_result)
print("Product:", product_result)

# ------------------------
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = 0  # Protected variable

    def drive(self, miles):
        self._mileage += miles


class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color
        self.mileage = 0  # Public variable

    def display_info(self):
        return f"{super().display_info()}, Color: {self.color}"

    def drive(self, miles):
        self.mileage += miles
    
    def play_music():
        print('Playing Heat Waves by Glass Animals...')


# Create instances of Vehicle and Car
vehicle = Vehicle("Toyota", "Camry", 2020)
car = Car("Honda", "Accord", 2018, "Red")

# Drive the vehicle and the car
vehicle.drive(100)
car.drive(150)

# Display updated mileage
print("Vehicle Mileage:", vehicle._mileage)
print("Car Mileage:", car.mileage)
