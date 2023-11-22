'''
3. Määrittele muutamalla lauseella seuraavat teorioissa esillä olleet käsitteet

a) Luokka / Class:
Luokka (class) on Pythonin ohjelmointikielen peruskäsite, joka mahdollistaa objekti-orientoituneen ohjelmoinnin.
Luokka toimii mallina objektien luomiseen, joilla voi olla ominaisuuksia (attribuutteja) ja toiminnallisuuksia (metodeja).
Olio (object) on instanssi luokasta, ja se perii luokan määrittelemät ominaisuudet ja toiminnot.

b) Assosiaatio:
Assosiaatio viittaa objektien väliseen suhteeseen. Pythonissa se voisi tarkoittaa, että kahdella luokalla on jokin yhteys toisiinsa.
Assosiaatiot voivat olla yksisuuntaisia tai kaksisuuntaisia, ja ne voivat ilmentyä esimerkiksi,
kun yksi luokka käyttää toisen luokan ominaisuuksia tai kutsuu sen metodeja.

c) Päätepiste / Endpoint:
Päätepiste tarkoittaa yhtä tiettyä paikkaa ohjelmistossa, johon voi liittyä tietty toiminnallisuus tai resurssi.
Esimerkiksi web-sovelluksessa päätepiste voi olla tietty URL, joka vastaa tiettyyn HTTP-pyyntöön.
Päätepisteet ovat erityisen tärkeitä RESTful-APIssa, jossa kukin URL päätepiste vastaa tiettyä resurssia tai toimintoa.

d) Flask:
Flask on Pythonin web-kehys, joka helpottaa web-sovellusten kehittämistä.
Se on kevyt, joustava ja helppokäyttöinen, ja se perustuu Werkzeugin WSGI-työkalupakettiin ja Jinja2-templaatointimoottoriin.
Flask tarjoaa rakenteen web-sovellusten luomiseen ja mahdollistaa reitityksen, näkymien hallinnan, ja tiedonkäsittelyn.
Flask on suosittu erityisesti pienten ja keskisuurten projektien kehityksessä.


1. Luokka: Suunnitelma olioiden luomiseen. Se määrittelee joukon attribuutteja (muuttujia) ja metodeja (funktioita), joita oliot käyttävät.

2. Olio: Luokan instanssi. Oliot sisältävät attribuutteja (dataa) ja käyttäytymistä (metodeja).

3. Perintö: Luokan kyky periytyä attribuutteja ja metodeja toiselta luokalta.
Se edistää koodin uudelleenkäyttöä ja mahdollistaa uuden luokan luomisen olemassa olevan perusteella.

4. Kapselointi: Tietojen ja niihin liittyvien metodien niputtaminen yhteen yksikköön (luokka).
Se auttaa rajoittamaan pääsyä oliokomponentteihin.

5. Polymorfismi: Olioiden kyky ottaa useita muotoja.
Pythonissa polymorfia saavutetaan usein metodin ylikuormituksen tai ylikirjoituksen avulla.

6. Metodin Ylikuormitus: Useiden metodien määrittely samalla nimellä samassa luokassa, mutta eri parametreilla.
Python ei tue perinteistä metodin ylikuormitusta, mutta voit saavuttaa samanlaisia tuloksia käyttämällä oletusarvoja tai muuttuvan pituuden argumenttilistoja.

7. Metodin Ylikirjoitus: Erityisen toteutuksen tarjoaminen metodille alaluokassa, joka on jo määritelty sen yliluokassa.
Tämä mahdollistaa aliluokan tarjoavan erityisen toteutuksen jo olemassa olevalle metodille.

8. Abstraktio: Monimutkaisen todellisuuden piilottaminen ja paljastaminen vain välttämättömillä osilla.
OOP:ssa abstraktio saavutetaan usein abstraktien luokkien ja rajapintojen avulla.

9. Abstrakti Luokka: Luokka, jota ei voi instanssioida ja joka on tarkoitettu aliluokkien tekemiseen.
Se voi sisältää abstrakteja metodeja, jotka on toteutettava sen aliluokissa.

10. Rajapinta: Pythonissa rajapintoja ei ole määritelty nimenomaisesti, mutta käsite viittaa joukkoon metodeita, jotka luokan on toteutettava.
Se on tapa määritellä sopimus luokille.

11. Kompositio: Monimutkaisten olioiden rakentaminen yhdistämällä yksinkertaisempia oliota.
Se edistää "omistaa" -suhdetta sen sijaan, että olisi "on" -suhde (kuten perinnössä).

12. Getter- ja Setter-metodit: Metodeita, joita käytetään yksityisten attribuuttien arvojen hakemiseen ja asettamiseen,
tarjoten valvottua pääsyä luokan attribuutteihin.

'''