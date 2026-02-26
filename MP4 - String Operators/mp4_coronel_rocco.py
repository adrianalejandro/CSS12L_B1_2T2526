# Machine Problem #4: String Operators

# 1. Full Name Super Formatter (10 pts.)
fname = input("Enter your first name: ")
mname = input("Enter your middle name: ")
lname = input("Enter your last name: ")

fname = fname.strip().lower().capitalize()
mname = mname.strip().lower().capitalize()
lname = lname.strip().lower().capitalize()

mi = mname[:1].upper()

print("Formatted Name: " + lname + ", " + fname + " " + mi + ".")

# Word Pyramid (10 pts.)
word = input("Enter a word: ")
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    print(word * i)

# 3. Sentence Analyzer (10 pts.)
sentence = input("Enter a sentence: ")

total_characters = len(sentence)

words = sentence.split()
total_words = len(words)

vowels = "aeiouAEIOU"
total_vowels = 0

for char in sentence:
    if char in vowels:
        total_vowels += 1

print("Characters:", total_characters)
print("Words:", total_words)
print("Vowels:", total_vowels)

# 4. word = input("Enter a word: ")

reverse_word = ""

for i in range(len(word) - 1, -1, -1):
    reverse_word += word[i]

if word == reverse_word:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")

# 5. Shout Backwards (10 pts.)
text_input = input("Enter a phrase: ")

loud_text = text_input.upper()
backward_text = loud_text[::-1]

print("Output:", backward_text)

# 6. Email Validator and Username Formatter (30 pts.)
email = input("Enter your email address: ")

at = email.find("@")
dot = email.find(".")

if at != -1 and dot != -1:
    username = email[:at]
    
    username = username.lower()
    username = username.replace(".", " ")
    username = username.replace("_", " ")
    
    print("Your username is:", username)
else:
    print('Invalid email address. Please include "@" and a dot (.)')

# 7. Smart Email Analyzer (20 pts.)
email = input("Enter your email address: ")

if " " in email:
    print("Invalid email: must not contain spaces.")

elif email.count("@") != 1:
    print("Invalid email: missing '@' symbol.")

else:
    at = email.find("@")
    username = email[:at]
    domain = email[at + 1:]

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