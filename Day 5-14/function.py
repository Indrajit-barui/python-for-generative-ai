# function

# def greet(name):
#     print("welcome ",name)
    
# greet("Indrajit barui")
# greet("Deep")
"""
def sum(num1,num2):
    return num1+num2

print(sum(10,20))

""" 
"""
def student_details(name,age,roll):
    print(f"name {name}")
    print(f"age {age}")
    print(f"roll: {roll}")
    
student_details("Indrajit barui",21,10)


#2. Keyword arguments
# Instead of relying on position, you can specify the parameter name.

student_details(age=21,name="deep",roll=1)

"""
#3. Default arguments
# Sometimes we want to provide a default value.

"""
def greet(name="alex"):
    print("hello ",name)


greet("indrajit barui")
greet()
"""

#Part 6 – Intermediate Python: *args and **kwargs

# 1. What is *args?
# Suppose we want to create a function that adds multiple numbers.

# We don't know how many numbers the user will provide.

def mul(*args):
    res=1
    for num in args:
        res=res*num
    return res
print(mul(1,2,3,4))


# Remember: args is just a conventional name. The * is what matters.

# 2. What is **kwargs?
# *args collects extra positional arguments into a tuple.

# **kwargs collects extra keyword arguments into a dictionary.
""" 
def std_details(**kwargs):
    print(kwargs)
    

std_details(
    name="indrajit",
    age=21,
    roll=10
)

"""

# A function can call another function
"""
def addition(num1,num2):
    return num2+num1

def multiplication(num1,num2):
    return num1*num2

def calculate(num1,num2):
    add=addition(num1,num2)
    mul=multiplication(num1,num2)
    
    return add,mul


print(calculate(10,20))
""" 

#callback function

def greeting(name):
    print(name)
    
def process_user(callback):
    print("hello...")
    callback("Indrajit barui")
    
process_user(greeting)
