import mysql.connector
import csv
# i created this file just to push import file to dbms as  phpadmin gui needed more time to define column
# Step 1: Connect to MySQL (XAMPP must be running)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",         # No password by default for XAMPP
    database="mydatabase"  # Make sure this database exists in phpMyAdmin
)

cursor = conn.cursor()

# Step 2: Create the table with correct columns
create_table = """
CREATE TABLE IF NOT EXISTS flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Airline VARCHAR(50),
    Date_of_Journey DATE,
    Source VARCHAR(30),
    Destination VARCHAR(30),
    Route TEXT,
    Dep_Time TIME,
    Duration INT,
    Total_Stops VARCHAR(20),
    Price INT
)
"""
cursor.execute(create_table)

# Step 3: Prepare insert query
insert_query = """
INSERT INTO flights (
    Airline, Date_of_Journey, Source, Destination, Route, Dep_Time, Duration, Total_Stops, Price
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Step 4: Read CSV and insert data
with open("flights.csv", newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        # Clean and convert if needed
        # Convert duration to integer safely
        row[6] = int(row[6])  # Duration
        row[5] = row[5] + ":00" if len(row[5].split(":")) == 2 else row[5]  # Ensure Dep_Time is HH:MM:SS
        cursor.execute(insert_query, row)

conn.commit()
print("✅ All rows inserted successfully.")

# Step 5: Close connections
cursor.close()
conn.close()
