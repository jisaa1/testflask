from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, World!")

@app.route('/api/data')
def get_data():
    data = {"name": "Jisa", "age": 36}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
