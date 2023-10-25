import mysql.connector
import configparser

def hae_kentta_icao_koodilla(icao):
    sql = SELECT ident, name, municipality FROM airport Where ident= {icao}
    print(sql)
    kursori = yhteys.cursor
    kursori.execute(sql)
    tulos = kursori:fetchall() fetchone() #fetchall
    return tulos

#pääohjelma

yhteys = mysql.connector.connect(
         host='127.0.0.1', #localhost
         port= 3306,
         database='flight_game',
         user= "config:user",
         password='config.pwd',
         autocommit=True
         )

icao = input("Anna kentän ICAO-koodi: ")
kenttä = haet_kenttä_icao_koodilla(icao)
print(kenttä)
print(f"Kentän nimi:{kenttä[0][1]}, sijainti kunnassa {kenttä[0][2]}")
