num = int(input("Enter a number: "))

for j in range(1, 11):
    if j == 5:
        continue
    print(num, "x", j, "=", num * j)
