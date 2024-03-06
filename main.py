from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/add_item', methods=['POST', 'GET'])
def add_item():
    return render_template("add_item.html")


if __name__ == '__main__':
    app.run(debug=True)
