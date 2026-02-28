
import csv
import os
#the imports below is only for the loading screen.
import time
import sys
#this import is only for colors. :]
import colorama
from colorama import Fore, Style, init

init(autoreset=True)
'''
this a global variable necessary for every 
function below to work and open the file.
'''
CSV_FILE = 'materials.csv'
#=====================CREDITS====================
def loading_aesthetic(duration = 5):
    print("Loading", end="")
    for _ in range(duration * 2):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\nDone!\nProgrammed by:{Fore.BLUE}\n1. Lunas, Euan Devaugn\n2. Ubarre, Jhune Gabriel\n3. Silva, Keian Carl{Style.RESET_ALL}")
    print(f'{Fore.YELLOW}Presented by Group DELL{Style.RESET_ALL}\nAssisted By:\n{Fore.BLUE}Custodio, Gabby Lionne{Style.RESET_ALL}')
#=====================CREDITS====================

#======================MENU======================
def menu_screen():
    print(f'''
    ==== Material Database Final Version! ====

    {Fore.CYAN}1. Add Material{Style.RESET_ALL}
    2. View Strongest Material
    {Fore.GREEN}3. Update Material{Style.RESET_ALL}
    {Fore.MAGENTA}4. Delete Material{Style.RESET_ALL}
    5. Display All Materials
    6. Exit
    ''')
#======================MENU======================

#=================LOAD_FROM_CSV==================
def load_csv_vertical(filename):
    '''
    Reads csv file and converts it into a dictionary named 'materials'
    Key: Material 
    Value: Tensile Strength 
    '''
    materials = {}

    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                material = row['Material'].strip()
                strength = float(row['Tensile Strength'].strip())
                materials[material] = strength

    #strip() function gets rid of 'dead space' before and after every material & strength entry
        print(f"Loaded {len(materials)} material(s) from {filename}.\n")

    except FileNotFoundError:
        print(f"'{filename}' not found. Starting with an empty database.\n")

    except Exception as e:
        print(f"Error reading CSV: {e}\n")

    return materials
#=================LOAD_FROM_CSV==================


#===================SAVE_TO_CSV==================
def update_to_csv(materials):
    '''
    Overwrites the materials.csv using writer() function with the current dictionary.
    this function is used to update the actual csv file. This function is called
    after cases 1, 3, and 4 specifically.
    '''

    try:
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Material', 'Tensile Strength'])  #This part is the header
            for material, strength in materials.items():
                writer.writerow([material, strength])

        print(f"  Saved to {CSV_FILE} successfully!\n")

    except Exception as e:
        print(f"  Error saving to CSV: {e}\n")
#===================SAVE_TO_CSV==================


#=====================DISPLAY====================
def display_materials(materials, sort_by='name'):
    '''
    Displays all materials in a table with added sorting! :]
    '''
    if not materials:
        print("  Database is empty.\n")
        return

    #sorts via user input. (needs to type 'material' or 'strength')
    if sort_by == 'strength':
        sorted_items = sorted(materials.items(), key=lambda x: x[1])
    else:
        sorted_items = sorted(materials.items(), key=lambda x: x[0].lower())

    print(f"\n{'#':<4} {'Material':<25} {'Tensile Strength':>18}")
    print("  " + "-" * 50)
#this code below numbers each entry for better finding
    for i, (material, strength) in enumerate(sorted_items, start=1):
        print(f"  {i}. {material:<24} {strength:>15.1f} MPa")

    print()
#=====================DISPLAY====================


#======================ADD=======================
def add_material(materials):
    '''
    This function lets the user add a new material to the dictionary
    - check for duplicate material_name
    - checks that strength is a positive number
    '''
    print("\n  -- Add Material --")
    material_name = input("  Enter Material Name: ").strip()

    if not material_name:
        print("  Material name cannot be empty.\n")
        return

    #a double checker if the material is already in the csv
    existing = next((k for k in materials if k.lower() == material_name.lower()), None)

    if existing:
        print(f"'{existing}' already exists in the database.")
        choice = input("  Do you want to update its strength instead? (y/n): ").strip().lower()
        if choice == 'y':
            update_material(materials, preset=existing)
        return

    #checks if strength is a positive number
    strength = get_valid_strength()
    if strength is None:
        return

    #adds it to dictionary to be saved in the csv
    materials[material_name] = strength
    print(f"  '{material_name}' added successfully!")
    update_to_csv(materials)
#======================ADD=======================


#====================STRONGEST===================
def strongest_material(materials):
    '''
    Scans the dictionary to find the material
    with the highest positive value tensile strength (MPa).
    '''
    if not materials:
        print("  Database is empty.\n")
        return

    max_material = None
    max_strength = -1

    for material, strength in materials.items():
        if strength > max_strength:
            max_strength = strength
            max_material = material

    print(f"\n  Strongest Material : {max_material}")
    print(f"  Tensile Strength   : {max_strength:.1f} MPa\n")
#====================STRONGEST===================

#=====================UPDATE=====================
def update_material(materials, preset=None):
    '''
    Updates the tensile strength of an existing material.
    'preset' is used internally when redirected from add_material()
    '''
    print("\n  -- Update Material --")
    display_materials(materials)

    if preset:
        material_name = preset
    else:
        material_name = input("  Enter material name to update: ").strip()

    #just like the add function, double checks if the material is already in the dictionary
    existing = next((k for k in materials if k.lower() == material_name.lower()), None)

    if not existing:
        print(f"  '{material_name}' not found in database.\n")
        choice = input("  Do you want to add it instead? (y/n): ").strip().lower()
        if choice == 'y':
            add_material(materials)
        return

    #gets the input and validates it
    strength = get_valid_strength()
    if strength is None:
        return

    materials[existing] = strength
    print(f"  '{existing}' updated successfully!")

    update_to_csv(materials)
#=====================UPDATE=====================


#=====================DELETE=====================
def delete_material(materials):
    #Removes a material from the dictionary
    print("\n  -- Delete Material --")
    display_materials(materials)

    material_name = input("  Enter material name to delete: ").strip()

    existing = next((k for k in materials if k.lower() == material_name.lower()), None)

    if not existing:
        print(f"  '{material_name}' not found in database.\n")
        return

    #confirmation for deletion. can be cancelled.
    confirm = input(f"  Are you sure you want to delete '{existing}'? (y/n): ").strip().lower()
    if confirm != 'y':
        print("  Deletion cancelled.\n")
        return
    #simply deletes the existing material
    del materials[existing]
    print(f"  '{existing}' deleted successfully!")

    update_to_csv(materials)
#=====================DELETE=====================


#===============POSITIVE_STRENGTH================
def get_valid_strength():
    '''
    Keeps displaying until the user enters a positive number.
    Returns the valid value, or none if the user decides to cancel
    by typing 'cancel' to the prompt
    '''
    while True:
        raw = input("  Enter Tensile Strength (MPa) [or 'cancel']: ").strip()

        if raw.lower() == 'cancel':
            print("  Operation cancelled.\n")
            return None

        try:
            value = float(raw)
            if value <= 0:
                print("  Strength must be a positive number. Try again.")
            else:
                return value
        except ValueError:
            print("  Invalid input. Please enter a number. Try again.")
#===============POSITIVE_STRENGTH================


#=====================PROGRAM====================
def calculator():
    materials = load_csv_vertical(CSV_FILE)
    loading_aesthetic()

    while True:
        menu_screen()

        try:
            option = int(input("  Enter Number Option: "))
        except ValueError:
            print("  Invalid input. Please enter a number from 1–6.\n")
            continue

        match option:
            case 1:
                add_material(materials)

            case 2:
                strongest_material(materials)

            case 3:
                update_material(materials)

            case 4:
                delete_material(materials)

            case 5:
                print("\n  -- Display All Materials --")
                sort_choice = input("  Sort by (name/strength): ").strip().lower()
                if sort_choice not in ('name', 'strength'):
                    sort_choice = 'name'
                display_materials(materials, sort_by=sort_choice)

            case 6:
                print("  Exiting program. Thank you for using our program! :]\n")
                break

            case _:
                print("  Invalid option. Please only choose between 1–6.\n")
#=====================PROGRAM====================

calculator()
