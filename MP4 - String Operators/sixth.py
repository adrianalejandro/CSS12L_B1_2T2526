email = input("Enter your email address:\n")

if email.find("@") != -1 and email.find(".") != -1:
    at_position = email.find("@")
    username = email[:at_position]

    username = username.lower()
    username = username.replace(".", " ")
    username = username.replace("_", " ")

    print("Valid email address!")
    print("Formatted username:", username)
else:
    print("Invalid email address. Please enter a valid email.")