from psycopg2 import connect


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

    def show_table(self):
        self.cursor.execute("SELECT * FROM shop_table")
        data = self.cursor.fetchall()
        lst = []
        for row in data:
            column_dict = {"id": row[0], "name": row[1], "price": row[2], "isactive": row[3], "file": row[4]}
            lst.append(column_dict)
        return lst

    def adding_item(self, id, name, price, file):
        self.cursor.execute(f"INSERT INTO shop_table  values({id}, '{name}', {price}, True, '{file}')")

    def id_counter(self):
        self.cursor.execute("SELECT count(*) FROM shop_table")
        data = self.cursor.fetchall()[0][0]
        return data

    def clear_db(self):
        self.cursor.execute("DELETE FROM shop_table")




