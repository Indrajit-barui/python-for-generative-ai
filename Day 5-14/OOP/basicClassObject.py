
""" 
class Student:
    college="ABC college" #class variable
     
    def __init__(self):
        pass
    
    def __init__(self,name,age): #Instance Variables
        self.name=name
        self.age=age
        print("this is constructor")
    def study(self):
        print(f"{self.name} is studying..")    
    def display(self):
        print("student name: ",self.name)
        print("age: ",self.age)
    


stu1=Student("Indrajit barui",21)
print(stu1.name)

stu1.display()
""" 

# Bank Account
"""
class BankAccount:
    
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        print(f"deposit {amount}")
        
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
            print(f"withdraw {amount} roupe")
            
        else:
            print("Insufficient balance!")
            
    def totalBalance(self):
        print(f"current balance {self.balance}")
        
        
acc1=BankAccount("indrajit barui",1000)
acc1.withdraw(500)
acc1.totalBalance()

"""

# 1. Instance Methods
# An instance method is a function defined inside a class that works with an object's data.

# It takes self as its first parameter.

class Person:
    
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
        
    # Instance Methods
    def details(self):
        print(f"name->{self.name} and age:->{self.age} and height:-> {self.height}")

per1=Person("indrajit",21,5.7)
per1.details()
        