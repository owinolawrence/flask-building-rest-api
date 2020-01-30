from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Lawrence"

tasks = [
    {
        "id": 1,
        "title":u'Books',
        "description" :u'Chem, Bio, Math, Buss',
        "done":False
    }


    {
        "id":2,
        "title": u'Github',
        "description":u'This is the platform where you can callaborate with other developers',
        "done": False
    }
]

@app.route('/todo/api/v1.0/tasks' , methods=["GET"])
def get_tasks():
    return jsonify({'tasks':tasks})

if __name__ == "__main__":
    app.run(debug=True)