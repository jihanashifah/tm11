from flask import Flask, request, jsonify
import random

app = Flask(__name__)

messages = [
    "Makan patty itu SpongeBob.",
    "Berdansalah, Patrick.",
    "Makan patty itu SpongeBob.",
    "Berdansalah, Patrick.",
    "Hari ini hoki, Squidward.",
    "Jangan marah, Krabby Patty datang lagi.",
    "Kamu seperti Gary, selalu setia.",
    "Patrick, itu bukan bintang laut sungguhan.",
    "Krabby Patty lebih enak dari Chum Bucket.",
    "Kamu mirip Plankton, selalu merencanakan sesuatu.",
    "Sandy selalu siap untuk petualangan.",
    "Bikini Bottom adalah tempat terbaik di dunia."
]

@app.route('/puja_kerang_ajaib', methods=['GET', 'POST'])
def puja_kerang_ajaib():
    if request.method == 'GET':
        name = request.args.get('nama')
        if name:
            message = f"{name}, {random.choice(messages)}"
        else:
            message = random.choice(messages)
        return jsonify({"message": message})

    elif request.method == 'POST':
        name = request.form.get('nama')
        if name:
            message = f"Selamat datang, {name}, anda berhasil masuk ke Puja Kerang Ajaib"
            return jsonify({"message": message})
        else:
            return jsonify({"error": "Nama harus disertakan dalam POST request"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
