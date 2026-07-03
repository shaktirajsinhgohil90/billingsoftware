items = []

while True:
    item = input("enter item name:(type 'exit' to quit): ")
    if item.lower() == 'exit':
        break
    items.append(item)

print("\nShopping list:")

for item in items:
    print("_",item)

