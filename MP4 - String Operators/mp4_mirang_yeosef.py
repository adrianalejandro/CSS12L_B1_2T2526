#1 Full name super formatter:

x = (input('Enter First Name:')).strip().capitalize()
y = (input('Enter Middle Name:')).strip().capitalize()[0]
z = (input('Enter Last Name:')).strip().capitalize()
 
print(f'\nFormatted name: {z}, {x} {y}.')

#2 Word pyramid:

x = input('Enter a word: ')
y = int(input('Enter a number: '))

print("\nOutput:")

for z in range(1, y + 1):
	print(x * z)

#3 Sentence analyzer:

x = input('Enter a sentence: ')
y = len(x)

a = x.split()
b = len(a)

vowel = "aeiouAEIOU"
vcount = 0

for e in x:
    if e in vowel:
        vcount += 1

print(f"\nCharacters: {y}")
print(f"Words: {b}")
print(f"Vowels: {vcount}")

#4 Palindrome detector:

x = input('Enter a word: ')
y = x.lower().strip()
z = y[::-1]

if y == z:
	print(f'\nThe word {x} is a palindrome!')

else:
	print(f'\nThe word {x} is not a palindrome.')

#5 Shout backwards:

x = input('Enter a phrase: ')
y = x.upper()[::-1]

print(f'\nOutput: {y}')

#6 Email validator and username formatter: 

email = input("Enter your email address: ")

if "@" in email and "." in email:
    x = email.find("@")
    username = email[:x]
    username = username.lower()
    username = username.replace(".", " ").replace("_", " ")
    print(f"Your username is: {username}")

else:
    print("Invalid email address. Please include \"@\" and a dot (.)")

#7 Smart email analyzer:

six7 = input("\nEnter your email address: ")


if six7.count("@") != 1:
    print("Invalid email: missing '@' symbol.")
elif " " in six7:
    print("Invalid email: contains space")
elif not (six7.endswith(".com") or six7.endswith(".edu") or six7.endswith(".org")):
    print("Invalid email: domain must end with .com, .edu, or .org.")
else:
    
    at_pos = six7.find("@")
    username7 = six7[:at_pos].lower().replace("_", " ").replace(".", " ")
    domain7 = six7[at_pos+1:]
    print("Username:", six7)
    print("Domain:", domain7)
