from flask import Flask, url_for, render_template

from Allergieausweis import allergie

app = Flask(__name__)

persons = allergie.create_uswiise(4)

@app.route('/')
def hello_world():
    return render_template('main.html', person=persons[0])

if __name__ == '__main__':
    app.run(threaded=True, port=5000)