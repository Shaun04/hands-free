import sqlite3

'''
Version: 1.0
^______^
'''

class TaskCreater:
    def __init__(self) :
        self.conn = sqlite3.connect("main.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS mainschedule (
            date text,
            time integer,
            title text,
            data text,
            link text
        )
        """)
        
        self.conn.commit()
    def add_data(self, date, time, title, data, link):
        self.cur.execute("INSERT INTO mainschedule VALUES (?, ?, ?, ?, ?)", (date, time, title, data, link))
        self.conn.commit()
    def read_data(self, date):
        self.cur.execute("SELECT * FROM mainschedule WHERE date=:date", {"date": date})
        items = self.cur.fetchall()
        return items
        self.conn.commit()
    def read_all_data(self):
        self.cur.execute("SELECT * FROM mainschedule")
        itemsAll = self.cur.fetchall()
        print(itemsAll)
    def del_data(self, date):
        self.cur.execute("DELETE FROM mainschedule WHERE date=:date", {"date": date})
        self.conn.commit()
    def del_all_data(self):
        self.cur.execute("DELETE FROM mainschedule")
        self.conn.commit()
if __name__ == "__main__":
    c = TaskCreater()
    c.create_table()
    choice = int(input("Choose 1 for adding data, 2 for reading data :"))
    if choice == 1:
        # date = input("Enter the date: ")
        time = int(input("Enter the time: "))
        title = input("Enter the title: ")
        data = input("Enter the data: ")
        link = input("Enter the link: ")
        c.add_data("14 09 2021", time, title, data, link)
        print("Added")
    elif choice == 2:
        print(c.read_data("09 09 2021"))
    elif choice == 3:
        c.del_all_data()
        c.read_all_data()
        print("Done")

