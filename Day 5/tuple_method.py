# 8. All important tuple methods
# Unlike lists, tuples have only two built-in methods.


"""
# A. count() – Count occurrences
# Counts how many times a particular value appears.

tuple=(1,1,1,2,1,1,2,3)
print(tuple.count(2))
"""

"""
# B. index() – Find the position
# Returns the index of the first matching element.
languages = ("Python", "Java", "C++", "Java")

result = languages.index("Java")

print(result)

"""
"""
# 9. Other operations you can perform on tuples
# Even though tuples are immutable, you can still perform many operations.

numbers=(4,1,2,4,8,9,7)
print(min(numbers))
print(max(numbers))
print(sorted(numbers))
"""

"""
# Tuple concatenation
tup1=(1,5,7,8,9)
tup2=(4,8,9,7)
result=tup1+tup2
print(result)
"""

"""
# 11. Tuple repetition
# You can repeat tuple elements using the * operator.

tup=(1,5)
res=tup*2
print(res)
"""
"""
# 12. Membership operators
# Just like lists, tuples support in and not in.

tuple=(1,7,8,9,10)
print(12 in tuple)
print(21 not in tuple)
"""

"""
# 13. Looping through a tuple
# You can use a for loop to access every element.

tuple=(14,57,89,4587)
for num in tuple:
    print(num)
    
# You can also use range():
for num in range(len(tuple)):
    print(tuple[num])
"""