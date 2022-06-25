from flask import Flask
app = Flask(__name__)


@app.route('/')
def Zertifizierungen():
    return 'Hello Pexonian, trage hier deine Zertifizierungen ein!'

if __name__ == '__main__':
    app.run()