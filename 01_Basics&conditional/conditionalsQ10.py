Species = str(input("Enter the species of the animal: "))
Age = int(input("Enter the age of the animal: "))

if Species.lower() == "dog":
    if Age < 2:
        print("Puppy Food")
    elif 2 <= Age <= 7:
        print("Adult Dog Food")
    else:
        print("Senior Dog Food")
        
if Species.lower() == "cat":
    if Age < 2:
        print("Kitten Food")
    elif 2 <= Age <= 7:
        print("Adult Cat Food")
    else:
        print("Senior Cat Food")