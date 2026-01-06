items = ["apple", "banana", "orange", "apple", "mango"]


Unique_items = set()

for item in items:
    if item in Unique_items:
        print(f"{item} - already exists")
    else:
        Unique_items.add(item)
        print(f"{item} - added to the set")