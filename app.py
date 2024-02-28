import flask

app =flask.Flask(__name__)

@app.route("/")
def show():
    return 'welcome to flask'
    
if __name__ == '__main__':
    app.run()
