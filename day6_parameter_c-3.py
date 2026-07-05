def result(name, marks):
    if marks>= 35:
        print(name, "pass")
    else:
        print(name, "fail")
name = input("enter your name:")
marks = int(input("enter your marks:"))
result(name, marks)

