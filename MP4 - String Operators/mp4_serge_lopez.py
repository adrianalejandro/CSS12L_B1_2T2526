first_name = input("Enter your first name: ").strip()
middle_name = input("Enter your middle name: ").strip()
last_name = input("Enter your last name: ").strip()

first_name = first_name.capitalize()
middle_initial = middle_name[0].capitalize()
last_name = last_name.capitalize()

print(f"Formatted Name: {last_name}, {first_name} {middle_initial}.")

word = input("Enter a word: ")
number = int(input("Enter a number: "))

print("Output:")
for i in range(1, number + 1):
    print(word * i)

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
