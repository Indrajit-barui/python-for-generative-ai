#  f-strings – Very important!
# An f-string lets you insert variables directly into a string.

name="indrajit barui"
age=21
print(f"hey my name is {name} and age -> {age}")


# You can also use expressions:
num1=20
num2=10
print(f"total {num1+num2}")

# 10. Useful string checks
text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())

"""
Method	             Meaning
isalpha()	Checks whether all characters are letters
isdigit()	Checks whether all characters are digits
isalnum()	Checks whether all characters are letters or digits
isspace()	Checks whether all characters are whitespace

These return True or False.
"""