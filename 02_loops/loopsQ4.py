char = str(input("Enter a string: "))
reversed_str = ""
for char in char:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)