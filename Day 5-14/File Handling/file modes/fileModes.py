
# Important: r+
# - The file must already exist.
# - It does not delete existing content.
# - The cursor initially starts at position 0

""" 

file=open("notes.txt","r+")
print(file.read())
file.write("Hello Java")

"""

# Important: w+
# - Creates a file if it doesn't exist.
# - If the file already exists, its old content is deleted immediately.
# - The cursor initially starts at position 0.

""" 
f=open("notes.txt","w+")
print(f.read())
f.writelines("hey this is me indrajit\nwhat is your name?")
f.seek(0)
print(f.read())

"""

# Important:
# - Creates a file if it doesn't exist.
# - Preserves existing content.
# - Writing always happens at the end of the file.
# - For reading from the beginning, use seek(0).


# f=open ("notes.txt","a+")
# f.seek(0)
# print(f.read())
# f.writelines("hey i am akash and how are you today")
# print(f.tell())

with open("notes.txt","a+") as f:
    f.seek(0)
    
    print(f.read())
    