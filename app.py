#first project
print("Welcome to the student grade calculator")

# allow repeats
num_students = int(input("Enter number of students: "))
for i in range(1, num_students + 1):
    print(f"\n Enter scores for student {i}: ")

    # inputs
    sub1 = float(input("Enter your Math score: "))
    sub2 = float(input("Enter your English score: "))
    sub3 = float(input("Enter your physics score: "))

    # calculate
    total = sub1 + sub2 + sub3
    average = total / 3

    # grade
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    # out putes
    print("Result: ")
    print(f"your total is: {total}")
    print(f"your average is: {average}")
    print(f"your garde is: {grade}")
    if average >= 90:
        print("Awesome")
    elif average >= 60:
        print("Very Good!")
    else:
        print("Try more!")

