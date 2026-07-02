def total_marks(math, science, english):
    return math+science+english

math = int(input("math: "))
science = int(input("science: "))
english = int(input("english:"))

total = total_marks(math, science, english)

print("total marks", total)

if total >=250:
    print("Grade: A")
elif total >=180:
    print("Grade: B")
else:
    print("Grade: C")
