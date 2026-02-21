number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))
sum = number1 + number2
difference = number1 - number2
product = number1 * number2
if number2 != 0:
quotient = number1 / number2
else:
quotient = "The number you input cannot be divided to zero."
print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")