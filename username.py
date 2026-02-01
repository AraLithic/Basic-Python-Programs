username=input("Enter your username of 12 alphabet, no digits and no space: ")
if len(username)==12 and username.isalpha()==True and username.find(" ")==-1:
    print(f"{username} username is valid")
else:
    print(f"{username} username is invalid ")