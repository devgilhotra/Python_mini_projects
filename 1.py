# Student Grade Calculator — Take marks for 5 subjects, calculate total, percentage, grade, pass/fail, and highest subject.

math = int(input("enter your marks: "))
physics = int(input("enter your marks: "))
chemistry = int(input("enter your marks: "))
english = int(input("enter your marks: "))
history = int(input("enter your marks: "))

total_marks = math + physics + chemistry + english + history
print("Toatal marks: ", total_marks)

percentage = (total_marks * 100) / 500 
print("Percentage of marks is: ", percentage)

if total_marks >= 450:
    print("Grade A")
elif total_marks >= 400:
    print("Grade B")
elif total_marks >= 350:
    print("Grade C")
elif total_marks >= 300:
    print("Grade D")
elif total_marks >= 250:
    print("Grade E")
else:
    print("Grade F")

if total_marks > 250 or percentage > 50:
    print("Pass")
else:
    print("Fail")

highest_marks = max(math, physics, chemistry, english, history)
print("Highest marks:", highest_marks)