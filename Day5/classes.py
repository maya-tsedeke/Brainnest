"""1.Create a Dog class with the following attributes: name, breed, and age. The class should also have the following methods: bark() and info()."""
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} barks!")

    def info(self):
        print(f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}")
my_dog = Dog("Max", "Golden Retriever", 3)
my_dog.bark()  # prints "Max barks!"
my_dog.info()  # prints "Name: Max\nBreed: Golden Retriever\nAge: 3"
"""In this implementation, the __init__() method is used to set the initial values of the name, breed, and age attributes. 
The bark() method simply prints out a message that the dog is barking. The info() method prints out the dog's name, breed, 
and age.You can create an instance of the Dog class like this:
my_dog = Dog("Max", "Golden Retriever", 3)
And then call the bark() and info() methods on that instance:
my_dog.bark()  # prints "Max barks!"
my_dog.info()  # prints "Name: Max\nBreed: Golden Retriever\nAge: 3"
"""

"""2. Create a BankAccount class with the following attributes: balance and account_number. 
The class should also have the following methods: deposit(amount), withdraw(amount), and info()."""
class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def info(self):
        print(f"Account Number: {self.account_number}\nBalance: {self.balance}")
#We can see output here
my_account = BankAccount("123456789")
my_account.deposit(1000)
my_account.withdraw(500)
my_account.info()
