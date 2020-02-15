from flask import Flask

app = Flask(__name__)

@app.route('/<name>')

def index(name):
    body = '<h1>Hello World {}!</h1>'.format(name)
    body = body + '<p>This is the body after the header...<p>'
    body = body + '<b><u>and after that...</b></u>'
    body = body + '<p><b><ui>and then the line with italics</i></u>'
    return body