import sys
import os
import re
from datetime import date

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QPushButton, QWidget, QDialogButtonBox, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QMessageBox, QDataWidgetMapper, QTableView,
)
from PySide6.QtGui import (QAction, QIcon)
from PySide6.QtCore import (Qt, QAbstractItemModel, )
from PySide6.QtSql import (QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery, QSqlRelation,
                           QSqlRelationalDelegate, QSqlRelationalTableModel,
                           )

from widgets.main_window import Ui_MainWindow
from widgets.novo_socio import Ui_janela_novoSocio


class Sociedade(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        self.home_action = QAction(QIcon("icons/house"), "Home")
        self.stackedWidget.setCurrentWidget(self.page_main)
        self.para_tras = QAction(QIcon("icons/arrow-left.png"), "Voltar atrás")
        self.para_frente = QAction(QIcon("icons/arrow-right.png"), "Voltar frente")
        self.toolbar.addAction(self.home_action)
        self.toolbar.addAction(self.para_tras)
        self.toolbar.addAction(self.para_frente)
        self.toolbar.addAction(self.action_InserirNovoSocio)
        self.toolbar.addAction(self.action_editarDadosDeSocio)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.showMaximized()
        # Variável para guardar o sócio atual a trabalhar
        self.socio_atual = dict()
        # Variável para guardar a página atual do QStackedLayout
        self.atual_widget = self.page_main
        # Definir os signals -> slots iniciais
        self.set_initial_signals()
        # Carregar a base de dados inicial
        self.db = self.load_database()
        for action in self.toolbar.children():
            if isinstance(action, QWidget):
                action.triggered.connect(self.set_current_page)

    def set_current_page(self, action):
        if action.text() == "Home":
            self.stackedWidget.setCurrentWidget(self.page_main)
        if action.text() == "Voltar atrás":
            anterior_widget = self.stackedWidget.currentWidget()
        if action.text() == "Voltar frente":
            pass
        if action.text() == "Abrir listagens" or action.text() == "Listagens":
            self.stackedWidget.setCurrentWidget(self.page_listagens)
            self.abrir_listagens()

    def ativar_actions(self, action):
        print("Widget que enviou:", self.sender(), action)

    def load_database(self, file=None):
        """
        Função para carregar a base de dados para a aplicação
        :param file: O ficheiro a abrir
        :return: QSqlDatabase
        """
        if file:
            ficheiro = file
        else:
            ficheiro = "srcvp_socios.sqlite3"
        try:
            if ficheiro not in os.listdir('database/'):
                raise FileNotFoundError
            db = QSqlDatabase("QSQLITE")
            db.setDatabaseName("database/srcvp_socios.sqlite3")
            db.open()
            return db
        except FileNotFoundError:
            aviso = QMessageBox(parent=self)
            aviso.setWindowTitle("Base de dados de sócios")
            aviso.setText("Não consegui carregar a base de dados a partir da localização original.\n"
                          "Tente carregar a base de dados manualmente.")
            aviso.setIcon(QMessageBox.Icon.Critical)
            aviso.show()

    def set_initial_signals(self):
        """
        Método para atribuir signals a slots
        :return: None
        """
        self.action_InserirNovoSocio.triggered.connect(self.abrir_criar_novo_socio)
        self.pushB_novoSocio.pressed.connect(self.abrir_criar_novo_socio)
        self.action_editarDadosDeSocio.triggered.connect(self.abrir_editar_socio)
        self.action_listagens.triggered.connect(self.abrir_listagens)
        self.pushB_listagens.pressed.connect(self.abrir_listagens)
        self.action_sair.triggered.connect(self.close)

    def abrir_listagens(self):
        """
        Método despoletado ao escolher a opção de listagens
        :return:
        """
        self.model = QSqlTableModel(db=self.db)
        #self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.setTable("Socio")
        self.model.select()
        self.tableV_listaSocios.setModel(self.model)
        self.stackedWidget.setCurrentWidget(self.page_listagens)
        self.atual_widget = self.page_listagens
        self.lineE_filtroSocios.textChanged.connect(self.atualizar_listagem)
        self.tableV_listaSocios.resizeColumnsToContents()

    def atualizar_listagem(self, string):
        """
        Método para filtrar a listagem de sócios
        :param string: o texto inserido pelo utilizador no widget lineE_filtroSocios
        :return: None
        """
        filtro_str = "nome LIKE '%{}%' OR id LIKE '%{}%'".format(string, string)
        self.model.setFilter(filtro_str)

    def abrir_editar_socio(self):
        model = QSqlTableModel(db=self.db)
        model.setTable("Socio")
        model.select()
        mapper = QDataWidgetMapper()
        mapper.setModel(model)
        tabela = QTableView()
        tabela.setModel(model)
        self.page_2.setLayout(QHBoxLayout())
        self.page_2.layout().addWidget(tabela)
        self.stackedWidget.setCurrentIndex(2)

    def abrir_criar_novo_socio(self):
        novo_socio_code = Ui_janela_novoSocio(db=self.db)
        novo_socio_code.setModal(True)
        socio = QSqlQuery("SELECT * FROM Socio WHERE id = :id", self.db)
        socio.bindValue(":id", 2)
        socio.exec()
        print(socio)
        # Se a opção for gravar um novo sócio
        if novo_socio_code.exec():
            pass
        else:
            del novo_socio_code


if __name__ == '__main__':
    icons_path = 'icons/'
    app = QApplication(sys.argv)
    window = Sociedade()
    window.show()
    app.exec()
