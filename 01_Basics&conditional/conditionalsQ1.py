Age = int(input("Enter your age: "))

if Age < 13:
    print("You are a child.")
elif 13 <= Age < 20:
    print("You are a teenager.")
elif 20 <= Age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    
    # just a comment