# # info = {
# #     "key" : "value" ,
# #     "name" : "Iqra" ,
# #     "learning" : "Python" ,
# #     "cgpa" : "8.70" ,
# #     "feeling" : "sad"
# # }
# # info["name"] = "UmmeHANI"
# # print(info)


# #NESTED DICTIONAY
# # student = {
# # "name ": "Iqra" ,
# # "subject" : {
# #     "sub1" : "Python" ,
# #     "sub2" : "Java" ,
# #     "sub3" : "C++"
# # }
# # }
# # print(len(student))
# # print(student)

# # Dictionary Methods in Python

# # Create a dictionary
# student = {
#     "name": "Iqra",
#     "age": 21,
#     "city": "Mumbai"
# }

# print("Original Dictionary:", student)
# # Output: Original Dictionary: {'name': 'Iqra', 'age': 21, 'city': 'Mumbai'}

# # -----------------------------
# # keys() - Returns all keys
# # -----------------------------
# print("Keys:", student.keys())
# # Output: Keys: dict_keys(['name', 'age', 'city'])

# # -----------------------------
# # values() - Returns all values
# # -----------------------------
# print("Values:", student.values())
# # Output: Values: dict_values(['Iqra', 21, 'Mumbai'])

# # -----------------------------
# # items() - Returns key-value pairs
# # -----------------------------
# print("Items:", student.items())
# # Output: Items: dict_items([('name', 'Iqra'), ('age', 21), ('city', 'Mumbai')])

# # -----------------------------
# # get() - Returns value of a key
# # -----------------------------
# print("Name:", student.get("name"))
# # Output: Name: Iqra

# # -----------------------------
# # update() - Updates/Adds elements
# # -----------------------------
# student.update({"age": 22})
# student.update({"course": "AI & ML"})
# print("After update():", student)
# # Output: After update(): {'name': 'Iqra', 'age': 22, 'city': 'Mumbai', 'course': 'AI & ML'}

# # -----------------------------
# # pop() - Removes a key
# # -----------------------------
# student.pop("city")
# print("After pop():", student)
# # Output: After pop(): {'name': 'Iqra', 'age': 22, 'course': 'AI & ML'}

# # -----------------------------
# # popitem() - Removes last item
# # -----------------------------
# student.popitem()
# print("After popitem():", student)
# # Output: After popitem(): {'name': 'Iqra', 'age': 22}

# # -----------------------------
# # copy() - Creates a copy
# # -----------------------------
# student_copy = student.copy()
# print("Copied Dictionary:", student_copy)
# # Output: Copied Dictionary: {'name': 'Iqra', 'age': 22}

# # -----------------------------
# # clear() - Removes all items
# # -----------------------------
# student_copy.clear()
# print("After clear():", student_copy)
# # Output: After clear(): {}

# practice
marks = {
    "Math": int(input("Enter Math marks: ")),
    "Science": int(input("Enter Science marks: ")),
    "English": int(input("Enter English marks: "))
}

print(marks)

# Output (Example):
# Enter Math marks: 80
# Enter Science marks: 75
# Enter English marks: 90
# {'Math': 80, 'Science': 75, 'English': 90}