from flask import Flask


def hello_world():
    with open('index.html') as file:
      return file.read()

app = Flask(__name__)
app.add_url_rule('/', 'hello', hello_world)
app.run('0.0.0.0')
