import pyodbc

user ="sa"
pwd="123456789"
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SCS-AIO-18\SCSSQLSRVR;"
                      "Database=DbUtil;"
                      'uid='+user+';pwd='+pwd)

# Trusted_Connection=yes;"
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Users")
tables  = cursor.fetchall()
add =[]
for row in tables:
   add.append(row.emailid)

print(add)