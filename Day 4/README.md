# Day 04 – Python Strings and String Methods

> Part of my 30-Day Python for Generative AI learning journey.

## 📚 Topics Covered

1. Introduction to Strings
2. String Indexing
3. String Slicing
4. String Length – `len()`
5. String Methods
6. String Membership – `in` and `not in`
7. String Concatenation
8. F-Strings
9. String Immutability
10. String Validation Methods
11. Practical GenAI Example

---

## 1. Introduction to Strings

A string is a sequence of characters enclosed within quotation marks.

Python supports single quotes, double quotes, and triple quotes.

### Examples

```python
name = "Indrajit"
language = 'Python'
message = """I am learning Python
for Generative AI."""
```

### Checking the Data Type

```python
message = "Hello Python"

print(type(message))
```

**Output:**

```text
<class 'str'>
```

---

## 2. String Indexing

Indexing allows us to access individual characters from a string.

Python indexing starts from `0`, not `1`.

### Example

```python
language = "Python"

print(language[0])
print(language[1])
print(language[2])
```

**Output:**

```text
P
y
t
```

### Understanding String Indexing

For the string `"Python"`:

| Character | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Positive Index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative Index | -6 | -5 | -4 | -3 | -2 | -1 |

### Negative Indexing

Negative indexing allows us to access characters from the end of a string.

```python
language = "Python"

print(language[-1])
print(language[-2])
```

**Output:**

```text
n
o
```

**Important:** The last character always has an index of `-1`.

---

## 3. String Slicing

Slicing allows us to extract a portion of a string.

### Syntax

```python
string[start:stop:step]
```

| Parameter | Meaning |
|---|---|
| `start` | Starting index |
| `stop` | Ending index (excluded) |
| `step` | Number of positions to move |

### Example 1: Basic Slicing

```python
language = "Python"

print(language[0:3])
```

**Output:**

```text
Pyt
```

The stop index `3` is excluded.

### Example 2: Omitting Start and Stop

```python
text = "Generative AI"

print(text[:5])
print(text[5:])
```

**Output:**

```text
Gener
ative AI
```

### Example 3: Using Step

```python
text = "Python"

print(text[::2])
```

**Output:**

```text
Pto
```

Here, Python takes every second character.

### Example 4: Reversing a String

```python
text = "PYTHON"

print(text[::-1])
```

**Output:**

```text
NOHTYP
```

### Understanding `[::-1]`

General slicing syntax:

```python
string[start:stop:step]
```

In `text[::-1]`:

- `start` is omitted.
- `stop` is omitted.
- `step = -1`.

A negative step tells Python to move backwards through the string.

Since start and stop are omitted, Python begins at the end and continues towards the beginning.

### Other Slicing Examples

```python
text = "PYTHON"

print(text[::1])    # PYTHON
print(text[::-1])   # NOHTYP
print(text[::2])    # PTO
print(text[::-2])   # NHY
```

**Important points:**

- `[::1]` moves forward.
- `[::-1]` moves backward.
- `[::2]` takes every second character moving forward.
- `[::-2]` takes every second character moving backward.

### Practical Example: Palindrome

A palindrome is a word that reads the same forwards and backwards.

```python
word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```

**Output:**

```text
Palindrome
```

---

## 4. String Length – `len()`

The `len()` function returns the total number of characters in a string.

Spaces are also counted.

### Example

```python
message = "Hello Python"

print(len(message))
```

**Output:**

```text
12
```

There are 11 letters and 1 space.

---

## 5. Important String Methods

Python provides built-in methods to manipulate strings.

### A. `upper()` – Convert to Uppercase

```python
name = "indrajit"

print(name.upper())
```

**Output:**

```text
INDRAJIT
```

### B. `lower()` – Convert to Lowercase

```python
name = "PYTHON"

print(name.lower())
```

**Output:**

```text
python
```

### C. `capitalize()` – Capitalize the First Character

```python
message = "hello python"

print(message.capitalize())
```

**Output:**

```text
Hello python
```

### D. `title()` – Capitalize Each Word

```python
message = "learning python for ai"

print(message.title())
```

**Output:**

```text
Learning Python For Ai
```

### E. `strip()` – Remove Spaces from Both Ends

```python
name = "   Indrajit   "

print(name.strip())
```

**Output:**

```text
Indrajit
```

Other related methods:

```python
name = "   Indrajit   "

print(name.lstrip())  # Removes left-side whitespace
print(name.rstrip())  # Removes right-side whitespace
```

### F. `replace()` – Replace Text

```python
message = "I love Java"

new_message = message.replace("Java", "Python")

print(new_message)
```

**Output:**

```text
I love Python
```

### G. `find()` – Find the Position of Text

```python
message = "I love Python"

print(message.find("Python"))
```

**Output:**

```text
7
```

If the text is not found, `find()` returns `-1`.

### H. `count()` – Count Occurrences

```python
message = "banana"

print(message.count("a"))
```

**Output:**

```text
3
```

### I. `startswith()` and `endswith()`

```python
email = "student@gmail.com"

print(email.startswith("student"))
print(email.endswith(".com"))
```

**Output:**

```text
True
True
```

These methods return Boolean values.

---

## 6. String Membership – `in` and `not in`

Membership operators check whether a particular character or substring exists inside a string.

### A. `in` Operator

The `in` operator returns `True` if the specified value exists.

```python
message = "I am learning Python"

print("Python" in message)
print("Java" in message)
```

**Output:**

```text
True
False
```

### B. `not in` Operator

The `not in` operator returns `True` if the specified value does not exist.

```python
message = "I am learning Python"

print("Python" not in message)
print("Java" not in message)
```

**Output:**

```text
False
True
```

### Practical Example

```python
message = "I love programming"

if "Java" not in message:
    print("Java is not mentioned.")
else:
    print("Java is mentioned.")
```

**Output:**

```text
Java is not mentioned.
```

### Difference Between `in` and `not in`

| Expression | Output |
|---|---|
| `"Python" in "I love Python"` | `True` |
| `"Java" in "I love Python"` | `False` |
| `"Python" not in "I love Python"` | `False` |
| `"Java" not in "I love Python"` | `True` |

**Remember:**

- `in` checks whether something exists.
- `not in` checks whether something does not exist.
- Both return Boolean values (`True` or `False`).

---

## 7. String Concatenation

Concatenation means joining two or more strings.

### Example

```python
first_name = "Indrajit"
last_name = "Barui"

full_name = first_name + " " + last_name

print(full_name)
```

**Output:**

```text
Indrajit Barui
```

### String Repetition

The multiplication operator can repeat a string.

```python
print("Python " * 3)
```

**Output:**

```text
Python Python Python
```

---

## 8. F-Strings – Formatted Strings

F-strings allow us to insert variables and expressions directly inside strings.

They make string formatting easier and more readable.

### Example 1: Using Variables

```python
name = "Indrajit"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

**Output:**

```text
My name is Indrajit and I am 21 years old.
```

### Example 2: Using Expressions

```python
number1 = 10
number2 = 20

print(f"Total: {number1 + number2}")
```

**Output:**

```text
Total: 30
```

### Example 3: Dynamic AI Prompt

```python
topic = "Machine Learning"
level = "Beginner"

prompt = f"Explain {topic} in simple language for a {level} student."

print(prompt)
```

**Output:**

```text
Explain Machine Learning in simple language for a Beginner student.
```

### Why Are F-Strings Important for Generative AI?

When developing AI applications, we frequently need to create prompts dynamically using user inputs.

F-strings make this process simple and readable.

---

## 9. String Immutability

This is one of the most important concepts in Python.

**Definition:** Strings are immutable. This means we cannot directly modify individual characters of an existing string.

### Example

```python
name = "Indrajit barui"

name.upper()

print(name)
```

**Output:**

```text
Indrajit barui
```

### Why Does This Happen?

The `upper()` method returns a new uppercase string. It does not modify the original string.

In the example above, we did not store the returned value.

### Correct Approach

```python
name = "Indrajit barui"

name = name.upper()

print(name)
```

**Output:**

```text
INDRAJIT BARUI
```

### Another Example Using `replace()`

```python
name = "Indrajit"

name = name.replace("Indrajit", "Rahul")

print(name)
```

**Output:**

```text
Rahul
```

### Important Points

1. Strings are immutable.
2. String methods that transform text return a new string.
3. The original string remains unchanged unless you reassign a value.
4. Slicing also creates a new string.

### Mutable vs Immutable

| Mutable | Immutable |
|---|---|
| Can be modified after creation | Cannot be modified directly |
| Lists | Strings |
| Dictionaries | Integers |
| Sets | Tuples |

We will study lists, tuples, dictionaries, and sets in upcoming lessons.

---

## 10. Useful String Validation Methods

Python provides methods to check the contents of a string.

These methods return `True` or `False`.

### A. `isalpha()`

Checks whether all characters are alphabetic letters.

```python
text = "Python"

print(text.isalpha())
```

**Output:** `True`

### B. `isdigit()`

Checks whether all characters are digits.

```python
text = "12345"

print(text.isdigit())
```

**Output:** `True`

### C. `isalnum()`

Checks whether all characters are letters or digits.

```python
text = "Python123"

print(text.isalnum())
```

**Output:** `True`

### D. `isspace()`

Checks whether all characters are whitespace.

```python
text = "   "

print(text.isspace())
```

**Output:** `True`

### Summary

| Method | Purpose |
|---|---|
| `isalpha()` | Checks alphabetic characters |
| `isdigit()` | Checks numeric digits |
| `isalnum()` | Checks letters and digits |
| `isspace()` | Checks whitespace |

---

## 11. Practical GenAI Example – User Prompt Cleaner

Imagine a user enters a prompt with unnecessary spaces.

We can clean and format the input using string methods.

```python
user_prompt = "   explain generative ai in simple words   "

cleaned_prompt = user_prompt.strip()

formatted_prompt = cleaned_prompt.capitalize()

print(formatted_prompt)
```

**Output:**

```text
Explain generative ai in simple words
```

This is a basic example of text preprocessing, which is useful when building AI applications.

---

# 💻 Day 04 – Practice Questions

Try to solve these questions independently. Do not simply copy solutions.

## Level 1 – Beginner

| No. | Problem | Concepts |
|---|---|---|
| 1 | Take a name as input and print it in uppercase and lowercase. | `upper()`, `lower()` |
| 2 | Take a sentence and count its characters. | `len()` |
| 3 | Reverse a string without using a loop. | Slicing |
| 4 | Count how many times the letter `a` appears in a string. | `count()` |
| 5 | Extract the first 5 characters of a string. | Slicing |
| 6 | Print the first and last character of a string. | Indexing |
| 7 | Remove unnecessary spaces from the beginning and end of a string. | `strip()` |

## Level 2 – Intermediate

| No. | Problem | Concepts |
|---|---|---|
| 8 | Check whether a word is a palindrome. | Slicing, conditions |
| 9 | Count the vowels in a sentence. | Loops, membership |
| 10 | Count the number of words in a sentence. | `split()`, `len()` |
| 11 | Replace every occurrence of `Java` with `Python`. | `replace()` |
| 12 | Check whether a sentence contains the word `Python`. | `in`, `not in` |
| 13 | Count uppercase and lowercase characters separately. | Loops, string methods |
| 14 | Find the frequency of every character in a string. | Loops, dictionaries |

## Level 3 – Advanced

| No. | Problem | Concepts |
|---|---|---|
| 15 | Remove all spaces from a string. | `replace()` |
| 16 | Check whether two words are anagrams. | Sorting, strings |
| 17 | Find the longest word in a sentence. | `split()`, loops |
| 18 | Remove duplicate characters while preserving order. | Loops, conditions |
| 19 | Check whether an email contains `@` and ends with `.com`. | `in`, `endswith()` |
| 20 | Build an AI prompt formatter using user input and f-strings. | `input()`, f-strings |

---

## 🎯 Day 04 – Interview Questions

1. What is a string in Python?
2. What is the difference between indexing and slicing?
3. What is negative indexing?
4. What does `len()` do?
5. What is the difference between `find()` and `count()`?
6. What are immutable data types?
7. Why are f-strings useful?
8. What is the difference between `strip()` and `replace()`?
9. What is the difference between `in` and `not in`?
10. Why does `name.upper()` not modify the original string?

---

## 📁 Suggested GitHub Folder Structure

```text
Day-04/
│
├── README.md
│
├── string_basics.py
├── string_indexing.py
├── string_slicing.py
├── string_methods.py
├── string_operators.py
├── string_immutability.py
│
└── practice_questions/
    ├── question_01.py
    ├── question_02.py
    ├── question_03.py
    └── ...
```

---

## 📌 Day 04 – Key Takeaways

- Strings are sequences of characters.
- Python indexing starts at zero.
- Negative indexing starts from the end.
- Slicing extracts portions of strings.
- `[::-1]` reverses a string.
- String methods help manipulate and validate text.
- `in` and `not in` check membership.
- F-strings help create dynamic text.
- Strings are immutable.
- String processing is an important foundation for Generative AI applications.

**Day 04 Status:** In Progress

**Next Topic:** Day 05 – Python Lists and Tuples.

---

*Consistency matters more than speed. Keep practising, experiment with code, and commit your daily progress to GitHub.*