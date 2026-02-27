#This program stores different materials and their tensile strength (MPa).
# You can add, update, delete, and view materials. 
# The data is saved in a CSV fileso it will not be lost after closing.
# csv - for reading and saving data to a CSV file
# os - to check if the file exists

import csv
import os

filename = "materials.csv"

materials = dict()

def load_from_csv(): 
	if os.path.exists(filename): # Check if the CSV file exists
		if os.path.getsize(filename) > 0: # Check if the file is not empty
			with open(filename, "r") as file: # Open the file in read mode
				reader = csv.reader(file)  # Read the CSV file
				next(reader, None) # Skip the header row
				for column in reader:  # Loop through each row
					name = column[0].capitalize() # Get material name and capitalize it
					tensile_strength = int(column[1]) # Convert tensile strength to integer
					materials[name] = tensile_strength # Store data in dictionary


	else:
		pass  # Do nothing if file does not exist

def save_to_csv():

	with open(filename, "w", newline = "") as file: # Open CSV file in write mode (overwrite old data)
		writer = csv.writer(file) # Create a CSV writer object
		writer.writerow(["Material", "Tensile Strength"]) # Write header row first
		for name in materials:  # Loop through each material in dictionary
			writer.writerow([name, materials[name]])  # Write material name and its tensile strength into the file

def add_material():

    name = input("Material name: ").capitalize() # Ask user for material name and capitalize

    if name in materials:  # Check if material already exists
        print("Material already exists.")
        x = input("Do you want to update it? (yes/no): ") # Ask if user wants to update

        if x.lower() == "yes": # If user chooses yes
        	update_material() # Call update function
        	return
        else:
        	return # Stop the function if no

    raw_strength = (input("Tensile Strength (MPa): "))  # Ask for tensile strength input

    if not raw_strength.isdigit(): # Check if input is not numeric
    	print("Invalid input. Please enter a numerical value.")
    	return

    tensile_strength = int(raw_strength) # Convert string to integer

    if tensile_strength < 0:  # Check if value is negative
    	print("Tensile strength must be a positive number.")
    	return

    materials[name] = tensile_strength # Add material and strength to dictionary

    print(f'{name} added successfully!') # Display success message

def view_strongest_material():
#Check if the dictionary is empty.
	if not materials:
		print("No material found to view.")
		return
#If dictionary is not empty, proceed with the code below.
	strongest = max(materials, key=materials.get) #Traversing the dictionary and finding the key with the highest numerical value.
	print(f'Strongest material: {strongest} ({materials[strongest]} MPa)') #String formatting containing the key and its value.

def update_material():

    name = input("Enter material name to update: ").capitalize() #Maitaining consistency and ensuring that input would matched to the stored data.

    if name in materials: #Condition if input material was reflected.

        new_strength = (input("Enter new tensile strength (MPa): ")) #Tensile Strength is string due to the possibility of user input being non-numerical.

        if not new_strength.isdigit(): #If the string is not numerical, it falls under this condition. 
        	print("Invalid input. Please enter a numerical value.")
        	return

        convert_new_strength = int(new_strength) #If string is numerical, it will be converted to an integer.

        if convert_new_strength < 0: #Condition if the integer is less than 0.
        	print("Tensile strength must be a positive number.")
        	return
        #If integer is greater than 0, proceed with the saving or storing of the changes to the dictionary. 
        materials[name] = convert_new_strength

        print("Material updated successfully.")

    elif name not in materials: #Condition if the material was not found in the dictionary.
        	print("Material not found.")
        	x = input("Do you want to add? (yes/no): ")
        	if x.lower() == "yes":
        		add_material() #Calling the function in order for the object to be added.
        	else:
        		return

def delete_material():

    name = input("Enter the material to delete: ").capitalize()

    if name in materials:
        del materials[name] #Keyword for deleting an object.
        print(f'{name} has been deleted.')

    else:
        print("Material not found.")

#Function to display all materials
#Default sort by strength
def display_all_material(sort_by="strength"):

	#Check if the material dictionary is empty
	if not materials:
		print("No materials found to display.")
		return #Stops the function if no data exists

#Display materials sorted by tensile strength
	print("Data successfully loaded. Displaying contents sorted by strength:\n")
#Convert dictionary into key, value and sort by descending	
	sorted_material = sorted(materials.items(), key=lambda x: -x[1])
#Print table header
	print("Material".ljust(30), "Tensile Strength (MPa)")
	print("-" * 55)
#Loop through sorted materials and diplay each one
	for name, tensile_strength in sorted_material:
		print(name.ljust(30), tensile_strength)

#Ask the user if they want to sort alphabetically by name	
	y = input("Sort by name? ")
	if y.lower() == "yes":
		print("Data successfully loaded. Displaying contents sorted by name:\n")
#Sort dictionary alphabetically by material name		
		sorted_materials = sorted(materials.items())
#Print table header
		print("Material".ljust(30), "Tensile Strength (MPa)")
		print("-" * 55)
#Display sorted results
		for name, tensile_strength in sorted_materials:
			print(name.ljust(30), tensile_strength)
	else:
		return


#Function to display main menu
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

#Load saved data from csv file at the start of the program
load_from_csv()
#Main program loops continuously until user exits
while True:

#Display Menu options	
	display_menu()
#Get user input and convert to integer	
	choice = int(input("Enter your choice: "))

#Use match case to hablde menu selection
	match(choice):
	#Call the functions
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
		    	
		    	else:
		    		print("Exiting program. Goodbye!")
				#Exit the while loop and end program	
		    	break
			#Handles the invalid menu choices	
		    case _:
		        print("Invalid choice.")







