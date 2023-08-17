from flask import Flask #Flask is the class whereas flask is the module

app = Flask(__name__)

@app.route("/")

def hello_world():
  return "HELLO World!..Testing"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)