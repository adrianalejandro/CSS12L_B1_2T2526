word = input("Enter a word:\n")

if word == word[::-1]:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")