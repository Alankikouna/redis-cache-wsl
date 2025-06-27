from flask import Flask, jsonify, render_template, request
import redis
import time

app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6380, decode_responses=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    key = request.form['key']
    value = cache.get(key)

    if value:
        source = "cache"
        message = f"✅ Donnée récupérée depuis le cache pour la clé « {key} »."
    else:
        time.sleep(2)
        value = f"Donnée générée pour « {key} »"
        cache.setex(key, 60, value)
        source = "slow_db"
        message = f"🕒 Donnée générée (cache mis à jour) pour la clé « {key} »."

    return render_template('index.html', key=key, value=value, source=source, message=message)

if __name__ == '__main__':
    app.run(debug=True)
