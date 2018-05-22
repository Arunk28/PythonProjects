import pyodbc

user ="sa"
pwd="123456789"
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SCS-AIO-18\SCSSQLSRVR;"
                      "Database=DbUtil;"
                      'uid='+user+';pwd='+pwd)


# Trusted_Connection=yes;"
cursor = cnxn.cursor()

cursor.execute("exec py_test")
# cursor.execute("SELECT * FROM Users")
tables  = cursor.fetchall()

add =[]
for row in tables:
   add.append([row.id,row.emailid])

print(add)
input("\n\nPress the enter key to exit.")