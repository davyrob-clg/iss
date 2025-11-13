

import sqlite3

# **Step 1: Connect to SQLite Database (or create it if it doesn't exist)**
conn = sqlite3.connect('iss_data.db')
cursor = conn.cursor()

# **Step 2: Create a table to store latitude and longitude**
cursor.execute('''
CREATE TABLE IF NOT EXISTS gps_coordinates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# **Step 3: Function to insert latitude and longitude into the table**
def insert_coordinates(lat, lon):
    cursor.execute('''
    INSERT INTO gps_coordinates (latitude, longitude)
    VALUES (?, ?)
    ''', (lat, lon))
    conn.commit()

# **Step 4: Example usage**
# Replace these with actual GPS coordinates
latitude = 36.1408
longitude = -5.3536

insert_coordinates(latitude, longitude)

print("Coordinates inserted successfully!")

# **Step 5: Close the connection**
conn.close()
