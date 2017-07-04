__author__ = 'Coupang'

import sqlite3


class sql:
    database = ""
    con = sqlite3.connect(database)
    cursor = con.cursor()

    def excute(self, query):
        self.cursor.execute(query)
        self.con.commit()
        return self.cursor

    def connect(self, dataName):
        self.database = dataName

    def close(self):
        self.con.close()
