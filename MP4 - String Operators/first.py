# Full name

first = input("Enter your first name:\n").strip().capitalize()
middle = input("Enter your middle name:\n").strip().capitalize()
last = input("Enter your last name:\n").strip().capitalize()

formatted_name = f"{last}, {first} {middle[0]}."

print("Formatted Name:", formatted_name)
