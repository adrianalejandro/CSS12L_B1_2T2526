sentence = input("Enter a sentence:\n")

characters = len(sentence)
words = len(sentence.split())

vowels = 0
for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1

print("Characters:", characters)
print("Words:", words)
print("Vowels:", vowels)