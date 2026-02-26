#1. Full Name Super Formatter (10 pts.)

first_name = input("Enter your first name:\n").strip().capitalize()
middle_name = input("Enter your middle name:\n").strip().capitalize()
last_name = input("Enter your last name:\n").strip().capitalize()

formatted_name = f"{last_name}, {first_name} {middle_name[0]}."
print(f"Formatted Name: {formatted_name}")


#2. Word Pyramid (10 pts.)

word = input("Enter a word:\n")
N = int(input("Enter a number:\n"))

# Print pyramid
for i in range(1, N+1):
    print(word * i)


#3. Sentence Analyzer (10 pts.)

sentence = input("Enter a sentence:\n")

char_count = len(sentence)

word_count = len(sentence.split())

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in sentence if char in vowels)

print(f"Characters: {char_count}")
print(f"Words: {word_count}")
print(f"Vowels: {vowel_count}")



#4. Palindrome Detector (10 pts.)

word = input("Enter a word:\n").strip()

if word.lower() == word.lower()[::-1]:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")



#5. Shout Backwards (10 pts.)

phrase = input("Enter a phrase:\n")
# Uppercase and reversed
output = phrase.upper()[::-1]
print(f"Output: {output}")



#6. Email Validator and Username Formatter (30 pts.)

email = input("Enter your email address:\n").strip()

# Basic validity check
if "@" in email and "." in email:
    username = email.split("@")[0].lower()
    username = username.replace(".", " ").replace("_", " ")
    print(f"Your username is: {username}")
else:
    print('Invalid email address. Please include "@" and a dot (.)')



#7. Smart Email Analyzer (20 pts.)

email = input("Enter your email address:\n").strip()

# Validation checks
if "@" not in email:
    print("Invalid email: missing '@' symbol.")
elif email.count("@") > 1:
    print("Invalid email: more than one '@' symbol.")
elif " " in email:
    print("Invalid email: email should not contain spaces.")
else:
    username, domain = email.split("@")
    if not (domain.endswith(".com") or domain.endswith(".edu") or domain.endswith(".ph")):
        print("Invalid email: domain must end with .com, .edu, or .org.")
    else:
        username_formatted = username.lower().replace("_", " ").replace(".", " ")
        print(f"Username: {username_formatted} | Domain: {domain}")
