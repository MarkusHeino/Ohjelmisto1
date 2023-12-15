from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/kenttä/<string:icao>', methods=['GET'])
def get_airport_info(icao):
    # Tarkistaa onko annettu ICAO-koodi tietokannassa
    if icao in airport_database:
        airport_info = {
            "ICAO": icao,
            "Name": airport_database[icao]["Name"],
            "Municipality": airport_database[icao]["Municipality"]
        }
        return jsonify(airport_info)
    else:
        return jsonify({"error": "ICAO code not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
