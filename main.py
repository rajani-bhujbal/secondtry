from flask import Flask
app =Flask(__name__)


@app.route('/',methods=['GET',"POST"])
def index():
    return " <h2>This is my second demo </h2>"


if __name__='__main__':
    app.run()