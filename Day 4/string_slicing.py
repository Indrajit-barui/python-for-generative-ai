#  String slicing
# Slicing allows you to extract a portion of a string.


#syntax
# string[start:stop:step]  (Remember: the stop index is excluded.)

#Example

text1="python"
print(text1[0:len(text1):1])

# More examples:
text2 = "Generative AI"

print(text2[0:len(text2)])
print(text2[:5])  #--> (0-4)
print(text2[0:])  #-->(0-length of string)

print(text2[::-1]) #reverse string
print(text2[::2])
