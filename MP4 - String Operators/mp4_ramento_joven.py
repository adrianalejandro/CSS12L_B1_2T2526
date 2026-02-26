#1
def name():
    x = input("Enter your first name: ")
    y = input("Enter your middle name: ")
    z = input("Enter your last name: ")
  
    first = x.strip().capitalize()
    middle = y.strip().capitalize()
    last = z.strip().capitalize()
    
print("Formatted Name: " + last + ", " + first + " " + middle[0] + ".")

#2
def pyramid():
    word = input("Enter a word: ")
    number = int(input("Enter a number: "))

    for w in range(1, number + 1):
        print(word * w)

#3
def sentence_analyzer():
    text = input("Enter a sentence: ")
    chars = len(text)
    words = len(text.split())
    
    vowels = "aeiouAEIOU"
    v_count = 0
    for char in text:
        if char in vowels:
            v_count += 1
            
    print("Characters: " + str(chars))
    print("Words: " + str(words))
    print("Vowels: " + str(v_count))

#4
def palindrome():
    word = input("Enter a word: ").lower()
    reversed_word = word[::-1]
    
    if word == reversed_word:
        print("The word is a palindrome!")
    else:
        print("Not a palindrome.")

#5
def shout():
    phrase = input("Enter a phrase: ")
    output = phrase.upper()[::-1]
    print("Output: " + output)

#6
def check_email():
    address = input("Enter your email address: ")

    if "@" in address and "." in address:

        at_index = address.find("@")
        username = address[:at_index].lower().replace(".", " ").replace("_", " ")
        print("Your username is: " + username)
    else:
        print("Invalid email address. Please include '@' and a dot (.)")

#7
def gmail():
    email = input("Enter your email address: ").lower()

    if "@gmail.com" in email:
        username = email.split("@")[0]
        print("Hello, " + username + "! You are using a Google account.")
    else:
        print("This is not a Gmail address.")
        
name()


