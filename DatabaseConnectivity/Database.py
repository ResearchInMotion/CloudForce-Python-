import MySQLdb

db=MySQLdb.connect("localhost","root","root","maroon5")

cursor=db.cursor()

cursor.execute("SELECT VERSION()")

data=cursor.fetchone()

print("Databse version : %s" ,data)


db.close()