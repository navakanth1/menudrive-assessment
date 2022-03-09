import sqlite3 as sql
connection = sql.connect("Sellar.db")
listoftables=connection.execute("SELECT mobile_phone from sqlite_master type'tablr' AND mobile_phone='SELLAR' ")
if listoftables!=[]:
    print("Table already there! ")
else:
    connection.execute(''' CREATE TABLE MOBILEPHONE(
                             ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             MOBILE_PHONE TEXT,
                             BRAND_NAME TEXT,
                             SERIAL_NO INTEGER,
                             YEAR INTEGER,
                             MONTH INTEGER,
                             PRICE INTEGER



    ); ''')
    print("table created successfully")

while True:
    print(" select a choice from the sellar")
    print("1. add a mobile")
    print("2. view all mobiles")
    print("3. find serial number")
    print("4. update mobile")
    print("5. delete mobile")
    print("6. exit")



    choice=int(input("Enter a choice"))
    if choice==1:
        getname = input("Enter  new mobile: ")
        getBrand = input("Enter new Brand: ")
        getserial = input("Enter Serial Number: ")
        getyear = input("Enter new Year: ")
        getmonth = input("Enter new Month: ")
        getPrice = input("Enter  new Price: ")


        connection.execute(" INSERT INTO MOBILEPHONE(MOBILE_PHONE, BRAND_NAME, BRAND_NAME,  SERIAL_NO, YEAR, MONTH, PRICE)\
        VALUES('"+ getname +"','" + getbrand + "'," + getserial + "," + getyear + ",\
            " + getmonth + "," + getprice + ")")
        connection.commit()
        print("Inserted Successfully")

    elif choice==2:

        result = connection.execute("SELECT * FROM MOBILEPHONE")

        for i in result:
            print("Id: ", i[0])
            print("mobile name: ", i[1])
            print("brand name", i[2])
            print("serial no: ", i[3])
            print("Year: ", i[4])
            print("Month: ", i[5])
            print("Price: ", i[6])
    elif choice == 3:
        getserialnumber = input("Enter Serial number: ")

        result = connection.execute("SELECT * FROM MOBILEPHONE WHERE SERIAL_NO=" + getserialnumber)

        for i in result:
            print("Id: ", i[0])
            print("mobilename: ", i[1])
            print("brand name: ", i[2])
            print("serial no: ", i[3])
            print("Year: ", i[4])
            print("Month: ", i[5])
            print("Price: ", i[6])

    elif choice==4:
        getSerialnumber = input("Enter Serial number: ")

        getnewserialnumber= input("Enter New Serial Number: ")
        getnewname = input("Enter New Model Name: ")
        getNewbrand = input("Enter New Brand: ")
        getnewuyear = input("Enter New Manufacture Year: ")
        getnewmonth = input("Enter New Manufacture Month: ")
        getnewprice = input("Enter New Price: ")

        result = connection.execute(" UPDATE MOBILLEPHONE SET SERIAL_NUMBER=" + getnewserialnumber + ", MOBILE_NAME='" + getnewname + "', \
                BRAND_NAME='" + getnewbrand + "', YEAR=" + getnewyear + ", MONTH='" + getnewmonth + "',\
                PRICE=" + getnewprice + " WHERE SERIAL_NUMBER=" + getserialnumber)
        connection.commit()
        print("Updated Successfully")

    elif choice == 5:
        getserialnumber = input("Enter new Serial number: ")

        result = connection.execute("DELETE FROM MOBILEPHONE WHERE SERIAL_NUMBER=" + getserialnumber)
        connection.commit()
        print("Deleted Successfully")

    elif choice == 6:
        connection.close()
        break

    else:
        print("Invalid Option")
