import csv

class Project:
    def __init__(self, name, start, end, percent, status):
        self.name = name
        self.start = start
        self.end = end
        
        self.percent = percent
        self.status = status

projects_list = []

def load_data():
	try:
		with open('projects.csv', mode='r') as file:
			reader = csv.DictReader(file)
			projects_dict = {}
			for row in reader:
				obj = Project(row['Project Name'], row['Start Date'], row['End Date'], row['Percentage Complete'], row['Status'])
				projects_dict[row['Project Name'].strip().lower()] = obj
		print("Data loaded Successfully!")		
	except FileNotFoundError:
		x = input("Error! File not Found!")

def save_data():
	with open('projects.csv', mode='w', newline='') as file:
		fieldnames = ['Project Name', 'Start Date', 'End Date', 'Percentage Complete', 'Status']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
		for p in projects_list:
			writer.writerow({
				'Project Name': p.name, 'Start Date': p.start,
				'End Date': p.end, 'Percentage Complete': p.percent, 'Status': p.status
			})

def add_new_project():
	name = input("Enter Project Name: ")
	start = input("Enter Start Date: ")
	end = input("Enter End Date: ")
	percent = input("Enter Percentage: ")
	status = input("Enter Status (Planned/Ongoing/Complete): ")
	
	new_obj = Project(name, start, end, percent, status)
	projects_list.append(new_obj)
	print("Project added successfully!")

def view_all_projects():
	projects_table = dict()

	with open("projects.csv") as file:
			table = file.read()
	rows = table.split("\n")

	x=0

	for row in rows:
			projects_table[x] = row
			column = row.split(",")
			x = x + 1
	for key, value in projects_table.items():
			print(f'{key}: {value}')
    	
def update_status():
	name = input("Enter Project Name: ")

	for p in projects_list:
		if p.name.strip().lower() == name.strip().lower():
			p.percent = int(input(f"Enter new Percentage Completion for {p.name}: "))
			p.status = input(f"Enter new status for {p.name}: ")
			save_data()
			print("Status Successfully Updated")
			return
		print(f"Error. {p.name} not found")		

def sort():
	if not projects_list:
		print("No projects to filter.")
		return

	status_filter = input("Filter by status (Planned/Ongoing/Completed): ").capitalize()

	print(f"{'Project Name'} {'Start Date'} {'End Date'} {'% Complete'} {'Status'}")

	for p in projects_list:
		if p.status.capitalize() == status_filter:
			print(f"{p.name:<25} {p.start:<10} {p.end:<10} {p.percent:<10} {p.status:<10}")
			found = True

	else:
		print(f"No other projects found with status: {status_filter}")

def answer():
	answer = input("Do you wish to save before exiting? ")
	x = answer.lower()
	if(x=='yes'):
		save_data()
		print("Data saved! Goodbye")
	if(x=='no'):
		print("Data not saved! Goodbye")

#=============================Main Menu=============================#

load_data()

while True:
	print('''====== Construction Project Tracker ======
	1. Add New Project
	2. View All Projects
	3. Update Completion Status
	4. Sort by Status
	5. Save CSV file
	6. Load from CVS
	7. Exit
		''')
	choice = int(input("Select an option: "))

	match(choice):
		case 1:
			add_new_project()
		case 2:
			view_all_projects()
		case 3:
			update_status()
		case 4:
			sort()
		case 5:
			save_data()
			print("Data saved!")
		case 6:
			load_data()
		case 7:
			answer()
			break
		case _:
			print("Invalid choice. Please try again.")