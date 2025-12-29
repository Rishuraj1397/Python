Distance = int(input("Enter the distance you want to travel (in km): "))

if Distance < 3:
    print("You can walk to your destination.")
elif 3 <= Distance <= 15:
    print("You should consider biking.")
else:
    print("It's best to take public transport or drive.")