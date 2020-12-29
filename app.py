from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1><center>This is a Demo Flask Application</center></h1>'

app.run(host='0.0.0.0', port=5000)

