# 1. What is a string?
# A string is a sequence of characters enclosed inside quotation marks.
# Strings are immutable.   =>In Python, strings are immutable. This means you cannot modify the original string directly after creating it.

# Example


text1='hey how are you'
text2= """Hello
I am learning Python
for Generative AI"""


print(text1);
print(text2)


# String indexing
# Every character in a string has an index (position).

name = "Python"

print(name[0])
print(name[1])
print(name[2])

"""
Character	    P	y	t	h	o	n
Positive index	0	1	2	3	4	5
Negative index	-6	-5	-4	-3	-2	-1

"""

print(name[-1])#n