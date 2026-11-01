#problem 1:Count how many times the letter a appears in a string.
"""
string=input("Enter a string: ");
count=0
i=0
while i<len(string):
    if string[i]=='a':
        count+=1
    i+=1
print("total number of a present a in the string: ", count)
# using for loop

count1=0
for i in range(len(string)):
    if(string[i]=='b'):
        count1+=1

print("total number of b is present in the string: ",count1)
"""

#problem 2:Extract the first 5 characters of a string.
"""
string1=input("enter a string that length shoulb be more than 5: ");

newString=string1[:6]
print("first 5 characters: ",newString)"""


#problem 3:Check whether a word is a palindrome.
"""
string2=input("enter a string: ");

if(string2==string2[::-1]):
    print("string is palindrome")
else:
    print("string is not a palindrome")
    """
    
#problem 4:Count the vowels in a sentence.
"""
string3=input("enter a string: ")
vowel="aeiouAEIOU"
count=0
for char in string3:
    if char in vowel:
        count+=1
print("total number vowel is : ",count)

"""
#problem 5:Count the number of words in a sentence.
"""
string4=input("enter a string: ")

strList=string4.split()
print(len(strList))
"""

#problem 6:Replace every occurrence of Java with Python.
str="hey rightnow i am learnig java java"
print(str.replace("java","python"))
