import sqlite3


class Database:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row

    def execute(self, query: str, params: tuple = (), fetchone=False, fetchall=False):
        with self.connection:
            cursor = self.connection.execute(query, params)
            if fetchone:
                return cursor.fetchone()
            if fetchall:
                return cursor.fetchall()

    def create_table_cocktails(self):
        self.execute("""CREATE TABLE cocktails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    photo_link TEXT,
    info TEXT,
    ingridients TEXT,
    method TEXT,
    glass TEXT
);""")

    def create_table_info(self):
        self.execute("""CREATE TABLE info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    photo_link TEXT,
    info TEXT,
    file_link TEXT,
);""")

    def create_table_cuisine(self):
        self.execute("""CREATE TABLE cuisine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    photo_link TEXT,
    description TEXT,
    info TEXT,
    extra_info TEXT,
);""")

    def create_table_salumeria(self):
        self.execute("""CREATE TABLE salumeria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    photo_link TEXT,
    description TEXT,
    info TEXT,
    extra_info TEXT,
);""")


    def create_table_wine(self):
        self.execute("""CREATE TABLE salumeria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    photo_link TEXT,
    vintage TEXT,
    country TEXT,
    includes TEXT,
    price TEXT,
    about TEXT,
    taste TEXT
);""")
