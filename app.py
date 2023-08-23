from flask import Flask, render_template, jsonify,request #Flask is the class whereas flask is the module
from database import li,add_todo_db
app = Flask(__name__)

# JOBS = [{
#   'id': 1,
#   'title': "DBMS Project",
#   'time': "22hrs",
#   'slaray': 'Rs 12,00,000'
# }, {
#   'id': 2,
#   'title': "FRPS Project",
#   'time': "10hrs",
# }, {
#   'id': 3,
#   'title': "Reserach paper",
#   'time': "122hrs",
#   'slaray': 'Rs 24,60,000'
# }]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=li, framework_name="Flask")


@app.route('/api/jobs')
def list_jobs():
  return jsonify(li)

# @app.route('/todo/<id>')

# def show_todo(id):
#   todo = li

#For the form
@app.route('/todo/apply',methods=['post'])

def form_apply():
  data = request.form
  add_todo_db(data.to_dict())
  return render_template('submitted.html',data=data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
