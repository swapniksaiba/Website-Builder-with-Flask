from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "main content goes here"


@app.route('/about/')
def about():
    return "About content here!"


if __name__ == "__main__":
    app.run(debug=True)
