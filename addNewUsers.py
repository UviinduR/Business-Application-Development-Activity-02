import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Publication"

)
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("USE Publication")
sql = "INSERT INTO Writer (writer_id, name, NIC, contact, address) VALUES (%s, %s, %s, %s, %s)"
val = ("W001", "Bishayn", "2005909090", "0772729729", "10, Hedges Court")
mycursor.execute(sql, val)

mydb.commit()