from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Devops Flask App!" 

@app.route('/api')
def api():
    data = {"name": "Asha","grade": "A"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    