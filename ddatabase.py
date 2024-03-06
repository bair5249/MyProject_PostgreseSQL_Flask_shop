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
        return data



