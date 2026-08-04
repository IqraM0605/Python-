mark=int(input("Enter your marks: "))
if (mark>=90):
    print("A")
elif (mark>=80 and mark<90):
    print("B")
elif (mark>=70 and mark<80):
    print("C")
else:
    grade="F"
print("Grade is:", grade)