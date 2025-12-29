Age = int(input("Enter your age: "))
day = input("Enter the day of the week: ")

price = 12 if Age >= 18 else 8

if day == "Wednesday" or day == "wednesday":
    price -= 2
    
print("The ticket price is:", price)