FruitaColour = input("Enter the color of the fruit: ").lower()
Fruit = input("Enter the type of fruit: ").lower()
if Fruit == "banana":
    if FruitaColour == "green":
        print("The fruit is unripe.")
    elif FruitaColour == "yellow":
        print("The fruit is ripe.")
    elif FruitaColour == "brown":
        print("The fruit is overripe.")