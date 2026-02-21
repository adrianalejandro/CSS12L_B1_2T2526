import csv
import os

filename = "materials.csv"

materials = dict()

def load_from_csv():

	if os.path.exists(filename):

		file = open(filename, "r")
		reader = csv.reader(file)

		next(reader, None)

		for column in reader:
			name = column[0].capitalize()
			tensile_strength = int(column[1])
			materials[name] = tensile_strength

	else:
		print("The file doesn't exists")
		
	file.close()

def save_to_csv():

	file = open(filename, "w", newline = "")
	writer = csv.writer(file)
	writer.writerow(["Material", "Tensile Strength"])

	for name in materials:
		writer.writerow([name.capitalize(), materials[name]])

	file.close()

def add_material():

    name = input("Material name: ").capitalize()

    if name in materials:
        print("Material already exists.")
        x = input("Do you want to update it? (yes/no): ")
        if x.lower() == "yes":
        	update_material()
        else:
        	return

    tensile_strength = int(input("Tensile Strength (MPa): "))

    if tensile_strength < 0:
    	print("Tensile strength must be a positive number.")
    	return

    materials[name] = tensile_strength

    print(f'{name} added successfully!')

def view_strongest_material():

    strongest = max(materials, key=materials.get)

    print(f'Strongest material: {strongest} ({materials[strongest]} MPa)')

def update_material():

    name = input("Enter material name to update: ").capitalize()

    if name.capitalize() in materials:

        new_strength = int(input("Enter new tensile strength (MPa): "))

        if new_strength < 0:
        	print("Tensile strength must be a positive number.")
        	return
        
        materials[name.capitalize()] = new_strength

        print("Material updated successfully.")

    elif name is not materials:
        	print("Material not found.")
        	x = input("Do you want to add? (yes/no): ")
        	if x.lower() == "yes":
        		add_material()
        	else:
        		return

def delete_material():

    name = input("Enter the material to delete: ").capitalize()

    if name.capitalize() in materials:
        del materials[name.capitalize()]
        print(f'{name} has been deleted.')

    else:
        print("Material not found.")

def display_all_material():
	y = input("Sort by (name/strength)? ")
	if y.lower() == "name":
		print("Data successfully loaded. Displaying contents sorted by name:\n")
		sorted_materials = sorted(materials.items())
		print("Material".ljust(30), "Tensile Strength (MPa)")
		print("-" * 45)
		for name, tensile_strength in sorted_materials:
			print(name.ljust(30), tensile_strength)

	elif y.lower() == "strength":
		print("Data successfully loaded. Displaying contents sorted by name:\n")
		sorted_material = sorted(materials.items(), key=lambda x: -x[1])
		print("Material".ljust(30), "Tensile Strength (MPa)")
		print("-" * 45)
		for name, tensile_strength in sorted_material:
			print(name.ljust(30), tensile_strength)

def display_menu():
    print('''
    	=== Material Strength Calculator ===
		1. Add Material
		2. View Strongest Material
		3. Update Material
		4. Delete Material
		5. Display All Materials
		6. Save to CSV
		7. Load from CSV
		8. Exit
		''')

load_from_csv()
while True:

	display_menu()
	choice = int(input("Enter your choice: "))

	match(choice):
		    case 1:
		        add_material()

		    case 2:
		        view_strongest_material()

		    case 3:
		    	update_material()

		    case 4:
		    	delete_material()

		    case 5:
		        display_all_material()

		    case 6:
		        save_to_csv()
		        print("Saving to materials.csv....")
		        print("Data successfully saved to CSV.")

		    case 7:
		    	load_from_csv()

		    case 8:
		    	answer = input("Would you like to save before exiting? (yes/no): ")

		    	if answer.lower() == "yes":
		    		print("Saving to materials.csv...")
		    		save_to_csv()
		    		print("Data successfully saved to CSV.")
		    		print("Exiting program. Goodbye!")
		    		break
		    case _:
		        print("Invalid choice.")

