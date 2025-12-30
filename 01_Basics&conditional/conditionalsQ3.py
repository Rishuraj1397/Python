Grades = int(input("Enter your grades: "))

if Grades >= 90:
    print("You received an A.")
elif 80 <= Grades < 90:
    print("You received a B.")
elif 70 <= Grades < 80:
    print("You received a C.")
elif 60 <= Grades < 70:
    print("You received a D.")
else:
    print("You received an F.")