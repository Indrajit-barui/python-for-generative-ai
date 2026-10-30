# The for loop

# A for loop is used when you want to repeat something over a sequence or a known range of values.


# Syntax:
"""{
# for variable in sequence:
    # code to execute
    }"""
    
for i in range(5):
    print(i)
    
    
# Understanding range()
"""
    The range() function is very important when working with loops.
    There are three common ways to use it.
    
    A. range(stop)
    
    for i in range(5):
       print(i)
    
    Output: 0 1 2 3 4
    
    
    B. range(start, stop)
    
     for i in range(1, 6):
         print(i)
         
     Output: 1 2 3 4 5 so stop will not include
     
     C. range(start, stop, step)
     
     for i in range(1, 11, 2):
        print(i)
    
    Output:1 3 5 7 9
    
    
    You can also count backwards:
    for i in range(10, 0, -1):
       print(i)
       
    Output: 10 9 8 7 6 5 4 3 2 1
"""


# practical example

print("practical example: ")
# problem 1:multiplication table:

num=5

for i in range(1,11,1):
    print(num,"*" ,i ,"=",num*i)
   
# problem 2: Calculate the sum of numbers

sum=0

for i in range(1,6):
    sum+=i
    
print(sum)