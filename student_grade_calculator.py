name = input("Enter your name: ")
score = float(input("Enter your score: "))

if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
elif score >= 45:
    grade = "D"
elif score >= 40:
    grade = "E"
else:
    grade = "F"

print("Name:", name)
print("Score:", score)
print("Grade:", grade)