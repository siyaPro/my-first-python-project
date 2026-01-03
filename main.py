# student pass checker

name = input("Enter student name: ")
score = float(input("Enter score (0-20): "))

if score < 0 or score > 20 :
    print('invalid score! ')

elif score == 10 :
    print(f"{name} passed (border line).")

elif score > 10 :
    print(f'{name} passed.')

elif score < 10 :
    print(f'{name} failed.')

