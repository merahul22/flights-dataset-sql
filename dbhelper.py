import mysql.connector

class DB:
    def __init__(self, table_name='flights'):
        self.table_name = table_name
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='mydatabase',
            )
            self.mycursor = self.conn.cursor()
            print('✅ Connection established')
        except mysql.connector.Error as err:
            print(f'❌ Connection error: {err}')

    def fetch_city_names(self):
        city = []
        query = f"""
            SELECT DISTINCT Destination FROM {self.table_name}
            UNION
            SELECT DISTINCT Source FROM {self.table_name}
        """
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        city = [item[0] for item in data]
        return city

    def fetch_all_flights_df(self, source, destination):
        query = f"""
            SELECT * FROM {self.table_name}
            WHERE LOWER(TRIM(Source)) = LOWER(%s)
            AND LOWER(TRIM(Destination)) = LOWER(%s)
        """
        self.mycursor.execute(query, (source.strip(), destination.strip()))
        rows = self.mycursor.fetchall()
        columns = [col[0] for col in self.mycursor.description]
        return rows, columns

    def fetch_airline_frequency(self):
        self.mycursor.execute(f"""
            SELECT Airline, COUNT(*) FROM {self.table_name}
            GROUP BY Airline
        """)
        data = self.mycursor.fetchall()
        airline = [item[0] for item in data]
        frequency = [item[1] for item in data]
        return airline, frequency

    def busy_airport(self):
        city = []
        frequency = []
        self.mycursor.execute(f"""
            SELECT src, COUNT(*) AS freq FROM (
                SELECT Source AS src FROM {self.table_name}
                UNION ALL
                SELECT Destination AS src FROM {self.table_name}
            ) t
            GROUP BY src
            ORDER BY freq DESC
        """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city, frequency

    def daily_frequency(self):
        date = []
        frequency = []
        self.mycursor.execute(f"""
            SELECT Date_of_Journey, COUNT(*) FROM {self.table_name}
            GROUP BY Date_of_Journey
            ORDER BY Date_of_Journey
        """)
        data = self.mycursor.fetchall()
        for item in data:
            date.append(str(item[0]))  # Convert date to string if needed
            frequency.append(item[1])
        return date, frequency
