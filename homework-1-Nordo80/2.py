import mysql.connector


class Connecion_mysql:
    """Class mysql."""

    def __init__(self, localhost: str, user: str, password: str, database_name: str):
        """Mysql constructor."""
        self.localhost = localhost
        self.user = user
        self.password = password
        self.database_name = database_name

    def connect(self):
        """Connect to database"""
        self.conn = mysql.connector.connect(
            host=self.localhost,
            user=self.user,
            password=self.password,
            database=self.database_name
        )

        return self.conn

    def create_database(self):
        """Creating database."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE 333wname_of_database")

    def check_database_exist(self):
        """Cheking database exist."""
        conn = self.connect()
        mycursor = conn.cursor()
        mycursor.execute("SHOW DATABASES")

        for x in mycursor:
            print(x)

    def create_a_table(self):
        """Creating a table."""
        conn = self.connect()
        mycursor = conn.cursor()
        mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

    def check_table_exist(self):
        """Check table exit."""
        conn = self.connect()
        mycursor = conn.cursor()
        mycursor.execute("SHOW TABLES")
        for x in mycursor:
            print(x)

    def set_a_primary_key(self):
        """Puts a primary key."""
        conn = self.connect()
        mycursor = conn.cursor()
        mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

    def insert_multiply_rows(self):
        """Insert multiply rows."""
        conn = self.connect()
        mycursor = conn.cursor()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = [
            ('Peter', 'Lowstreet 4'),
            ('Amy', 'Apple st 652'),
            ('Hannah', 'Mountain 21'),
            ('Michael', 'Valley 345'),
            ('Sandy', 'Ocean blvd 2'),
            ('Betty', 'Green Grass 1'),
            ('Richard', 'Sky st 331'),
            ('Susan', 'One way 98'),
            ('Vicky', 'Yellow Garden 2'),
            ('Ben', 'Park Lane 38'),
            ('William', 'Central st 954'),
            ('Chuck', 'Main Road 989'),
            ('Viola', 'Sideway 1633')
        ]
        mycursor.executemany(sql, val)
        conn.commit()
        print(mycursor.rowcount, "was inserted.")

    def select_from_table(self):
        """Select from table."""
        conn = self.connect()
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def drop_table(self):
        """Drop table."""
        conn = self.connect()
        mycursor = conn.cursor()
        sql = "DROP TABLE IF EXISTS customers"
        mycursor.execute(sql)


if __name__ == '__main__':
    connect_without_database = Connecion_mysql("localhost", "newuser", "password", "")
    connect_with_database = Connecion_mysql("localhost", "newuser", "password", "mydatabase")
