# 1. What is a tuple?
# A tuple is a built-in Python data structure used to store multiple values in a single variable. but it's immutable
"""
lan=("python","java","cpp")
print(type(lan))
print(lan)
"""

#tuple with different data type
"""
tuple=("string",21,2.5)
print(tuple)
"""

#B. Without parentheses
"""
tuple=1,2,3,4
print(type(tuple))
print(tuple)
"""

# C. Creating an empty tuple
"""
empty_tuple=()
print(type(empty_tuple))
"""

# . Creating a tuple with one element
# This is a very important concept!
"""
OneElement=(21,) #OneElement=(21) this is incorrect 
print(OneElement)
print(type(OneElement))

# Why?
# Because the comma creates the one-element tuple. Parentheses alone don't.
"""


"""
# 4. Accessing tuple elements (indexing)
# Tuples support indexing just like lists and strings.


tuple=(4,5,7,8,9,41)
print(tuple[0])
print(tuple[-1])
"""
