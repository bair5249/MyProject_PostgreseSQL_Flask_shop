import ddatabase
from flask import Flask, render_template, request, redirect


app = Flask(__name__)
item = ddatabase.Item()
# item.close_db()


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html", data=item.show_table())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/add_item', methods=['POST', 'GET'])
def add_item():
    if request.method == "POST":
        item_id = item.id_counter() + 1
        name = request.form['title']
        price = request.form['price']

        item.adding_item(item_id, name, price)
        return render_template("add_item.html")
    else:
        return render_template("add_item.html")


if __name__ == '__main__':
    app.run(debug=True)
