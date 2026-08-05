# Tuple in Python

# Create a tuple
tup = (10, 20, 30, 40, 50)

print("Original Tuple:", tup)

# -----------------------------
# Access Elements (Indexing)
# -----------------------------
print("First Element:", tup[0])
print("Last Element:", tup[-1])

# -----------------------------
# Slicing
# -----------------------------
print("Elements from index 1 to 3:", tup[1:4])

# -----------------------------
# count() - Counts occurrences
# -----------------------------
tup2 = (10, 20, 10, 30, 10)

print("Tuple:", tup2)
print("Count of 10:", tup2.count(10))

# -----------------------------
# index() - Finds the index
# -----------------------------
print("Index of 30:", tup2.index(30))

# -----------------------------
# Length of Tuple
# -----------------------------
print("Length of Tuple:", len(tup))

# -----------------------------
# Membership
# -----------------------------
print("Is 20 present?", 20 in tup)
print("Is 100 present?", 100 in tup)

# -----------------------------
# Concatenation
# -----------------------------
tup3 = tup + (60, 70)

print("After Concatenation:", tup3)

# -----------------------------
# Repetition
# -----------------------------
print("Repeated Tuple:", tup * 2)