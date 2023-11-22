from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/summa')
def summa():
    # Simulate API parameters
    luku1 = 17
    luku2 = 41

    # Perform the calculation
    summa = luku1 + luku2

    # Prepare the response in JSON format
    response_data = {
        "luku1": str(luku1),
        "luku2": str(luku2),
        "summa": summa
    }

    # Return the response as JSON
    return jsonify(response_data)

if __name__ == '__main__':
    # Run the Flask application with specified parameters
    app.run(use_reloader=True, host='0.0.0.0', port=5000)
