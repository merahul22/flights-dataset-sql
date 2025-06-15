import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mydatabase"
)

cursor = conn.cursor()

# create_table = """
# CREATE TABLE IF NOT EXISTS airport (
#     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(20) NOT NULL,
#     city VARCHAR(20) NOT NULL,
#     code VARCHAR(10) NOT NULL
# )
# """
insert_table = """
  INSERT INTO airport VALUES
    (1,'DEL','New Delhi','IGIA'),
    (2,'CCU','Kolkata','NSCA'),
    (3,'BOM','Mumbai','CSMA')
"""
# cursor.execute(create_table)
cursor.execute(insert_table)
cursor.execute("SELECT * FROM airport WHERE id > 1")
data=cursor.fetchall()
print(data)
# print("Table 'airport' created successfully.")
upadte_table = """
UPDATE airport 
SET name='BOMBAY'
WHERE id=3
"""
cursor.execute(upadte_table)
cursor.execute("SELECT * FROM airport WHERE id > 1")
data=cursor.fetchall()
print(data)
cursor.execute("DELETE FROM airport WHERE id = 3")
conn.commit()
cursor.execute("SELECT * FROM airport")
print(cursor.fetchall())
cursor.close()
conn.close()
