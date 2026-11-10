# list unpacking (*)

""" 
numbers=[10,20,30,40]

def addition(*num):
    res=0
    for val in num:
       res=res+val
    return res    


print(addition(*numbers))

"""

"""


#dictionary unpacking (**)

details={
    "name":"Indrajit barui",
    "age":21,
    "course":"BCA"
}

def printDetails(**details):
    for val in details.values():
        print(val)
        
printDetails(**details)

"""

#First-class functions

# 1. store function in a variable:

""" 
def greeting(name):
    print(f"hello {name}")
    
my_func=greeting

my_func("indrajit barui")
"""

#2. pass a function as an argument  ->callback function


""" 
def greeting(name):
    print("hello",name)
    
def process(callback):
    callback("indrajit")


process(greeting)

"""

#3 return function from another function:

"""
def outer():
    def inner():
        print("hello i am inner function")
        
    
    return inner

result=outer()

result()

"""


# 4.store function inside a list
""" 
def add(a,b):
    return a+b

def mul(a,b):
    return a*b

operations=[add,mul]

print(operations[0](10,20))
print(operations[1](5,20))

calculator={
    
    "+":add,
    "*":mul
    
}

result=calculator["*"](10,20)

print(result)

"""


# A Higher-Order Function (HOF) is a function that does at least one of these two things:

# Accepts another function as an argument.
# Returns another function.
    
    
#Lambda function
""" 
addition=lambda a,b:a+b

print(addition(10,20)) 

#syntax
# lambda:argument: expression

square=lambda x:x*x

print(square(5))

#odd or enen check

check=lambda num:"Even" if num%2==0 else "odd"

print(check(10))
  
  """
# Nested functions
"""" 
def outer():
    print("I am a outer function")
    def inner():
        print("I am inner function")
        
    inner()
    
outer()

"""
#output->
# I am a outer function
# I am inner function


#closure

""" 

def outer():
    name="Indrajit barui"
    
    def inner():
        print(name)
        
    return inner

result=outer()

result()


def backAccount():
    balance=500
    
    def deposit(amount):
        nonlocal balance
        balance+=amount
        return balance
    
    def Withdrawal(amount):
        nonlocal balance
        if(amount<=balance):
            balance-=amount
            print(f"Successfully withdrew {amount}. Remaining balance: {balance}")
            
    def totalBalance():
        nonlocal balance
        return balance
    
    
    return deposit,Withdrawal,totalBalance

account=backAccount()

deposit,Withdrawal,totalBalance=account

print(deposit(500))
Withdrawal(100)
print(totalBalance())


"""

"""
# map()

number=[1,2,5,4,10,20]

result=map(lambda num:num+1,number)

print(list(result))



# filter

filterRes=filter(lambda num:num%2==0,number)

print(list(filterRes))


#  reduce

from functools import reduce


sumRes=reduce(lambda x,y:x+y,number)


print(sumRes)

"""

#async await

import time

def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 completed")
    
def task2():
    
    print("Task 2 started")
    print("Task 2 completed")
    
    
task1()
task2()