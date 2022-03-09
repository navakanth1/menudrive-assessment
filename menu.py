



while True:

    print("select an option to select")
    print("1. add on employee")
    print("2. search on employee")
    print("3. update an employee")
    print("4. delete an employee")
    print("5. exit")


    choice=int(input("Enter a choice"))
    if choice==1:
        print("select a option to add employee data")
    elif choice==2:
        print("select a option to update employee data")
    elif choice==3:
        print("select a option to search employee data")
    elif choice==4:
        print("select a option to delete employee data")
    elif choice==5:
        break
    else:
        print("invalid choice")