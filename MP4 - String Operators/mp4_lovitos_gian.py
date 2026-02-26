#1. Full Name Super Formatter
def name():
    x = input("Enter your first name: ")
    y = input("Enter your middle name: ")
    z = input("Enter your last name: ")

    first = x.lower().title().strip()
    middle = y.lower().capitalize()[0]
    last = z.lower().capitalize().strip()

    print(f"Your formated name is: {last}, {first} {middle}.")
 
name()

#2. Word Pyramid:

Random = input("Enter a word: ")

Number = int(input("Enter a number: "))

print("\nOutput:")

for i in range(1, Number + 1):

    print(Random * i)

#3. Sentence Analyzer:

sentence = input("Enter a sentence:")

char_numbers = len(sentence)

words_list = sentence.split()
word_numbers = len(words_list)

vowels_numbers = 0
vowels = "aeiouAEIOU"

for char in sentence:
    if char in vowels:
        vowels_numbers = vowels_numbers + 1

print("\nCharacters:", char_numbers)
print("Words:", word_numbers)
print("Vowels:", vowels_numbers)

#4. Palindrome Detector:

word = input("Enter a word: ")

reverse = word[::-1]

if word == reverse:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")

#5. Shout Backwards:

phrase = input("Enter a phrase: ")

Upper_Case = phrase.upper()

backwards = Upper_Case[::-1]

print("Output:", backwards)

#6. Email Validator and Username Formatter:

email = input("Enter your email address: ")

if "@" in email and "." in email:

        index = email.find("@")

        username = email[:index]

        username = username.lower()
        username = username.replace(".", " ")
        username = username.replace("_", " ")

        print("Your username is:", username)

else:
    print("Invalid email address. Please include \"@\" and a dot (.).")

#7. Smart Email Analyzer:

email = input("Enter your email address: ")

if " " in email:
    print("Invalid email: contains space.")

elif email.count("@") != 1:
    print("Invalid email: missing '@' symbol.")

else:
    index = email.find("@")

    username = email[:index]
    domain = email[index + 1:]

    if not (domain.endswith(".com") or domain.endswith(".edu") or domain.endswith(".org")): 
        print("Invalid email: domain must end with .com, .edu, or .org.")

    else:
        clean_username = username.lower()
        clean_username = clean_username.replace("_"," ")
        clean_username = clean_username.replace("."," ")

        print("Username:", clean_username)
        print("Domain:", domain)