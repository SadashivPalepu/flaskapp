import flask

app =flask.Flask(__name__)

@app.route("/")
def show():
    return 'welcome to flask'

@app.route("/user/<name>")
def show1(name):
    return f'<h1>welcome to {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
