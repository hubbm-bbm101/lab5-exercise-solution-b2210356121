email= str(input("email: "))
for x in email :
    if "@" in email :
        if "." in email :
            print("valid email")
            break
        else:
            print("invalid email")
    else:
        print("invalid email")