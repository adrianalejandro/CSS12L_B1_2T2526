import csv

class Project:
    def __init__(self, name, start, end, percent, status):
        self.name = name
        self.start = start
        self.end = end
        
        self.percent = percent
        self.status = status

projects_dict = {}

def load_data():#this loads the data from csv and puts it into a dictionary
	global projects_dict
	try:
		with open('projects.csv', mode='r') as file:
			reader = csv.DictReader(file)
			for row in reader:
				obj = Project(row['Project Name'], row['Start Date'], row['End Date'], row['Percentage Complete'], row['Status'])
				projects_dict[row['Project Name'].strip().lower()] = obj
		print("Data loaded Successfully!")		
	except FileNotFoundError:
		print("Error! File not Found!")

def save_data():#this uses file write and adds or updates the project inside of the dictionary
	with open('projects.csv', mode='w', newline='') as file:
		fieldnames = ['Project Name', 'Start Date', 'End Date', 'Percentage Complete', 'Status']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		writer.writeheader()
		for p in projects_dict.values():
			writer.writerow({
				'Project Name': p.name, 'Start Date': p.start,
				'End Date': p.end, 'Percentage Complete': p.percent, 'Status': p.status
			})

def add_new_project():#This adds the project and checks if there is more than one of these in the dictionary
	name = input("Enter Project Name: ")
	key = name.strip().lower()

	if key in projects_dict:
		print(f"{name} is already in projects.csv!")
		return 

	start = input("Enter Start Date: ")
	end = input("Enter End Date: ")
	percent = input("Enter Percentage: ")
	status = input("Enter Status (Planned/Ongoing/Complete): ")

	new_obj = Project(name, start, end, percent, status)
	projects_dict[key] = new_obj
	print("Project added successfully!")

def view_all_projects():#views all project in the dictionary in a column format
	print("====== Construction Project Tracker ======")
	
	print(f"{'Project Name':30} {'Start Date':15} {'End Date':15} {'% Complete':<12} {'Status':12}")
	print("-" * 90)

	if not projects_dict:
		print("No projects to display.")
		return

	for p in projects_dict.values():
		print(f"{p.name:30} {p.start:15} {p.end:15} {p.percent:<12} {p.status:12}")
    	
def update_status():#updates status by matching project name to name in csv-dictionary
	name = input("Enter Project Name: ").strip().lower()

	if name in projects_dict:
		p = projects_dict[name]
		p.percent = int(input(f"Enter new Percentage Completion for {p.name}: "))
		p.status = input(f"Enter new status for {p.name} (Planned, Ongoing, Completed): ")
		print("Status Successfully Updated! (Don't Forget to Save!)")
		return
	else:	
		print("Error. Project not found")			

def sort():#sorts the dictionary into groups based on the given status filter
	if not projects_dict:
		print("No projects to filter.")
		return

	status_filter = input("Filter by status (Planned/Ongoing/Completed): ").strip().capitalize()

	print(f"\n{'Project Name':30} {'Start Date':15} {'End Date':15} {'% Complete':<12} {'Status':12}")
	print("-" * 90)

	Found = False
	for p in projects_dict.values():
		if p.status.capitalize() == status_filter:
			print(f"{p.name:30} {p.start:15} {p.end:15} {p.percent:<12} {p.status:12}")
			Found = True

	if not Found:
		print(f"No other projects found with status: {status_filter}")

def answer():#exits the program, ask if saves and exit and breaks loop
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
	6. Load from CSV
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

