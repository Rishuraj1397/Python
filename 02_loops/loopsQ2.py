number = int(input("Enter a number: "))


sum = 0
for i in range(0, number + 1):
    if i % 2 == 0:
        print(i)
        sum += i
print("Sum of even numbers from 0 to", number, "is:", sum)