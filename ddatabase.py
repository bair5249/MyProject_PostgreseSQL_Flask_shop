import os

from shutil import rmtree
from psycopg2 import connect
from jinja2 import Environment, FileSystemLoader


class Item:
    def __init__(self):
        try:
            self.conn = connect(dbname="flaskPython", host="localhost", user="postgres", password="993", port="5432")
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("Ошибка при подключении", e)

    def close_db(self):
        self.cursor.close()
        self.conn.close()
        print("Соединение закрыто")

    def show_table(self):  # Возвращает список словарей
        self.cursor.execute("SELECT * FROM shop_table")
        data = self.cursor.fetchall()
        lst = []
        for row in data:
            column_dict = {"id": row[0], "name": row[1], "price": row[2], "isactive": row[3], "file": row[4]}
            lst.append(column_dict)
        return lst

    def adding_item(self, id, name, price, filename):
        self.cursor.execute(f"INSERT INTO shop_table  values({id}, '{name}', {price}, True, '{filename}')")
        self.creating_details(id, name, price, filename)

        # try:
        #     self.cursor.execute(f"INSERT INTO shop_table  values({id}, '{name}', {price}, True, '{filename}')")
        #     self.creating_details(id, name, price, filename)
        # except Exception as e:
        #     print(e)
        #     self.clear_db()
        #     folder = 'C:/Users/79615/PycharmProjects/shop_site/static'
        #     for filename in os.listdir(folder):
        #         file_path = os.path.join(folder, filename)
        #         if os.path.isfile(file_path) or os.path.islink(file_path):
        #             os.unlink(file_path)
        #         elif os.path.isdir(file_path):
        #             rmtree(file_path)

    def id_counter(self):
        self.cursor.execute("SELECT count(*) FROM shop_table")
        data = self.cursor.fetchall()[0][0]
        return data

    def clear_db(self):
        self.cursor.execute("DELETE FROM shop_table")

    def creating_details(self, id, name, price, filename):
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("details_page.html")
        filename_html = f"details_page_{str(id)}.html"
        content = template.render(
            id=id,
            name=name,
            price=price,
            isactive=True,
            filename=filename
        )
        with open(f"templates/{filename_html}", mode="w", encoding="utf-8") as new_page:
            new_page.write(content)
