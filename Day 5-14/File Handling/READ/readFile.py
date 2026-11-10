# file = open("notes.txt", "r")
""" 
data = file.read() # reads entire file

print(data)
"""
"""
print(file.readline()) # reads one line at a time
print(file.readline())
print(file.read())
print(file.read())  # The cursor automatically moves forward after reading.

"""
# tell() – Check cursor position

file = open("notes.txt", "r", encoding="utf-8")

print(file.tell())

data = file.read(6)
print(data)

print(file.tell())


# seek() – Move the cursor
# seek() allows you to move the cursor to a particular position.

#syntax ->   file.seek(position)


file.seek(0)
print(file.tell())
print(file.read())
file.close()