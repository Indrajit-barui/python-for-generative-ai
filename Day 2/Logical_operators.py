# Logical operators combine multiple conditions.

# Python has three main logical operators:
# - and
# - or
# - not

#A. AND operator
#Returns True only when both conditions are true.
num=30

print(num>20 and  num<40 )#true 

# B. OR operator
# Returns True when at least one condition is true.
has_email = False
has_phone = True

print(has_email or has_phone)#true


# C. NOT operator
# Reverses a Boolean value.
is_learning = True

print(not is_learning)