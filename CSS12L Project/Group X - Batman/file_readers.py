inventory_table = dict()

with open("inventory.csv") as file:
	header_row = file.readline().strip()
	table = file.read()

# get headers as keys for the dictionary
headers = header_row.split(",")

# split table into rows
rows = table.split("\n")

x=0
# split each row into values/columns
for row in rows:
	
	columns = row.split(",")
	x += 1 #index for rows

	y = 0 #index for columns
	row_dict = dict()
	for column in columns:
		row_dict[headers[y]] = column
		y += 1

	inventory_table[x] = row_dict

for key, value in inventory_table.items():
	print(f'{key}: {value}')