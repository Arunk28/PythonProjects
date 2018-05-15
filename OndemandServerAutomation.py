import pyodbc

user ="sa"
pwd="123456789"
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=SCS-AIO-18\SCSSQLSRVR;"
                      "Database=DbUtil;"
                      'uid='+user+';pwd='+pwd)

# Trusted_Connection=yes;"
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Users where emailid = 'arun@syscloud.com'")
tables  = cursor.fetchall()
for row in tables:
    print (row.emailid)