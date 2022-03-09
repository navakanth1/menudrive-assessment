while True:

    print("select an option from the menu")
    print("1. add 2 employee")
    print("2. subtract 2 employee")
    print("3. multiply 2 employee")
    print("4. divide 2 employee")
    print("5. exit")


    choice = int(input("select choice"))
    if choice==1:
        x = int(input("Enter 1st number"))
        y = int(input("Enter 2nd number"))
        z = x+y
        print(z)
    elif choice==2:
        x = int(input("Enter 1st number"))
        y = int(input("Enter 2nd number"))
        z = x - y
        print(z)
    elif choice==3:
        x = int(input("Enter 1st number"))
        y = int(input("Enter 2nd number"))
        z = x * y
        print(z)
    elif choice==4:
        x = int(input("Enter 1st number"))
        y = int(input("Enter 2nd number"))
        z = x%y
        print(z)
    elif choice==5:
        break
    else:
        print("invalid choice")





