import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
port = "3306",
database = "ardit700_pm1database"
)

cursor = con.cursor()
querry = cursor.execute('SELECT * FROM DICTIONARY ')
result = cursor.fetchall()
print(result)