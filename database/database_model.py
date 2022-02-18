import sqlite3

from PySide6.QtGui import QStandardItemModel
from PySide6.QtCore import QAbstractItemModel, QAbstractListModel, QAbstractTableModel, Qt
from PySide6.QtSql import (QSqlDatabase, QSqlQueryModel, QSqlQuery, QSqlRelation, QSqlTableModel,
                           QSqlRelationalTableModel, )

import pandas as pd


class my_model(QSqlRelationalTableModel):
    def __init__(self, db):
        super(my_model, self).__init__(db=db)
        self.table = None

    def setTable(self, tableName:str) -> None:
        self.table = tableName
