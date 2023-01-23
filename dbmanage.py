import sqlite3







class Users:

    def __init__(self, database: str):
        self.db = sqlite3.connect(database)
        self.cursor = self.db.cursor()
    
    def new_user(self, id, name, day, level):
        self.cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (id, name, day, level))
        self.db.commit()

    def get_user(self, name):
        self.cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        return self.cursor.fetchone()

    def get_user_by_id(self, id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def update_user(self, id, name, day, level):
        self.cursor.execute("UPDATE users SET name = ?, day = ?, level = ? WHERE id = ?", (name, day, level, id))
        self.db.commit()

    def update_all_days(self):
        self.cursor.execute("UPDATE users SET day = day + 1")
        self.db.commit()

    def delete_user(self, id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        self.db.commit()
    
    def delete_user_by_id(self, id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (id,))
        self.db.commit()

    def delete_all_users(self):
        self.cursor.execute("DELETE FROM users")
        self.db.commit()


