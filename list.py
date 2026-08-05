# marks= [85, 90, 78, 92, 88]
# print(marks)
# marks[2] = "iqra"
# print(marks[3])
# print(marks[2])

# List Methods in Python

# Create a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# -----------------------------
# append() - Adds an element at the end
# -----------------------------
numbers.append(60)
print("After append():", numbers)

# -----------------------------
# insert() - Inserts an element at a specific index
# -----------------------------
numbers.insert(2, 25)
print("After insert():", numbers)

# -----------------------------
# remove() - Removes the given element
# -----------------------------
numbers.remove(40)
print("After remove():", numbers)

# -----------------------------
# pop() - Removes the last element
# -----------------------------
removed = numbers.pop()
print("Popped Element:", removed)
print("After pop():", numbers)

# -----------------------------
# extend() - Adds multiple elements
# -----------------------------
numbers.extend([70, 80])
print("After extend():", numbers)

# -----------------------------
# count() - Counts occurrences
# -----------------------------
print("Count of 20:", numbers.count(20))

# -----------------------------
# index() - Finds the index of an element
# -----------------------------
print("Index of 30:", numbers.index(30))

# -----------------------------
# reverse() - Reverses the list
# -----------------------------
numbers.reverse()
print("After reverse():", numbers)

# -----------------------------
# sort() - Sorts the list
# -----------------------------
numbers.sort()
print("After sort():", numbers)

# -----------------------------
# copy() - Creates a copy
# -----------------------------
copy_list = numbers.copy()
print("Copied List:", copy_list)

# -----------------------------
# clear() - Removes all elements
# -----------------------------
copy_list.clear()
print("After clear():", copy_list)