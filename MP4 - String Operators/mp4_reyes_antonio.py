#1.
def name():
	x = input("Enter your first name: ")
	y = input("Enter your middle name: ")
	z = input("Enter your last name: ")

	first = x.lower().title().strip()
	middle = y.lower().capitalize()[0]
	last = z.lower().capitalize().strip()

	print(f"Your formated name is: {last}, {first} {middle}.")
 
name()

#2.
def pyramid():
	word = input("Enter a word: ")
	number = int(input("Enter a number: "))

	for w in range(1, number + 1):
		print(word*w)

pyramid()

#3.
def length():
	z = input("Enter sentence: ")
	sentence = z.title().strip()
	word_list = sentence.split()
	a = len(word_list)
	b = len(sentence)

	def vowels(text):
		bilang = 0
		vowels = "aeiouAEIOU"
		for c in text:
			if c in vowels:
				bilang += 1
		return bilang

	total_vowels = vowels(sentence)	

	print(f"""Characters: {b}
Words: {a}
Vowels: {total_vowels}""")		

length()

#4.
def palindrome():
	w = input("Enter a word: ")
	word = w.lower()
	reverse = word[::-1]

	if reverse == word:
		print("This word is a Palindrome")
	else:
		print("This word is not a  Palindrome")	

palindrome()

#5.
def shout():
	x = input("Enter a Phrase: ")
	shout = x.upper()

	print(shout[::-1])

shout()

#6.
def email():
	email = input("Enter your email: ")

	index = email.find("@")

	if (email.count("@")==1) and (email.count(".")!=0):
		user = email[:index]
		username = user.lower()
		format_user = username.replace(".", " ").replace("_", " ")

		print(f"Your username is {format_user}")
	else:
		print("Invalid email! Must Contain @ and .")	

email()

#7
def gmail():
    email = input("Enter your email address: ")

    if " " in email:
        print("Invalid email: contains spaces.")

    elif email.count("@") != 1:
        print("Invalid email: missing '@' symbol.")

    else:
        index = email.find("@")
        domain = email[index + 1:]

        if not (domain.endswith(".com") or domain.endswith(".edu") or domain.endswith(".org")):
            print("Invalid email: domain must end with .com, .edu, or .org.")

        else:

            username = email[:index]
            username = username.lower()
            username = username.replace("_", " ").replace(".", " ")

            print("Username:", username)
            print("Domain:", domain)

gmail()
