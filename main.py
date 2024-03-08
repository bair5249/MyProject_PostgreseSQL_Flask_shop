import psycopg2
import ddatabase
import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename


app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = "C:/Users/79615/PycharmProjects/shop_site/static/images"
item = ddatabase.Item()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# item.close_db()
# item.clear_db()


def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/home')
def index():
    data = item.show_table()
    return render_template("index.html", data=data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/add_item', methods=['POST', 'GET'])
def add_item():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join("C:/Users/79615/PycharmProjects/shop_site/static/", filename))
        item_id = item.id_counter() + 1
        name = request.form['title']
        price = request.form['price']

        item.adding_item(item_id, name, price, filename)
        return redirect(request.url)
    else:
        return render_template("add_item.html")


if __name__ == '__main__':
    app.run(debug=True)
