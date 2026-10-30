age =int(input("enter your age: "))

if (age >= 18):
    print("You are eligible for vote")
else:
   print("You are not eligible for vote");
   
   
# if-elif-else statement
# What if you have multiple conditions?
# Use elif.

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
    


# D. Nested if statements
# A nested if means placing one if statement inside another.

num = 21
has_id = True

if num >= 18:
    if has_id:
        print("You can enter")
    else:
        print("ID required")
else:
    print("You are too young")
    
    
# project one odd or even number check

number=int(input("Enter a number: "))
if number%2==0:
    print(number,"is even number")
else:
    print(number,"is odd number")
    
    
# Problem 2. Positive, Negative or Zero

if number>0:
    print("number is positive")
elif number<0:
    print("number is negetive")
else:
    print("number is zero")
    

#Problem 3. Find the Greatest of Three Numbers

number1=int(input("Enter a number1: "))
number2=int(input("Enter a number2: "))
number3=int(input("Enter a number3: "))

if(number1>=number2 and number1>=number3):
    print(number1 ,"is largest number")
elif number2>number3 and number2>number1:
    print(number2,"is largest number");
else:
    print(number3 ,"is largest number")