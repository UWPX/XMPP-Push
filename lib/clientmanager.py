import sqlite3
from lib.log import log


class Clientmanager(object):
    """docstring for Clientmanager"""
    log = None

    connection = None
    cursor = None

    def __init__(self, logger):
        self.log = logger

    def connectToDatabase(self, datebaseName):
        try:
            self.connection = sqlite3.connect(datebaseName)
            self.cursor = self.connection.cursor()
        except:
            self.log.printError("Connection to database couldn't be established!")

    def closeConncection(self):
        try:
            self.connection.close()
        except:
            self.log.printError("Connection to database couldn't be closed!")

    def commitChanges(self):
        try:
            self.connection.commit()
        except:
            self.log.printError("Couldn't commit (save) changes in database!")

    def addClient(self, hash, ip, server):
        try:
            self.cursor.execute("INSERT INTO clients VALUES (?, ?, ?)",
                (hash, ip, server))
        except:
            self.log.printError("Couldn't write new entry to database")

    def readClientData(self):
        pass
        # TODO

    def deleteClient(self, criteria):
        try:
            pass
            # TODO
            # self.cursor.execute("DELETE FROM Zoznam WHERE Name=?", criteria)
        except:
            self.log.printError("Database entry couldn't be deleted!")


if __name__ == '__main__':
    pass
