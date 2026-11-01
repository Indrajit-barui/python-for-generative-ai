# Part 1: Python Lists
# 1. What is a list?

# A list is a collection that allows us to store multiple values in a single variable.

#list
"""
language=["python","java","Cpp","javascript"]
print(language)
"""

# 2. Lists can store different data types
# A Python list can contain different types of data.
"""
student=["Indrajit barui",21,5.7,"bca student"]
print(student)
"""
#nested list.
"""
list=["indrajit barui",[54,80,96]]
print(list)
"""

# 3. Accessing list elements (indexing)
# Just like strings, lists use indexing.
"""
print(list[1][-1])
"""

# 4. List slicing
# Slicing allows you to access multiple elements.

# Syntax:list_name[start:stop:step]

"""
List=[10,20,30,40,50,60]
print(List[::-1]) #reverse
print(List[:3])
print(List[0:])
"""

# 5. Modifying list elements
# One important property of lists is that they are mutable.

# Mutable means you can change the elements after creating the list.
"""
list=["cpp","java","python","javascript"]
list[1]="react"
print(list)
"""