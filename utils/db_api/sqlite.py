import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    def create_cart(self):
        sql = """
    CREATE TABLE Cart (
        tg_id int NOT NULL,
        Product varchar(255),
        quantity int
        );
"""
        self.execute(sql, commit=True)
        # bu codeni app.py qo'shib qo'yamiz

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def add_product(self, tg_id: int, Product: str, quantity: int):
        sql = "INSERT INTO Cart(tg_id, Product,  quantity) VALUES( ?, ?, ?)"
        self.execute(sql, parameters=(tg_id, Product, quantity), commit=True)

    def get_product(self, **kwargs):
        sql = " SELECT * FROM Cart WHERE "
        sql, parametrs = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parametrs, fetchall=True)

    def update_product(self, tg_id: int, Product: str, quantity: int):
        sql = """ UPDATE Cart SET quantity=? WHERE tg_id=? AND Product=?"""
        return self.execute(sql, (quantity, tg_id, Product), commit=True)

    def chek_product(self, **kwargs):
        sql = " SELECT * FROM Cart WHERE "
        sql, parametrs = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parametrs, fetchone=True)

    def delete_product(self, tg_id: int, Product: str):
        sql = "DELETE FROM Cart WHERE tg_id=? AND Product=?"
        return self.execute(sql, (tg_id, Product), commit=True)

    def clear_cart(self, **kwargs):
        sql = "DELETE FROM Cart WHERE"
        sql, parameters = self.format_args(sql, kwargs)
        sql = self.format_args(sql, parameters=parameters, commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________
Executing:
{statement}
_____________________________________________________
""")
