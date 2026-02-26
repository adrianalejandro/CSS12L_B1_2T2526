# Word Pyramid

word = input("Enter a word:\n")
number = int(input("Enter a number:\n"))

print("Output:")
for i in range(1, number + 1):
    print(word * i)