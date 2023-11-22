'''
Kuva API-kutsusta, joka tuottaa seuraavan tulosteen selaimeen. Ilman prooffausta:

from flask import Flask, Response
app = Flask(__name__) @app.route(' ') def summa( ):

# varsinainen koodi

if __name__ == '__main__': app.run(use_reloader=True, host=' ', port= )

Tuloste:
{
    "luku1: "17",
    "luku2: "41",
    "summa": 58
}
'''


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/summa')
def summa():
    # Simuloi API-parametrit
    luku1 = 17
    luku2 = 41

    # Tee laskenta
    summa = luku1 + luku2

    # Valmistele vastaus JSON-muodossa
    response_data = {
        "luku1": str(luku1),
        "luku2": str(luku2),
        "summa": summa
    }

    # Palauta vastaus JSON-muodossa
    return jsonify(response_data)

if __name__ == '__main__':
    # Käynnistä Flask-sovellus määritetyillä parametreilla
    app.run(use_reloader=True, host='0.0.0.0', port=5000)

