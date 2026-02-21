balance = 10000

def display_menu():
	print('''
		==== ATM Menu ====
		1. Check Balance
		2. Deposit Money
		3. Withdraw Money
		4. Exit
		''')

def check_balance():
	print(f'Your balance is {balance}')

def deposit():
	dep = float(input('Enter amount to deposit:'))
	return dep 

def withdraw():
	withdrawal = float(input('Enter amount to withdraw: '))
	return withdrawal
#=============MAIN MENU=============#


while(True):

	display_menu()
	choice = int(input('Enter choice: '))

	match(choice):
		case 1:
			check_balance()
		case 2:
			balance = balance + deposit()
			check_balance()
		case 3:
			balance = balance - withdraw()
			check_balance()
		case 4:
			print('You are now exiting the program...')
			break

