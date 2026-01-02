# برنامه تشخیص قبولی

name = input("Enter student name: ")
score = float(input("Enter score (0-20): "))

if score >= 10:
    print(f"{name} passed the exam!")
else:
    print(f"{name} failed the exam!")
