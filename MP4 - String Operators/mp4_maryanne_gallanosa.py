#1. Full Name Super Formatter

first_name = input("Enter your first name: ").strip()
middle_name = input("Enter your middle name: ").strip()
last_name = input("Enter your last name: ").strip()

first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

full_name = print(f'Formatted name: {last_name}, {first_name} {middle_name}')


#2. Word Pyramid

word = input("Enter a word: ")
number = int(input("Enter a number: "))
for x in range(1, number + 1):
	print(word * x)

#3. Sentence Analyzer

sentence = input("Enter a sentence:\n")
total_characters = len(sentence)
words = sentence.split()
total_words = len(words)

vowels = "aeiouAEIOU"
total_vowels = 0

for letter in sentence:
    if letter in vowels:
        total_vowels += 1

print("\nCharacters:", total_characters)
print("Words:", total_words)
print("Vowels:", total_vowels)

#4. Palindrome Detector

word = input("Enter a word: ")

if word == word[::-1]:
	print("The word is a palindrome!")
else:
	print("The word is Not a palindrome.")

#5. Shout Backwards

x = input("Enter a phrase: ")
x = x.upper()
reverse = x[::-1]
print("Output: ", reverse)

#6. Email Validator and Username Formatter

email = input("Enter your email address: ")

x = "@" in email
y = "." in email

if x and y:
	position = email.find("@")
	username = email[:position]
	username = username.lower()
	username = username.replace("_", " ")
	print("Your username is: ", username)

else: 
	print("Invalid email address.")
	print("Please include '@' and '.'")


#7. Smart Email Analyzer

email = input("Enter your email address: ")

if " " in email:
	print("Invalid email: email must not contain spaces.")
elif email.count("@") != 1:
	print("Invalid email: missing '@' symbol.")
else:
	x = email.find("@")

	username = email[:x]
	domain = email[x + 1:]

	if domain.endswith(".com") or domain.endswith(".edu") or domain.endswith(".org"):
		username = username.lower()
		username = username.replace("_", " ")
		username = username.replace(".", " ")
		print("Username:", username)
		print("Domain:", domain)

	else:
		print("Invalid email: domain must end with .com, .edu, or .org.")
