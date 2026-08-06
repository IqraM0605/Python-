# Set Methods in Python

# Create a set
numbers = {10, 20, 30, 40}

print("Original Set:", numbers)
# Output: Original Set: {10, 20, 30, 40}

# -----------------------------
# add() - Adds one element
# -----------------------------
numbers.add(50)
print("After add():", numbers)
# Output: After add(): {10, 20, 30, 40, 50}

# -----------------------------
# update() - Adds multiple elements
# -----------------------------
numbers.update([60, 70])
print("After update():", numbers)
# Output: After update(): {10, 20, 30, 40, 50, 60, 70}

# -----------------------------
# remove() - Removes an element
# -----------------------------
numbers.remove(20)
print("After remove():", numbers)
# Output: After remove(): {10, 30, 40, 50, 60, 70}

# -----------------------------
# discard() - Removes an element (No error if not found)
# -----------------------------
numbers.discard(100)
print("After discard(100):", numbers)
# Output: After discard(100): {10, 30, 40, 50, 60, 70}

# -----------------------------
# pop() - Removes a random element
# -----------------------------
removed = numbers.pop()
print("Removed Element:", removed)
print("After pop():", numbers)
# Output: Removed Element: (Any one element)
# Output: After pop(): Remaining elements

# -----------------------------
# copy() - Creates a copy
# -----------------------------
copy_set = numbers.copy()
print("Copied Set:", copy_set)
# Output: Copied Set: Same elements as numbers

# -----------------------------
# clear() - Removes all elements
# -----------------------------
copy_set.clear()
print("After clear():", copy_set)
# Output: After clear(): set()

# -----------------------------
# union() - Combines two sets
# -----------------------------
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1.union(set2))
# Output: Union: {1, 2, 3, 4, 5}

# -----------------------------
# intersection() - Common elements
# -----------------------------
print("Intersection:", set1.intersection(set2))
# Output: Intersection: {3}

# -----------------------------
# difference() - Elements in set1 but not in set2
# -----------------------------
print("Difference:", set1.difference(set2))
# Output: Difference: {1, 2}

# -----------------------------
# issubset() - Checks subset
# -----------------------------
print({1, 2}.issubset(set1))
# Output: True

# -----------------------------
# issuperset() - Checks superset
# -----------------------------
print(set1.issuperset({1, 2}))
# Output: True