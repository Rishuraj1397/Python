Password = input("Enter your password: ")

count = len(Password)

if count < 6:
    print("Weak password")
elif 6 <= count <= 10:
    print("Moderate password")
else:
    print("Strong password")