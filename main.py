from flask import Flask, url_for, render_template

app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)