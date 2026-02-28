#John Oliver Inac - CSSL
#1. Full name super formatter
first_name = input("Enter your first name: ").strip()
middle_name = input("Enter your middle name: ").strip()
last_name = input("Enter your last name: ").strip()

first_name = first_name.capitalize()
middle_initial = middle_name[0].capitalize()
last_name = last_name.capitalize()

print(f"Formatted Name: {last_name}, {first_name} {middle_initial}.")

#2 Word Pyramid 
word = input("Enter a word: ")
number = int(input("Enter a number: "))

print("Output:")
for i in range(1, number + 1):
    print(word * i)
#3 Sentence Analyzer
sentence = input("Enter a sentence: ")

characters = len(sentence)

words = sentence.split()
word_count = len(words)

vowels = "aeiouAEIOU"
vowel_count = 0

for letter in sentence:
    if letter in vowels:
        vowel_count += 1

print("Characters:", characters)
print("Words:", word_count)
print("Vowels:", vowel_count)

#4. Palindrome Detector

word = input("Enter a word: ")

reverse_word = word[::-1]

if word == reverse_word:
    print("The word is a palindrome!")
else:
    print("The word is NOT a palindrome.")

#5.Shout Backwards

phrase = input("Enter a phrase: ")

result = phrase.upper()[::-1]

print("Output:", result)

#6.Email Validator and Username Formatter

email = input("Enter your email address: ")

if "@" in email and "." in email:
    
    at_index = email.find("@")

    username = email[:at_index]
    
    username = username.lower()
    
    username = username.replace(".", " ")
    username = username.replace("_", " ")
    
    print("Your username is:", username)

else:
    print('Invalid email address. Please include "@" and a dot (.)')

#7. Smart Email Analyzer

email = input("Enter your email address: ")

if " " in email:
    print("Invalid email: should not contain spaces.")

elif email.count("@") != 1:
    print("Invalid email: missing '@' symbol.")

else:
    at_index = email.find("@")
    username = email[:at_index]
    domain = email[at_index + 1:]

    if not (domain.endswith(".com") or 
            domain.endswith(".edu") or 
            domain.endswith(".org")):
        print("Invalid email: domain must end with .com, .edu, or .org.")
    
    else:
        username = username.lower()
        username = username.replace("_", " ")
        username = username.replace(".", " ")

        print("Username:", username)
        print("Domain:", domain)
