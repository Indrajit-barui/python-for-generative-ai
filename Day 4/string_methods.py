#  Important string methods
# Python provides built-in methods to manipulate strings.


# Strings are immutable.   =>In Python, strings are immutable. This means you cannot modify the original string directly after creating it.

# A. upper() – Convert to uppercase
name="Indrajit barui"
print(name.upper())

# B. lower() – Convert to lowercase
print(name.lower())

#C. capitalize() – Capitalize the first character
print(name.capitalize())

# D. title() – Capitalize each word
print(name.title())

# E. strip() – Remove spaces from both ends
text1="    hey how are you?     "
print(text1.strip())

# other releted method

name = "   Indrajit   "

print(text1.lstrip())  # Remove left-side spaces
print(text1.rstrip())  # Remove right-side spaces

# name = "   Indrajit   "print(name.lstrip())  # Remove left-side spacesprint(name.rstrip())  # Remove right-side spaces



# F. replace() – Replace text

message = "I love Java Java"

new_message = message.replace("Java", "Python")
print(new_message)


# G. find() – Find the position of text
# If the text is not found, find() returns -1.
text2="Indrajit"
print(text2.find("n"))


# I. startswith() and endswith()
# Both return Boolean values (True or False).
email = "student@gmail.com"

print(email.startswith("student"))
print(email.endswith(".com"))


# String membership – in and not in
# You can check whether a particular word or character exists inside a string.

# in → Checks whether something exists.
# not in → Checks whether something does not exist.

message2 = "I am learning Python"

print("I" in message2) #true
print("java" in message2) #false
print("Python" not in message2) #false
print("java" not in message2) #true


# String concatenation
# Concatenation means joining two or more strings.

first_name = "Indrajit"
last_name = "Barui"

full_name = first_name + " " + last_name

print(full_name)
#you can also repeat the string
print("Python " * 3)