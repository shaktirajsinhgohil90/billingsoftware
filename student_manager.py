students = []

while True:
    student = input("enter student name (type '3' to quit): ")   


    if student.lower() == "3":
        print("Good Bye!")
        break

students.append(student)

print("\n Student list: ")

for student in students :
    print("_", student)
    