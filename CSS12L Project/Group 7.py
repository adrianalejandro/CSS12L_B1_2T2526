import csv

materials = {}

FILE_NAME = "materials.csv"

def add():
    name = input("Material Name: ").strip().title()

    if name in materials:
        choice = input("Material already exists. Do you want to update it? (y/n): ").lower()
        if choice == "y":
            new_strength = float(input("Enter new tensile strength (MPa): "))
            materials[name] = new_strength
            print(f"{name} updated successfully.")
        else:
            print("No changes made.")
    else:
        strength = float(input("Tensile Strength (MPa): "))
        materials[name] = strength
        print("Material added successfully!")

def strongest():
    if not materials:
        print("No materials available.")
        return

    strongest = max(materials, key=materials.get)
    print(f"Strongest material: {strongest} ({materials[strongest]} MPa)")

def update():
    name = input("Enter the material name to update: ").strip().title()

    if name in materials:
        new_strength = float(input("Enter new tensile strength (MPa): "))
        materials[name] = new_strength
        print(f"{name} updated successfully.")

    else:
        print("Material not found.")
        choice = input("Do you want to add it? (y/n): ").lower()

        if choice == "y":
            strength = float(input("Enter tensile strength (MPa): "))
            materials[name] = strength
            print(f"{name} added successfully.")

def delete():
    name = input("Enter the material to delete: ").strip().title()

    if name in materials:
        del materials[name]
        print(f"{name} has been deleted.")

    else:
        print("Material not found.")

def see(sort_by='strength'):
    if not materials:
        print("No materials to display.")
        return

    print("\nMaterial\tTensile Strength (MPa)")
    print("--------------------------------------------")

    if sort_by == "name":
        sorted_items = sorted(materials.items())
    else:
        sorted_items = sorted(materials.items(), key=lambda x: x[1])

    for name, strength in sorted_items:
        print(f"{name}\t\t{strength}")

def save_to_csv():
    print("Saving to materials.csv")
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Material", "Tensile Strength"])
        for name, strength in materials.items():
            writer.writerow([name, strength])
    print("Data successfully saved to CSV.")

def load_from_csv():
    global materials

    print("Loading from materials.csv")

    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  

            materials = {}
            for row in reader:
                if len(row) == 2:
                    name, strength = row
                    materials[name] = float(strength)

        print("Data successfully loaded. Displaying contents sorted by name:")
        see(sort_by='name')

    except FileNotFoundError:
        materials = {}
        print("No existing CSV file found.")

def out():
    choice = input("Would you like to save before exiting? (y/n): ").lower()
    if choice == "y":
        save_to_csv()
    print("Exiting program. Goodbye!")
    exit()
 
def menu():   

    while True:
        print('''\n=== Material Strength Calculator ===
            1. Add Material
            2. View Strongest Material
            3. Update Material
            4. Delete Material
            5. Display All Materials
            6. Save to CSV
            7. Load from CSV
            8. Exit
            ''')

        choice = input("Enter your choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            strongest()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            sort_choice = input("Sort by (name/strength)? ").lower()
            see(sort_by=sort_choice)
        elif choice == "6":
            save_to_csv()
        elif choice == "7":
            load_from_csv()
        elif choice == "8":
            out()
        
        else:
            print("Invalid choice. Please select 1–8.")


menu()
