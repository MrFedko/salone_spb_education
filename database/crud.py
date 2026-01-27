import sqlite3


class Database:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.scheme_tables = {
            "cocktails": ("category", "name", "photo_link", "info", "ingridients", "method", "glass"),
            "info": ("category", "name", "photo_link", "info", "file_link"),
            "cuisine": ("category", "name", "photo_link", "description", "info", "extra_info"),
            "salumeria": ("category", "name", "photo_link", "description", "info", "extra_info"),
            "wine": ("category", "name", "photo_link", "vintage", "country", "includes", "price", "about", "taste"),
        }

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
    file_link TEXT
);""")

    def create_table_cuisine(self):
        self.execute("""CREATE TABLE cuisine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    photo_link TEXT,
    description TEXT,
    info TEXT,
    extra_info TEXT
);""")

    def create_table_salumeria(self):
        self.execute("""CREATE TABLE salumeria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    name TEXT NOT NULL,
    photo_link TEXT,
    description TEXT,
    info TEXT,
    extra_info TEXT
);""")


    def create_table_wine(self):
        self.execute("""CREATE TABLE wine (
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

    def insert_row(self, table: str, row: list):
        row = [x.strip() if isinstance(x, str) else x for x in row]
        placeholders = ', '.join(['?'] * len(row))
        table_names = self.scheme_tables[table]
        query = f"INSERT INTO {table} {table_names} VALUES ({placeholders})"
        self.execute(query, tuple(row))

    def clean_all_values(self):
        for table in self.scheme_tables.keys():
            self.execute(f"DELETE FROM {table}")
