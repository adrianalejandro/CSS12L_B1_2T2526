#1---------------------------------------------------------------------
def name():

	name = input("Enter your first name: ").strip().lower()
	na = name.capitalize()
	
	middle = input("Enter your middle name: ").strip().lower()
	mi = middle.capitalize()

	familyname = input("Enter your last name: ").strip().lower()
	fn = familyname.capitalize()

	Format = (f"Formatted Name: {fn}, {na} {mi[0]}.")
	print(Format)



#2---------------------------------------------------------------------
def pyramid():

	word = input("Enter a word: ").strip()
	num = int(input("Enter a number: "))

	for x in range(1, num + 1):
		
		print(word * x)

pyramid()



#3---------------------------------------------------------------------
def sen_ana():

	sentence = input("Enter a sentence: ").strip()

	char = len(sentence)
	print(f"Characters: {char}")
	
	words = len(sentence.split())
	print(f"Words: {words}")
	
	vowl = 0
	vow_s = "aeiouAEIOU"
	for x in sentence:
		if x in vow_s:
			vowl += 1

	print(f"Vowels: {vowl}")

sen_ana()



#4---------------------------------------------------------------------
def pal_det():

	word = input("Enter a word: ").strip().lower()
	reverse = word[::-1]

	if word == reverse:
		print("The word is a palindrome!")
	else:
		print("The word is not a palidrome :(.")

pal_det()



#5---------------------------------------------------------------------
def shout():

	scream = input("Enter a phrase: ").upper().strip()
	echo = scream[::-1]
	print(f"Output:{echo}")

shout()



#6---------------------------------------------------------------------
def email_val_user_fot():

	email = input("Enter your email address: ").strip().lower()

	at = email.find("@")
	do = email.find(".")

	if at != -1 and do != -1:
		username = email[:at]
		formuser = username.replace("_", " ").replace("-", " ").replace(".", " ")
	
		print(f"Your username is:{formuser}")

	else:
		print("Invalid email address. Please include @ and a dot (.)")

email_val_user_fot()



#7---------------------------------------------------------------------
def mails():

	gmail = input("Enter your email address: ")

	ats = gmail.find("@")

	if " " in gmail:
		print("Invalid email: Must not contains spaces")

	elif gmail.count("@") != 1:
		print("Invalid email: Must not contains more than one @ symbol")

	elif gmail.count("@") == 0:
		print("Invalid email: missing '@' symbol")

	elif not gmail.endswith(".com") or gmail.endswith(".edu") or gmail.endswith(".org"):
		print("Invalid email: domain must end with .com, .edu, or .org.")

	else:
		user = gmail[:ats]
		domain_expansion = gmail[ats + 1:]
		formuser = user.replace("_", " ").replace("-", " ").replace(".", " ").lower()

		print(f"Username:{user}") 
		print(f"Username:{domain_expansion}") 




mails()
