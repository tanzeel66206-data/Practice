

student={}
for i in range(5):
    name= input("enter name")
    marks= int(input("enter marks"))
    student[name]= marks

print(student)

for name,marks in student.items():
    grade=""
    if marks>=90 and marks<=100:
        grade="A"
    elif marks>=80 and marks<90:
        grade="B"
    elif marks>=70 and marks<80:
        grade="C"
    elif marks>=60 and marks<70:
        grade="D"
    else:
        grade="F"
    print(f"{name} got grade {grade}")


average= sum(student.values())/len(student)
print(f"Average marks: {average}")

highest_marks= max(student.values())
print(f"Highest marks: {highest_marks}")
