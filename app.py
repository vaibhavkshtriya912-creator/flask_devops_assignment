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

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json(silent=True) or request.form
    n, d = data.get("itemName"), data.get("itemDescription")
    if not n or not d:
        return jsonify({"error": "itemName and itemDescription required"}), 400
    todos.insert_one({"itemName": n, "itemDescription": d})
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True)
    