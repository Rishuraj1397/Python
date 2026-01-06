num  = int(input("Enter a number: "))

i  = 2

while i < num:
    if num % i == 0:
        print(f"{num} is not a prime number.")
        break
    i += 1
else:
    if num > 1:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
        