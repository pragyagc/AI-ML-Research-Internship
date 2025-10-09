class Person:
   #constructor initializer
  def __init__(self,name,age):
   self.name = name
   self.age=age
  def greet(self):
    print(f"hello,my name is {self.name} and i am {self.age} years old.")

#creating objects
p1=Person("pragya",21)

p1.greet()



class Dog:
  species="bulldog"

  def __init__(self,name):
   self.name=name

dog1=Dog("Buddy")
dog2=Dog("Rocky")

print(dog1.name, dog1.species)


#class and instance attributes
class Student:
    school_name = "ABC School"  # class attribute (shared)

    def __init__(self, name):
        self.name = name        # instance attribute (unique)

s1 = Student("Pragya")
s2 = Student("Sita")

print(s1.name)          
print(s2.name)         
print(s1.school_name)  



#methos in classes

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):  # instance method
        return self.number ** 2

    @classmethod
    def greet(cls):  # class method
        print("Hello from Calculator class!")

    @staticmethod
    def add(a, b):  # static method
        return a + b

c = Calculator(4)
print(c.square())           
Calculator.greet()          # class method call
print(Calculator.add(5, 3)) 




#encapsulation

class BankAccount:
   def __init_self(self,owner,balance):
      self.owner=owner
      self.__balance=balance  #private


   def deposit(self,amount):
    self.__balance += amount

    def show_balance(self):
      print(f"Balance: Rs. {self.__balance}")

acc = BankAccount("Pragya", 5000)
acc.deposit(1000)
acc.show_balance() 