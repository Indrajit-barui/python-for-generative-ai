# Day 06 – Dictionaries and Sets in Python

## 📌 Overview

In this lesson, we learn about two important Python data structures:

1. **Dictionary (`dict`)** – Stores data in key-value pairs.
2. **Set (`set`)** – Stores unique elements without duplicates.

Both are useful when working with APIs, JSON data, user information, chat history, and Generative AI applications.

---

# 1. Dictionaries in Python

## What is a Dictionary?

A dictionary is a built-in Python data structure that stores information in **key-value pairs**.

### Example

```python
student = {
    "name": "Alex",
    "age": 21,
    "course": "BCA"
}

print(student)
```

Output:

```text
{'name': 'Alex', 'age': 21, 'course': 'BCA'}
```

### Important Characteristics

- Stores data in key-value pairs.
- Ordered (preserves insertion order).
- Mutable (can be modified).
- Keys must be unique.
- Values can be duplicated.
- Keys must be hashable (e.g. strings, numbers, or suitable tuples).
- Values can contain different data types.
- Supports nested dictionaries.

## 2. Creating Dictionaries

```python
# Normal dictionary
student = {
    "name": "Alex",
    "age": 21
}

# Empty dictionary
data = {}

# Using dict()
person = dict(name="John", age=25)

print(student)
print(data)
print(person)
```

## 3. Accessing Dictionary Values

### Using square brackets

```python
student = {
    "name": "Alex",
    "age": 21
}

print(student["name"])
print(student["age"])
```

Output:

```text
Alex
21
```

**Important:** Accessing a missing key using square brackets raises a `KeyError`.

### Using get()

```python
print(student.get("name"))
print(student.get("city"))
print(student.get("city", "Not Available"))
```

Output:

```text
Alex
None
Not Available
```

**Difference:**

| `student["city"]` | `student.get("city")` |
|---|---|
| Raises KeyError if missing | Returns None by default |
| Direct access | Safer access |
| Can be used to access existing keys | Can provide a default value |

## 4. Adding and Updating Values

```python
student = {
    "name": "Alex",
    "age": 21
}

# Add a new key
student["city"] = "Kolkata"

# Update an existing key
student["age"] = 22

print(student)
```

Output:

```text
{'name': 'Alex', 'age': 22, 'city': 'Kolkata'}
```

## 5. Removing Dictionary Elements

### pop()

Removes a specified key and returns its value.

```python
student = {"name": "Alex", "age": 21}

removed_value = student.pop("age")

print(removed_value)
print(student)
```

### popitem()

Removes and returns the last inserted key-value pair.

```python
student = {"name": "Alex", "age": 21}

student.popitem()

print(student)
```

### del

Deletes a specified key.

```python
del student["name"]
```

### clear()

Removes all elements.

```python
student.clear()
print(student)
```

## 6. Important Dictionary Methods

| Method | Description |
|---|---|
| `get(key)` | Returns the value of a key |
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `update()` | Adds or updates multiple pairs |
| `pop(key)` | Removes a specified key |
| `popitem()` | Removes the last inserted pair |
| `clear()` | Removes all elements |
| `copy()` | Creates a shallow copy |
| `setdefault()` | Returns a value; inserts a default if the key is missing |

### keys()

```python
student = {"name": "Alex", "age": 21}

print(student.keys())
```

### values()

```python
print(student.values())
```

### items()

```python
print(student.items())
```

### update()

```python
student.update({
    "age": 22,
    "city": "Kolkata"
})

print(student)
```

### setdefault()

```python
student = {"name": "Alex"}

student.setdefault("age", 21)
student.setdefault("name", "John")

print(student)
```

Output:

```text
{'name': 'Alex', 'age': 21}
```

`setdefault()` does not overwrite an existing key.

### copy()

```python
original = {"name": "Alex", "age": 21}

new_student = original.copy()

new_student["age"] = 22

print(original)
print(new_student)
```

**Note:** `copy()` creates a shallow copy. Nested mutable objects can still be shared between the original and copied dictionaries.

## 7. Looping Through Dictionaries

### Loop through keys

```python
student = {
    "name": "Alex",
    "age": 21,
    "course": "BCA"
}

for key in student:
    print(key)
```

### Loop through values

```python
for value in student.values():
    print(value)
```

### Loop through keys and values

```python
for key, value in student.items():
    print(key, ":", value)
```

Output:

```text
name : Alex
age : 21
course : BCA
```

**Important:** `items()` is especially useful when you need both the key and its value.

## 8. Nested Dictionaries

A dictionary can contain another dictionary.

```python
students = {
    "student1": {
        "name": "Alex",
        "age": 21
    },

    "student2": {
        "name": "John",
        "age": 22
    }
}

print(students["student1"]["name"])
print(students["student2"]["age"])
```

Output:

```text
Alex
22
```

## 9. Dictionary Comprehension

A shorter way to create dictionaries.

```python
numbers = [1, 2, 3, 4, 5]

squares = {
    num: num ** 2
    for num in numbers
}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

With a condition:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(even_squares)
```

---

# 10. Sets in Python

## What is a Set?

A set is a built-in Python data structure that stores **unique elements**.

### Example

```python
numbers = {1, 2, 3, 4, 5}

print(numbers)
```

### Important Characteristics

- Stores unique elements.
- Automatically removes duplicates.
- Unordered (no guaranteed positional order).
- Mutable.
- Does not support indexing or slicing.
- Elements must be hashable.
- Supports mathematical set operations.

## 11. Creating Sets

```python
# Normal set
numbers = {1, 2, 3, 4}

# Empty set
empty_set = set()

# Set from a list
values = [1, 2, 2, 3, 3, 4]

unique_values = set(values)

print(unique_values)
```

**Important:**

```python
empty_dict = {}
empty_set = set()
```

`{}` creates an empty dictionary, not an empty set.

## 12. Adding Elements

### add()

Adds one element.

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

### update()

Adds multiple elements from an iterable.

```python
numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)
```

## 13. Removing Elements

### remove()

Removes an element. Raises `KeyError` if it does not exist.

```python
numbers = {1, 2, 3}

numbers.remove(2)

print(numbers)
```

### discard()

Removes an element without raising an error if it is missing.

```python
numbers.discard(5)
```

### pop()

Removes and returns an arbitrary element.

```python
numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)
print(numbers)
```

### clear()

Removes all elements.

```python
numbers.clear()
```

## 14. Important Set Methods

| Method | Description |
|---|---|
| `add()` | Adds one element |
| `update()` | Adds multiple elements |
| `remove()` | Removes an element; raises an error if missing |
| `discard()` | Removes an element without an error if missing |
| `pop()` | Removes an arbitrary element |
| `clear()` | Removes all elements |
| `copy()` | Creates a shallow copy |
| `union()` | Combines elements from sets |
| `intersection()` | Returns common elements |
| `difference()` | Returns elements present in the first set only |
| `symmetric_difference()` | Returns elements present in either set, but not both |
| `issubset()` | Checks whether one set is a subset of another |
| `issuperset()` | Checks whether one set contains another |
| `isdisjoint()` | Checks whether two sets have no common elements |
| `intersection_update()` | Updates the set with common elements |
| `difference_update()` | Removes elements found in another set |
| `symmetric_difference_update()` | Updates the set with non-common elements |

---

# 15. Mathematical Set Operations

Consider these two sets:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### Union

Combines all unique elements from both sets.

```python
print(A.union(B))
print(A | B)
```

Output:

```text
{1, 2, 3, 4, 5, 6}
```

### Intersection

Returns common elements.

```python
print(A.intersection(B))
print(A & B)
```

Output:

```text
{3, 4}
```

### Difference

Returns elements present in A but not in B.

```python
print(A.difference(B))
print(A - B)
```

Output:

```text
{1, 2}
```

Reverse direction:

```python
print(B - A)
```

Output:

```text
{5, 6}
```

### Symmetric Difference

Returns elements that are not common to both sets.

```python
print(A.symmetric_difference(B))
print(A ^ B)
```

Output:

```text
{1, 2, 5, 6}
```

## 16. Checking Set Relationships

```python
A = {1, 2}
B = {1, 2, 3, 4}
C = {7, 8}
```

### issubset()

```python
print(A.issubset(B))
```

Output:

```text
True
```

### issuperset()

```python
print(B.issuperset(A))
```

Output:

```text
True
```

### isdisjoint()

```python
print(A.isdisjoint(C))
```

Output:

```text
True
```

## 17. Set Comprehension

A shorter way to create a set.

```python
numbers = [1, 2, 3, 4, 5]

squares = {
    num ** 2
    for num in numbers
}

print(squares)
```

Output:

```text
{1, 4, 9, 16, 25}
```

With a condition:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    num
    for num in numbers
    if num % 2 == 0
}

print(even_numbers)
```

---

# 18. Dictionary vs Set

| Feature | Dictionary | Set |
|---|---|---|
| Structure | Key-value pairs | Unique elements |
| Syntax | `{key: value}` | `{value1, value2}` |
| Ordered | Yes | No guaranteed order |
| Mutable | Yes | Yes |
| Duplicates | Keys cannot repeat | Elements cannot repeat |
| Indexing | Access through keys | No indexing |
| Main purpose | Store related information | Store unique values |

# 19. List vs Tuple vs Dictionary vs Set

| Feature | List | Tuple | Dictionary | Set |
|---|---|---|---|---|
| Syntax | `[]` | `()` | `{key: value}` | `{}` |
| Ordered | Yes | Yes | Yes | No |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | Keys: No | No |
| Indexing | Yes | Yes | By key | No |
| Main use | Collection of items | Fixed collection | Key-value data | Unique items |

**Remember:**

- List → Ordered and changeable collection.
- Tuple → Ordered and immutable collection.
- Dictionary → Key-value storage.
- Set → Unique elements.

---

# 20. Practical Examples for Generative AI

Understanding dictionaries and sets is important when working with APIs, JSON responses, LLMs, and chat history.

## Example 1: API Response

API responses commonly contain JSON objects that map naturally to Python dictionaries.

```python
api_response = {
    "status": "success",
    "model": "gemini",
    "tokens": 150,
    "response": "Hello! How can I help you?"
}

print(api_response["model"])
print(api_response.get("tokens"))
```

## Example 2: Chat Message

```python
message = {
    "role": "user",
    "content": "Explain Generative AI"
}

print(message["role"])
print(message["content"])
```

## Example 3: Chat History

```python
chat_history = [
    {
        "role": "user",
        "content": "What is Python?"
    },

    {
        "role": "assistant",
        "content": "Python is a programming language."
    }
]

for message in chat_history:
    print(message["role"], ":", message["content"])
```

## Example 4: Unique Words

```python
message = "AI is amazing and AI is useful"

words = message.split()

unique_words = set(words)

print(unique_words)
```

A set removes duplicate words. Remember that this simple example is case-sensitive.

## Example 5: Model Configuration

```python
model_config = {
    "model": "gemini",
    "temperature": 0.7,
    "max_tokens": 1000,
    "streaming": True
}

print(model_config)
```

---

# 21. Common Mistakes to Avoid

1. Using `{}` when you want an empty set. Use `set()`.
2. Accessing a missing dictionary key using square brackets without checking.
3. Thinking dictionary keys can be duplicated.
4. Thinking sets preserve insertion order.
5. Trying to access set elements using indexing.
6. Using `remove()` when an element might not exist; consider `discard()`.
7. Confusing `append()` with `update()` or `add()`.
8. Assuming `copy()` performs a deep copy.
9. Trying to use a list or dictionary as a set element.
10. Forgetting that set output order is not guaranteed.

---

# 22. Practice Questions

## Beginner Level

1. Create a dictionary containing your name, age, and course.
2. Access the name and age from the dictionary.
3. Add a new key called `city`.
4. Update the age.
5. Remove one key using `pop()`.
6. Print all dictionary keys.
7. Print all dictionary values.
8. Loop through a dictionary using `items()`.
9. Create a set containing five numbers.
10. Create a set from a list containing duplicate elements.

## Intermediate Level

11. Count the frequency of each character in a string using a dictionary.
12. Count how many times each number appears in a list.
13. Merge two dictionaries using `update()`.
14. Create a nested dictionary for three students.
15. Find unique elements from a list using a set.
16. Find common elements between two sets.
17. Find the union of two sets.
18. Find the difference between two sets.
19. Check whether one set is a subset of another.
20. Remove duplicate words from a sentence.

## Advanced Level

21. Find the student with the highest marks using a dictionary.
22. Count the frequency of each word in a sentence.
23. Find common elements among three sets.
24. Group numbers into even and odd lists using a dictionary.
25. Create a dictionary from two lists: one containing keys and another containing values.

## Generative AI Practice

26. Create a dictionary containing AI model configuration details.
27. Create a list containing multiple chat message dictionaries.
28. Create a nested dictionary representing a user profile.
29. Extract unique words from a user message using a set.
30. Create a simple chat history manager using a list of dictionaries.

---

# 23. Important Interview Questions

1. What is a dictionary in Python?
2. What is a set in Python?
3. What is the difference between a dictionary and a set?
4. Are dictionaries mutable?
5. Can dictionary keys be duplicated?
6. What types of objects can be dictionary keys?
7. What is the difference between `get()` and square bracket access?
8. What is the purpose of `items()`?
9. What is the difference between `pop()` and `popitem()`?
10. What does `setdefault()` do?
11. Why does `{}` create an empty dictionary?
12. How do you create an empty set?
13. Why are duplicate elements removed from a set?
14. Can a set contain a list?
15. What is the difference between `remove()` and `discard()`?
16. Explain union and intersection.
17. What is symmetric difference?
18. What is dictionary comprehension?
19. What is set comprehension?
20. Why are dictionaries useful when working with APIs and JSON?

---

# 24. Quick Revision Cheat Sheet

## Dictionary

```python
data = {"name": "Alex", "age": 21}

data["city"] = "Kolkata"      # Add
data["age"] = 22              # Update

data.get("name")              # Access safely
data.keys()                   # All keys
data.values()                 # All values
data.items()                  # Key-value pairs

data.update({"age": 23})      # Update multiple values
data.pop("age")                # Remove specified key
data.popitem()                 # Remove last inserted pair
data.copy()                    # Shallow copy
data.setdefault("course", "BCA")
data.clear()                   # Remove everything
```

## Set

```python
A = {1, 2, 3}
B = {3, 4, 5}

A.add(4)                       # Add one element
A.update([5, 6])               # Add multiple elements

A.remove(2)                    # Remove; error if missing
A.discard(10)                  # Remove; no error if missing
A.pop()                        # Remove arbitrary element
A.copy()                       # Shallow copy

A.union(B)                     # Union
A.intersection(B)              # Intersection
A.difference(B)                # Difference
A.symmetric_difference(B)     # Symmetric difference

A.issubset(B)                  # Subset check
A.issuperset(B)                # Superset check
A.isdisjoint(B)                # No common elements check

A.clear()                      # Remove everything
```

---

# 25. What Should You Remember for Future GenAI Development?

Prioritize these concepts:

- Dictionary creation and accessing values.
- `get()`, `keys()`, `values()`, and `items()`.
- Adding, updating, and deleting dictionary values.
- Nested dictionaries.
- Dictionary comprehension.
- Set creation and duplicate removal.
- `add()`, `update()`, `remove()`, and `discard()`.
- Union, intersection, difference, and symmetric difference.
- Lists of dictionaries for storing chat messages.
- Dictionaries for handling API responses and model configurations.

**My recommendation:** Do not just memorize methods. Practice writing small programs using dictionaries and sets. You will encounter these structures frequently when working with APIs, JSON, LLMs, and RAG applications.

---

## Day 06 Completed – Dictionaries and Sets

**Next:** Day 07 – Revision and Mini Project

Keep practising, keep building, and keep pushing your code to GitHub! 🚀