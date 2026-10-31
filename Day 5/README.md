# Day 05 – Python Lists and Tuples

## 📌 Overview

In Python, **Lists and Tuples** are built-in data structures used to store multiple values in a single variable.

They can store different data types, including:
- Integers
- Floats
- Strings
- Booleans
- Other lists and tuples

The main difference is:

- **List:** Mutable (can be modified).
- **Tuple:** Immutable (cannot be directly modified).

---

# 1. Python Lists

## 1.1 What is a List?

A list is an ordered collection of elements. It allows duplicate values and supports different data types.

### Creating a List

```python
languages = ["Python", "Java", "JavaScript", "C++"]

print(languages)
print(type(languages))
```

**Output:**
```text
['Python', 'Java', 'JavaScript', 'C++']
<class 'list'>
```

### List with Different Data Types

```python
student = ["Indrajit", 21, 85.5, True]

print(student)
```

**Output:**
```text
['Indrajit', 21, 85.5, True]
```

### Empty List

```python
numbers = []

print(type(numbers))
```

**Output:**
```text
<class 'list'>
```

### Nested List

A list can contain another list.

```python
data = ["Python", [10, 20, 30], "Java"]

print(data)
```

---

## 1.2 Properties of Lists

| Property | Description |
|---|---|
| Ordered | Maintains insertion order |
| Mutable | Elements can be modified |
| Duplicates | Allows duplicate values |
| Multiple data types | Supports different data types |
| Indexed | Supports positive and negative indexing |
| Dynamic | Can grow or shrink in size |
| Nested | Can contain other lists |

---

## 1.3 List Indexing

Indexing allows us to access individual elements.

```python
languages = ["Python", "Java", "JavaScript", "C++"]
```

| Element | Positive Index | Negative Index |
|---|---:|---:|
| Python | 0 | -4 |
| Java | 1 | -3 |
| JavaScript | 2 | -2 |
| C++ | 3 | -1 |

### Example

```python
print(languages[0])
print(languages[2])
print(languages[-1])
```

**Output:**
```text
Python
JavaScript
C++
```

**Important:** Positive indexing starts from 0, while negative indexing starts from -1.

---

## 1.4 List Slicing

Slicing allows us to access multiple elements from a list.

### Syntax

```python
list_name[start:stop:step]
```

- `start`: Starting index (included).
- `stop`: Ending index (excluded).
- `step`: Number of positions to skip.

### Examples

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
print(numbers[::2])
```

**Output:**
```text
[20, 30, 40]
[10, 20, 30]
[30, 40, 50, 60]
[60, 50, 40, 30, 20, 10]
[10, 30, 50]
```

---

## 1.5 Modifying List Elements

Lists are mutable, meaning we can change their elements after creating them.

```python
languages = ["Python", "Java", "C++"]

languages[1] = "JavaScript"

print(languages)
```

**Output:**
```text
['Python', 'JavaScript', 'C++']
```

---

# 2. All Important List Methods

Python provides 11 built-in list methods.

## 2.1 append()

Adds one element at the end of a list.

```python
languages = ["Python", "Java"]

languages.append("JavaScript")

print(languages)
```

**Output:**
```text
['Python', 'Java', 'JavaScript']
```

**Important:** `append()` adds the supplied object as one element.

```python
numbers = [10, 20]

numbers.append([30, 40])

print(numbers)
```

**Output:**
```text
[10, 20, [30, 40]]
```

## 2.2 extend()

Adds elements from another iterable to the end of a list.

```python
numbers = [10, 20]

numbers.extend([30, 40, 50])

print(numbers)
```

**Output:**
```text
[10, 20, 30, 40, 50]
```

## Difference Between append() and extend()

```python
a = [10, 20]
a.append([30, 40])

b = [10, 20]
b.extend([30, 40])

print(a)
print(b)
```

**Output:**
```text
[10, 20, [30, 40]]
[10, 20, 30, 40]
```

| append() | extend() |
|---|---|
| Adds one object | Adds elements from an iterable |
| Can add a list as one nested element | Adds the iterable's elements individually |

## 2.3 insert()

Adds an element at a specific index.

**Syntax:**
```python
list.insert(index, element)
```

**Example:**
```python
languages = ["Python", "Java"]

languages.insert(1, "C++")

print(languages)
```

**Output:**
```text
['Python', 'C++', 'Java']
```

## 2.4 remove()

Removes the first matching element by value.

```python
languages = ["Python", "Java", "C++"]

languages.remove("Java")

print(languages)
```

**Output:**
```text
['Python', 'C++']
```

**Important:** If the value does not exist, Python raises a `ValueError`.

## 2.5 pop()

Removes an element by index and returns the removed value.

```python
numbers = [10, 20, 30, 40]

removed = numbers.pop(1)

print(removed)
print(numbers)
```

**Output:**
```text
20
[10, 30, 40]
```

Without an index, `pop()` removes the last element.

```python
numbers = [10, 20, 30]

numbers.pop()

print(numbers)
```

**Output:**
```text
[10, 20]
```

## Difference Between remove() and pop()

| remove() | pop() |
|---|---|
| Removes by value | Removes by index |
| Returns None | Returns removed element |
| `remove(20)` | `pop(1)` |

## 2.6 clear()

Removes all elements from a list.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

**Output:**
```text
[]
```

## 2.7 index()

Returns the index of the first matching element.

```python
languages = ["Python", "Java", "C++", "Java"]

print(languages.index("Java"))
```

**Output:**
```text
1
```

You can specify a starting position:

```python
languages = ["Python", "Java", "C++", "Java"]

print(languages.index("Java", 2))
```

**Output:**
```text
3
```

If the value is not found, Python raises `ValueError`.

## 2.8 count()

Counts how many times an element appears.

```python
numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))
```

**Output:**
```text
3
```

## 2.9 sort()

Sorts the original list in ascending order by default.

```python
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)
```

**Output:**
```text
[10, 20, 30, 40, 50]
```

### Descending Order

```python
numbers.sort(reverse=True)

print(numbers)
```

**Output:**
```text
[50, 40, 30, 20, 10]
```

### Sorting Strings

```python
names = ["Rahul", "Amit", "John"]

names.sort()

print(names)
```

**Output:**
```text
['Amit', 'John', 'Rahul']
```

**Important:**
- `sort()` modifies the original list.
- `sort()` returns `None`.
- It sorts strings lexicographically (by Unicode ordering), not necessarily by human-language dictionary rules.

## 2.10 reverse()

Reverses the current order of elements.

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

**Output:**
```text
[40, 30, 20, 10]
```

**Important:** `reverse()` does not sort the list. It simply reverses the current order.

## 2.11 copy()

Creates a shallow copy of a list.

```python
original = [10, 20, 30]

new_list = original.copy()

new_list.append(40)

print(original)
print(new_list)
```

**Output:**
```text
[10, 20, 30]
[10, 20, 30, 40]
```

### Difference Between Assignment and copy()

```python
original = [10, 20, 30]

new_list = original

new_list.append(40)

print(original)
print(new_list)
```

**Output:**
```text
[10, 20, 30, 40]
[10, 20, 30, 40]
```

Both variables refer to the same list.

Using `copy()` creates a separate outer list.

**Important:** `copy()` is a shallow copy. If a list contains nested mutable objects, those inner objects are still shared. Use `copy.deepcopy()` when a fully independent nested copy is required.

---

## 2.12 Quick Revision: All List Methods

| Method | Purpose |
|---|---|
| `append(x)` | Adds one element |
| `extend(iterable)` | Adds elements from an iterable |
| `insert(i, x)` | Inserts at a specific index |
| `remove(x)` | Removes first matching value |
| `pop(i)` | Removes and returns an element |
| `clear()` | Removes all elements |
| `index(x)` | Finds first matching index |
| `count(x)` | Counts occurrences |
| `sort()` | Sorts the original list |
| `reverse()` | Reverses the original list |
| `copy()` | Creates a shallow copy |

---

# 3. Useful Built-in Functions With Lists

These are Python built-in functions, not list methods.

```python
numbers = [10, 50, 20, 40, 30]

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))
```

**Output:**
```text
5
10
50
150
[10, 20, 30, 40, 50]
```

| Function | Purpose |
|---|---|
| `len()` | Returns number of elements |
| `min()` | Returns smallest element |
| `max()` | Returns largest element |
| `sum()` | Calculates the total |
| `sorted()` | Returns a new sorted list |

**Important difference:**

- `list.sort()` modifies the original list and returns `None`.
- `sorted(list)` returns a new sorted list and leaves the original unchanged.

---

# 4. Membership Operators

Use `in` and `not in` to check whether an element exists.

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("PHP" not in languages)
```

**Output:**
```text
True
True
```

---

# 5. Looping Through Lists

### Using a for loop

```python
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
```

**Output:**
```text
Python
Java
C++
```

### Using range() and len()

```python
languages = ["Python", "Java", "C++"]

for i in range(len(languages)):
    print(i, languages[i])
```

**Output:**
```text
0 Python
1 Java
2 C++
```

### Using enumerate()

`enumerate()` gives us both the index and the element.

```python
languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)
```

**Output:**
```text
0 Python
1 Java
2 C++
```

---

# 6. Python Tuples

## 6.1 What is a Tuple?

A tuple is an ordered collection used to store multiple values in a single variable.

Unlike lists, tuples are immutable.

### Creating a Tuple

```python
languages = ("Python", "Java", "JavaScript", "C++")

print(languages)
print(type(languages))
```

**Output:**
```text
('Python', 'Java', 'JavaScript', 'C++')
<class 'tuple'>
```

### Tuple With Different Data Types

```python
student = ("Indrajit", 21, "BCA", 85.5, True)

print(student)
```

### Empty Tuple

```python
empty_tuple = ()

print(type(empty_tuple))
```

### Single-Element Tuple

Incorrect:

```python
numbers = (10)

print(type(numbers))
```

Output:
```text
<class 'int'>
```

Correct:

```python
numbers = (10,)

print(type(numbers))
```

Output:
```text
<class 'tuple'>
```

**Remember:** The comma is what makes a one-element tuple.

---

## 6.2 Properties of Tuples

| Property | Description |
|---|---|
| Ordered | Maintains insertion order |
| Immutable | Cannot reassign existing elements |
| Duplicates | Allows duplicate values |
| Multiple data types | Supports different data types |
| Indexed | Supports positive and negative indexing |
| Nested | Can contain other tuples and lists |

---

## 6.3 Tuple Indexing

```python
languages = ("Python", "Java", "JavaScript", "C++")

print(languages[0])
print(languages[2])
print(languages[-1])
```

**Output:**
```text
Python
JavaScript
C++
```

| Element | Positive Index | Negative Index |
|---|---:|---:|
| Python | 0 | -4 |
| Java | 1 | -3 |
| JavaScript | 2 | -2 |
| C++ | 3 | -1 |

---

## 6.4 Tuple Slicing

Syntax:

```python
tuple_name[start:stop:step]
```

Example:

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
```

**Output:**
```text
(20, 30, 40)
(10, 20, 30)
(30, 40, 50, 60)
(60, 50, 40, 30, 20, 10)
```

Slicing creates a new tuple.

---

# 7. Tuple Immutability

Tuples are immutable, meaning we cannot directly add, remove, or reassign their elements.

### Example: Modifying an Element

```python
languages = ("Python", "Java", "C++")

languages[1] = "JavaScript"
```

**Output:**
```text
TypeError: 'tuple' object does not support item assignment
```

### Example: Adding Elements

```python
languages = ("Python", "Java")

languages.append("C++")
```

This causes an `AttributeError` because tuples do not have an `append()` method.

### Workaround: Convert Tuple Into List

```python
languages = ("Python", "Java", "C++")

temp = list(languages)

temp.append("PHP")

languages = tuple(temp)

print(languages)
```

**Output:**
```text
('Python', 'Java', 'C++', 'PHP')
```

This creates a new tuple and assigns it to the same variable.

---

# 8. All Built-in Tuple Methods

Tuples have only two built-in methods.

## 8.1 count()

Counts how many times an element appears.

```python
numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))
```

**Output:**
```text
3
```

## 8.2 index()

Returns the index of the first matching element.

```python
languages = ("Python", "Java", "C++", "Java")

print(languages.index("Java"))
```

**Output:**
```text
1
```

You can also provide a starting index.

```python
print(languages.index("Java", 2))
```

**Output:**
```text
3
```

### Tuple Methods Revision

| Method | Purpose |
|---|---|
| `count(x)` | Counts occurrences |
| `index(x)` | Finds first matching index |

---

# 9. Useful Built-in Functions With Tuples

```python
numbers = (10, 50, 20, 40, 30)

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))
```

**Output:**
```text
5
10
50
150
[10, 20, 30, 40, 50]
```

Remember: `sorted()` returns a list, even when the input is a tuple.

To convert the sorted result back into a tuple:

```python
numbers = (40, 10, 30, 20)

result = tuple(sorted(numbers))

print(result)
```

**Output:**
```text
(10, 20, 30, 40)
```

---

# 10. Tuple Concatenation

We can combine two tuples using `+`.

```python
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

result = tuple1 + tuple2

print(result)
```

**Output:**
```text
(10, 20, 30, 40, 50, 60)
```

This creates a new tuple.

---

# 11. Tuple Repetition

We can repeat tuple elements using `*`.

```python
numbers = (10, 20)

result = numbers * 3

print(result)
```

**Output:**
```text
(10, 20, 10, 20, 10, 20)
```

---

# 12. Tuple Packing and Unpacking

## 12.1 Tuple Packing

Putting multiple values together into one tuple is called packing.

```python
student = "Indrajit", 21, "BCA"

print(student)
```

**Output:**
```text
('Indrajit', 21, 'BCA')
```

## 12.2 Tuple Unpacking

Extracting tuple elements into separate variables is called unpacking.

```python
student = ("Indrajit", 21, "BCA")

name, age, course = student

print(name)
print(age)
print(course)
```

**Output:**
```text
Indrajit
21
BCA
```

The number of variables must match the number of elements unless extended unpacking is used.

## 12.3 Extended Unpacking Using *

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

**Output:**
```text
10
[20, 30, 40]
50
```

**Important:** The variable `middle` receives a list.

---

# 13. Nested Tuples

A tuple can contain another tuple.

```python
students = (
    ("Rahul", 85),
    ("Amit", 90),
    ("John", 78)
)

print(students[0])
print(students[1][0])
print(students[2][1])
```

**Output:**
```text
('Rahul', 85)
Amit
78
```

### Understanding Nested Indexing

`students[1][0]`

1. `students[1]` accesses `("Amit", 90)`.
2. `[0]` accesses `"Amit"` from that inner tuple.

---

# 14. Mutable Objects Inside Tuples

A tuple is immutable, but it can contain mutable objects such as lists.

```python
data = ("Python", [10, 20, 30])

data[1].append(40)

print(data)
```

**Output:**
```text
('Python', [10, 20, 30, 40])
```

Why does this work?

- The tuple's element references have not changed.
- The list stored inside the tuple has been modified.

However, this is not allowed:

```python
data[1] = [50, 60]
```

This attempts to replace a tuple element and raises `TypeError`.

**Key takeaway:** Tuple immutability does not make the objects stored inside it immutable.

---

# 15. Lists vs Tuples

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[]` | `()` |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Duplicates | Allowed | Allowed |
| Multiple data types | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| Methods | 11 | 2 |
| Add/remove elements | Yes | Not directly |
| Typical use | Changeable collections | Fixed collections |

### When Should You Use a List?

Use a list when:
- You need to add new elements.
- You need to remove elements.
- You need to update values.
- Your collection changes frequently.

Example:
```python
chat_history = ["Hello", "How are you?"]

chat_history.append("Explain Python")
```

### When Should You Use a Tuple?

Use a tuple when:
- You want a fixed collection of values.
- You want to represent a record or configuration.
- You need a hashable collection for a dictionary key (provided all its elements are hashable).

Example:
```python
model_config = ("Gemini", 0.7, 1000)
```

---

# 16. Real-World Examples for GenAI

## Example 1: Chat History Using a List

```python
chat_history = []

chat_history.append("Hello!")
chat_history.append("What is Python?")
chat_history.append("Explain Python lists.")

for message in chat_history:
    print(message)
```

**Output:**
```text
Hello!
What is Python?
Explain Python lists.
```

Why use a list?

Because new messages can be added as the conversation continues.

## Example 2: AI Model Configuration Using a Tuple

```python
model_config = ("Gemini", 0.7, 1000)

model_name, temperature, max_tokens = model_config

print(model_name)
print(temperature)
print(max_tokens)
```

**Output:**
```text
Gemini
0.7
1000
```

Why use a tuple?

It represents a fixed group of configuration values.

## Example 3: Coordinates Using a Tuple

```python
location = (22.5726, 88.3639)

latitude, longitude = location

print(latitude)
print(longitude)
```

## Example 4: Conversation Snapshot

```python
messages = ["Hello", "What is Python?", "Explain lists"]

conversation_snapshot = tuple(messages)

print(conversation_snapshot)
```

A tuple can represent a fixed snapshot of the messages at that point in time. Note that it is a shallow snapshot.

---

# 17. Common Beginner Mistakes

| Mistake | Correct understanding |
|---|---|
| Thinking `append()` adds multiple elements separately | Use `extend()` |
| Thinking `remove()` removes by index | It removes by value |
| Thinking `pop()` removes by value | It removes by index |
| Thinking `reverse()` sorts a list | It only reverses the current order |
| Thinking `sort()` returns a sorted list | It returns `None` |
| Writing `(10)` for a one-element tuple | Use `(10,)` |
| Trying to modify tuple elements | Tuples are immutable |
| Thinking `sorted(tuple)` returns a tuple | It returns a list |
| Using `new_list = original` for a copy | Both names refer to the same list |

---

# 18. Important Interview Questions

1. What is a list in Python?
2. What is a tuple in Python?
3. What is the difference between lists and tuples?
4. What does mutable mean?
5. What does immutable mean?
6. What is the difference between `append()` and `extend()`?
7. What is the difference between `remove()` and `pop()`?
8. What is the difference between `sort()` and `sorted()`?
9. What is the difference between `reverse()` and `sort()`?
10. What is a nested list?
11. What is a nested tuple?
12. Why do we need a comma in a single-element tuple?
13. What are tuple packing and unpacking?
14. Can a tuple contain a list?
15. Can we add two tuples?
16. What does `count()` do?
17. What does `index()` do?
18. What is the difference between assignment and `copy()`?
19. What is a shallow copy?
20. When should we use a list instead of a tuple?

---

# 19. Practice Exercises

## Beginner Level

1. Create a list containing five programming languages.
2. Print the first and last elements.
3. Use slicing to extract three elements.
4. Replace one element in a list.
5. Add an element using `append()`.
6. Add multiple elements using `extend()`.
7. Remove an element using `remove()`.
8. Create a tuple with five elements.
9. Create a single-element tuple.
10. Access tuple elements using negative indexing.

## Intermediate Level

11. Find the largest number without `max()`.
12. Find the smallest number without `min()`.
13. Calculate the sum of list elements using a loop.
14. Count even and odd numbers.
15. Remove duplicates while preserving order.
16. Sort a list in ascending and descending order.
17. Count occurrences of a particular element.
18. Unpack a tuple into separate variables.
19. Convert a tuple into a list and add an element.
20. Create a nested tuple and access its elements.

## Advanced Level

21. Separate even and odd numbers into two lists.
22. Find the second-largest distinct number.
23. Reverse a list without `reverse()` or slicing.
24. Merge two lists.
25. Find common elements between two lists.

## Real-World / GenAI Level

26. Create a student marks management program.
27. Build a shopping cart using a list.
28. Build a simple chat history manager.
29. Create an AI model configuration using a tuple.
30. Create a basic AI conversation system using a list and tuple.

---

# 20. Day 05 – Key Takeaways

- Lists and tuples are built-in Python data structures.
- Both can store multiple values and different data types.
- Lists are mutable.
- Tuples are immutable.
- Lists have 11 built-in methods.
- Tuples have 2 built-in methods.
- Lists support indexing, slicing, and iteration.
- Tuples support indexing, slicing, and iteration.
- Tuple packing and unpacking are useful concepts.
- Lists are useful for changing collections such as chat history.
- Tuples are useful for fixed records and configurations.

## My Learning Checklist

- [ ] Understand list creation and properties.
- [ ] Understand indexing and slicing.
- [ ] Practise all 11 list methods.
- [ ] Understand tuple creation and properties.
- [ ] Understand tuple immutability.
- [ ] Practise both tuple methods.
- [ ] Understand packing and unpacking.
- [ ] Understand nested tuples.
- [ ] Understand list vs tuple.
- [ ] Solve the 30 practice exercises.
- [ ] Answer the interview questions.

---

**Next Topic: Day 06 – Python Dictionaries and Sets**

Keep practising. Understanding these data structures will help you work with JSON, API responses, and GenAI applications in the future.

**Repository:** `python-for-generative-ai`  
**Folder:** `Day-05`  
**File:** `README.md`  
**Status:** Learning / Practice in Progress
