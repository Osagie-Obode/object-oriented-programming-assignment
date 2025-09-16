class Customer:
    def __init__(self, name):
        self.name = name

    def drink(self):
        print(f"{self.name} is having a drink.")

class Man(Customer):
    def drink(self):
        print(f"{self.name} drinks beer. 🍺")

class Woman(Customer):
    def drink(self):
        print(f"{self.name} drinks soda. 🥤")

class Child(Customer):
    def drink(self):
        print(f"{self.name} drinks juice. 🧃")

class Grandpa(Customer):
    def drink(self):
        print(f"{self.name} drinks water. 💧")

# Example usage
if __name__ == "__main__":
    customers = [
        Man("Victor"),
        Woman("Lola"),
        Child("Dave"),
        Grandpa("Papa Joe"),
        Customer("Everybody")
    ]

    for customer in customers:
        customer.drink()