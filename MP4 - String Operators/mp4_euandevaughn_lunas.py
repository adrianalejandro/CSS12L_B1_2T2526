#All calling functions are in #comment mode. Thank you!

#1 FULL-NAME SUPER FORMATTER (10pts.)
def fullname():

	one = input('Enter First Name: ').lower()
	two = input('Enter Middle Name: ').lower()
	three = input('Enter Last Name: ').lower()
	another_yey = two[:1]
	yey = f'{three}, {one} {another_yey}.'.title()

	print('='*40 + f"\nFull Unedited Format:\n{three}, {one} {two}")
	print(f'Super Format:\n{yey}')

#fullname()

#2 WORD PYRAMID (10pts.)
def wordpyramid(num, word):
	for i in range(1, num + 1):
		print(word * i)

word = input('Enter Word: ')
num = int(input('Enter Number: '))

#wordpyramid(num, word)

#3 SENTENCE ANALYZER (10pts.)
def sentence_analyzer():
	sentence = input('Enter Sentence: ')
	vowels = "aeiouAEIOU"
	vowel_count = sum(char in vowels for char in sentence)
	words = sentence.split()
	character_count = len(sentence)
	word_count = len(words)

	print(f'Total Words: {word_count}\nTotal Characters: {character_count}\nTotal Vowels: {vowel_count}')

#sentence_analyzer()

#4 PALINDROME DETECTOR (10pts.)
def palindrome_checker():
	word = input('Enter Word: ').lower()
	checker = word[::-1].lower()
	if word == checker:
		print(f'{word} is a Palindrome! :]')

	else:
		print('This is not a Palindrome, Silly!')

#palindrome_checker()

#5 SHOUT BACKWARDS (10pts.)
def shout_backwards():
	sentence = input('Enter Phrase to Backwardsify: ').upper()
	backwards = sentence[::-1]

	print(f'{sentence}\n{backwards}')

#shout_backwards()

#6 EMAIL VALIDATOR & USERNAME FORMATTER (30pts.)
def emailkemerut():
	email = input('Enter Email Address: ').lower()
	at = "@" 

	if "@" and "." in email:
		index = email.find(at)
		this = email[:index]
		that = this.replace("_", " ")
		print(f'{that} is your username!')

	else:
		print(f"{email} has no '@' and/or '.'")

#emailkemerut()

#7 SMART EMAIL ANALYZER (20pts.)
def email_yesh():
    email = input("Enter your email address: ")

    if email.count('@') != 1:
        print("Invalid email: missing '@' symbol.")
        return

    if ' ' in email:
        print("Invalid email: contains space.")
        return

    index = email.find('@')
    username = email[:index]
    domain = email[index + 1:]
    valid = ('.com', '.edu', '.org')
    if not domain.endswith(valid):
        print("Invalid email: domain must end with .com, .edu, or .org.")
        return

    cleany = username.lower()
    formatted = cleany.replace('_', ' ').replace('.', ' ')
    print(f"Username: {formatted} | Domain: {domain}")

#email_yesh()





