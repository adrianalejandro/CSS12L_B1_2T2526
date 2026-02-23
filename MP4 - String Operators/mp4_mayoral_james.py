###1.) Ask for first name, middle name, and last name. Format the output as: Last Name, First Name M.with proper capitalization)###

def name():
	x = input("Enter your first name: ")
	y = input("Enter your middle name: ")
	z = input("Enter your last name: ")

	first = x.lower().title().strip()
	middle = y.lower().capitalize()[0]
	last = z.lower().capitalize().strip()

	print(f"Your formated name is: {last}, {first} {middle}.")
 

###2.) Ask for a word and an integer N. Print the word in a growing pyramid pattern up to N times.###

def pyramid():
	word = input("Enter a word: ")
	number = int(input("Enter a number: "))

	for w in range(1, number + 1):
		print(word*w)


###3.) Ask for a sentence and return the total characters, words, and vowels###
