import mysql.connector
import configparser

def hae_kentta_icao_koodilla:

    return

#pääohjalema

yhteys = mysql.connector.connect(
         host='127.0.0.1',  #localhost
         port= 3306,
         database='flight_game',
         user='config:user',
         password='config.pwd',
         autocommit=True
         )

icao = input("Anna kentän ICAO-koodi: ")



