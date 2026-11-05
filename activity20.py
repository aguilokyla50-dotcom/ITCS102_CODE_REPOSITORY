from getpass import getpass

u = "kyla05"
p = "123456789"

isLogin = False

while isLogin == False:

    user = input("WHAT IS YOUR USERNAME-->")
    pword = getpass("PLEASE ENTER YOUR PASSWORD-->")

    if user == u and pword == p:
        print("LOGIN SUCCESSFULLY")
        isLogin = True
    else:
        print("ACCESS DENIED")
        isLogin == False