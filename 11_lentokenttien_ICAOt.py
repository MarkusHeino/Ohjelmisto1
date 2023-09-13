import mysql

# Create a SQLite database (you can replace this with your own database connection)
conn = sqlite3.connect('airports.db')
cursor = conn.cursor()

# Create a table to store airport information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS airports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        icao_code TEXT NOT NULL,
        name TEXT NOT NULL,
        ident_bracket TEXT NOT NULL
    )
''')

# Insert sample data into the table
cursor.executemany('''
    INSERT INTO airports (icao_code, name, ident_bracket)
    VALUES (?, ?, ?)
''', [
    ('KJFK', 'John F. Kennedy International Airport', 'JFK'),
    ('KLAX', 'Los Angeles International Airport', 'LAX'),
    ('EGLL', 'Heathrow Airport', 'LHR'),
])

# Commit changes and close the database connection
conn.commit()
conn.close()

# Function to fetch airport information by ICAO code
def get_airport_info(icao_code):
    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()

    cursor.execute('SELECT name, ident_bracket FROM airports WHERE icao_code = ?', (icao_code,))
    result = cursor.fetchone()

    conn.close()

    return result

# Main program
while True:
    icao_code = input('Enter the ICAO code of the airport (e.g., KJFK): ').strip().upper()

    if icao_code == 'QUIT':
        break

    airport_info = get_airport_info(icao_code)

    if airport_info:
        name, ident_bracket = airport_info
        print(f'Airport Name: {name}')
        print(f'Ident-Bracket: {ident_bracket}')
    else:
        print('Airport not found. Please enter a valid ICAO code or type QUIT to exit.')

print('Goodbye!')
