import  getpass

username = "kyla05"
password = 'SECRETHAHAHA'

u = input("Enter username -->")
p = getpass.getpass("Input password ==>")

if username == u and password == p :
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")