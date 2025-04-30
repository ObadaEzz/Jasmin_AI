from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"name": "Sarah AlAli", "age": 20, "major": "Software Engineering"},
    {"name": "Yasser Mansour", "age": 22, "major": "Computer Science"},
    {"name": "Jana Khaled", "age": 21, "major": "Artificial Intelligence"},
    {"name": "Raed Zahran", "age": 23, "major": "Cybersecurity"},
    {"name": "Dalia Fahad", "age": 24, "major": "Network Engineering"},
]

@app.route('/', methods=['GET'])
@app.route('/students', methods=['GET'])
def get_students():
    return render_template("students.html", students=students)

if __name__ == '__main__':
    app.run(debug=True)
