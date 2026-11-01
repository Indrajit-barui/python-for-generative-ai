#python all important method

# Python lists have 11 built-in methods:
# append()
# extend()
# insert()
# remove()
# pop()
# clear()
# index()
# count()
# sort()
# reverse()
# copy()


# 1. append() – Add an element at the end
# Adds one element to the end of a list.
"""
list=['python',"java","c"]
list.append("cpp")
print(list)
"""

# 2. extend() – Add multiple elements
# Adds elements from another iterable to the end of the list.

""" 
list=['python',"java","c"]
list.extend(["cpp","java"])
print(list)
"""

# 3. insert() – Add an element at a specific position
# Syntax:list.insert(index, element)
"""
language=['english',"ben"]
language.insert(2,"hindi")
language.insert(0,"sanskrit")
print(language)
"""


# 4. remove() – Remove an element by value
# Removes the first matching value from the list.
"""
list=[1,2,3,4,5,5]
list.remove(5)
print(list)
"""


# 5. pop() – Remove an element by index
# Removes an element and also returns the removed value.

"""
list=["hii","hello","welcome","thankyou"]
delele=list.pop(1)
print(delele)
print(list)
# If you don't provide an index, it removes the last element.
"""

# 6. clear() – Remove all elements
# Removes every element but keeps the list variable.

"""
list=[1,5,4,5,6]
list.clear()
print(list)
print(len(list))

"""


# 7. index() – Find the position of an element
# Returns the index of the first matching element.
"""
list=[45,5,68,9,8]
print(list.index(45))

"""

# 8. count() – Count occurrences
# Counts how many times a value appears in a list.
"""
list=[1,2,3,4,5,1,1,1,4]
print(list.count(1))
"""

# 9. sort() – Sort elements
# Sorts the original list in ascending order by default.
"""
numbers=[1,5,4,7,81,1,56,85]
numbers.sort()
print(numbers)

# decending order
numbers.sort(reverse=True)
print(numbers)

"""
#10. reverse() – Reverse the list
list=[1,2,3,4,5]
list.reverse()
print(list)