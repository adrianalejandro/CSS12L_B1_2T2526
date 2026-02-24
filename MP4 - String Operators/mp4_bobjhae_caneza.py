#1. Full Name Super Formatter (10 pts.)

first_name = input("Enter your first name: ").capitalize()
middle_name = input("Enter your middle name: ").capitalize()
last_name = input("Enter your last name: ").capitalize()

print(f"Formatted Name: {last_name}, {first_name} {middle_name[0]}.")

#2. Word Pyramid (10 pts.)

word = input("Enter a word: ")
number = int(input("Enter a number: "))

for x in (range(number)):
	print((x+1) * word)

#3. Sentence Analyzer (10 pts.)

sentence = input("Enter a sentence: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
total_vowels = 0

x = sentence.split()
y = len(x)

for char in sentence:
	if char in vowels:
		total_vowels += 1

print(f"Characters: {len(sentence)}")
print(f"Words: {y}")
print(f"Vowels: {total_vowels}")

#4. Palindrome Detector (10 pts.)

word = input("Enter a word: ")
palindrome = word[::-1]

if word.lower() == palindrome.lower():
	print("The word is a palindrome!")
else:
	print("The word is not a palindrome.")

#5. Shout Backwards (10 pts.)

phrase = input("Enter a phrase: ").upper()

x = phrase[::-1]

print(f"Output: {x}")

#6. Email Validator and Username Formatter (30 pts.)

email = input("Enter your email address: ").lower()

if "@" and "." not in email:
	print("Invalid email address. Please include @ and a dot (.)")

else:
	extract = email.find("@")
	username = email[:extract].lower()
	suggest_username = username.replace("."," ").replace("_"," ")
	print(f'Your username is: {suggest_username}')

#7. Smart Email Analyzer (20 pts.)

email = input("Enter your email address: ")

x = email.count("@")

if "@" not in email:
	print("Invalid email: missing '@'")

elif x != 1:
	print("@ must be exactly one.")

elif " " in email:
	print("Invalid email: contains spaces.")

elif not (email.endswith(".org") or email.endswith(".edu") or email.endswith(".com")):
	print("Invalid email: domain must end with .com, .edu, or .org.")

else:
	x = email.find("@")
	username = email[:x].lower()
	domain = email[x+1:].lower()
	suggest_username = username.replace("."," ").replace("_"," ")
	print(f'Username: {suggest_username} | Domain: {domain}')


