#1
fname = input("Enter your first name: ").strip().capitalize()
mname = input("Enter your middle name: ").strip().capitalize()
lname = input("Enter your last name: ").strip().capitalize()


print("Formatted Name: " + lname + ", " + fname + " " + mname[0] + ".")

#2
word = input("\nEnter a word: ")
n = int(input("Enter a number: "))
print("Output:")
for i in range(1, n + 1):
    print(word * i)

#3 
sentence = input("\nEnter a sentence: ")
chars = len(sentence)
words = len(sentence.split())
vowels = sum(1 for char in sentence.lower() if char in "aeiou")

print(f"Characters: {chars}")
print(f"Words: {words}")
print(f"Vowels: {vowels}")

#4
word_pal = input("\nEnter a word: ").lower()
if word_pal == word_pal[::-1]:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")

#5
phrase = input("\nEnter a phrase: ")
print(f"Output: {phrase.upper()[::-1]}")

#6
email = input("\nEnter your email address: ")
if "@" in email_v and "." in email:
    username = email.split("@")[0].lower().replace("_", " ").replace(".", " ")
    print(f"Your username is: {username}")
else:
    print("Invalid email address. Please include \"@\" and a dot (.)")

#7
email5 = input("\nEnter your email address: ")


if email5.count("@") != 1:
    print("Invalid email: missing '@' symbol.")
elif " " in email5:
    print("Invalid email: contains space")
elif not (email5.endswith(".com") or email5.endswith(".edu") or email5.endswith(".org")):
    print("Invalid email: domain must end with .com, .edu, or .org.")
else:
    
    at_pos = email5.find("@")
    username7 = email5[:at_pos].lower().replace("_", " ").replace(".", " ")
    domain7 = email5[at_pos+1:]
    print("Username:", username5)
    print("Domain:", domain5)
