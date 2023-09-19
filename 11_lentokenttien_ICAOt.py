# Create a SQLite database (you can replace this with your own database connection)
import = mysql.connect('airports.db')
cursor = conn.cursor()

#Luo taulu lentokenttätiedoilla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS airports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        icao_code TEXT NOT NULL,
        name TEXT NOT NULL,
        ident_bracket TEXT NOT NULL
    )
''')

#Laita tauluun lisätieto
cursor.executemany('''
    INSERT INTO airports (icao_code, name, ident_bracket)
    VALUES (?, ?, ?)
''', [
    ('KJFK', 'John F. Kennedy International Airport', 'JFK'),
    ('EFAH', 'Ammasuo Lentokenttä', 'OUL'),
    ('EGLL', 'Heathrow Airport', 'LHR'),
])

#Commit ja tietokantayhteyden sulku

conn.commit()
conn.close()

#Funktio jolla haetaan ICAO-koodi tietokannasta
def get_airport_info(icao_code):
    conn = mysql.connect('airports.db')
    cursor = conn.cursor()

    cursor.execute('SELECT name, ident_bracket FROM airports WHERE icao_code = ?', (icao_code,))
    result = cursor.fetchone()

    conn.close()

    return result

#Pääohjelma

while True:
    icao_code = input('Anna lentokentän ICAO-koodi: ').strip().upper()

    if icao_code == '':
        break

    airport_info = get_airport_info(icao_code)

    if airport_info:
        name, ident_bracket = airport_info
        print(f'Lentokentän nimi: {name}')
        print(f'ident-sarake: {ident_bracket}')
    else:
        print('Ei löydy lentokenttää. Anna ICAO-koodi tai paina Enter poistuaksesi.')

print('Hei hei!')
