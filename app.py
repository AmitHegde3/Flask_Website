from flask import Flask, render_template, jsonify  #Flask is the class whereas flask is the module
from database import li
app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': "DBMS Project",
  'time': "22hrs",
  'slaray': 'Rs 12,00,000'
}, {
  'id': 2,
  'title': "FRPS Project",
  'time': "10hrs",
}, {
  'id': 3,
  'title': "Reserach paper",
  'time': "122hrs",
  'slaray': 'Rs 24,60,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=li, framework_name="Flask")


@app.route('/api/jobs')
def list_jobs():
  return jsonify(li)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
