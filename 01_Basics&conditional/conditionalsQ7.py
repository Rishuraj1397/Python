CoffeeSize = input("Enter coffee size (small, medium, large): ").lower()

extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").lower()

if extra_shot == "yes":
    if CoffeeSize == "small":
        print(CoffeeSize + " with an extra shot of espresso")
else:
    print(CoffeeSize + " coffee ")
