import sqlite3 as sql

connection = sql.connect("Sellar.db")
# connection.execute(''' CREATE TABLE MOBILEPHONE(
#                          ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                          MOBILE_PHONE TEXT,
#                          BRAND_NAME TEXT,
#                          SERIAL_NO INTEGER,
#                          YEAR INTEGER,
#                          MONTH INTEGER,
#                          PRICE INTEGER
#
#
#
# ); ''')
print("table created successfully")


getmobile = input("Enter new mobile: ")
getbrand = input("Enter new brand: ")
getserial = input("Enter new serial: ")
getyear = input("Enter new year: ")
getmonth = input("Enter new month: ")

connection.execute("INSERT INTO MOBILEPHONE(MOBILE_PHONE,BRAND_NAME,SERIAL_NO,YEAR,MONTH) \
 VALUES ('"+getmobile+"','"+getbrand+"',"+getserial+","+getyear+","+getmonth+")")


connection.commit()
connection.close()
print("Inserted successfully")