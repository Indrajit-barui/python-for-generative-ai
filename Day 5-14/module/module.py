import calculator

result = calculator.mul(10, 20)

print(result)


import math

print(math.sqrt(64))
print(math.pow(2,4))
print(math.ceil(4.15))
print(math.floor(5.63))
print(math.factorial(4))


import datetime

today=datetime.date.today() #today's date.
print(today.year)
print(today.month)
print(today.day)
print()
print("current date and time.")

now=datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)

print()
# Create your own date — datetime()

my_date=datetime.datetime(2026, 12, 25)
print(my_date)
