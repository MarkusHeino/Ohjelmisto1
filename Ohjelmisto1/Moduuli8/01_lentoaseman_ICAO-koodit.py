import mysql.connector
import SQLconfig

def haeLentokentanicao(icao):
    sql = "SELECT ident, airport, mumicipality FROM ident= {icao}"
    sql += " ICAO='" + icao + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

# Pääohjelma
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user= SQLconfig.user,
         password= SQLconfig.password,
         autocommit=True
         )

icao = input("Anna ICAO: ")
haeLentokentanicao(icao)
