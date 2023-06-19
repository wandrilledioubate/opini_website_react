from flask import Flask, request, jsonify
import random

app = Flask(__name__)

mots_positifs = ["pas cher", "joli", "personnel accueillant"]
mots_negatifs = ["trop cher", "pas beau", "personnel desagreable"]

@app.route('/randomize', methods=['POST'])
def randomize():
    data = request.get_json()
    url = data.get('url')
    
    if url:
        random_number = random.randint(1, 100)
        mots_choisis_positifs = random.sample(mots_positifs, 3)
        mots_choisis_negatifs = random.sample(mots_negatifs, 3)
        return jsonify({
            'url': url,
            'random_number': random_number,
            'mots_positifs': mots_choisis_positifs,
            'mots_negatifs': mots_choisis_negatifs
        }), 200
    else:
        return jsonify({"error": "Missing url"}), 400

if __name__ == "__main__":
    app.run(debug=True)
