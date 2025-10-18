from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Devops Flask App!" 

@app.route('/api')
def api():
    data = {"name": "Asha","grade": "A"}
    return jsonify(data)

@app.route("/todo")
def todo_page():
    return render_template("todo.html")

if __name__ == '__main__':
    app.run(debug=True)
    