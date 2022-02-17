# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSplitter,
    QStackedWidget, QStatusBar, QTableView, QVBoxLayout,
    QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(894, 838)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setLocale(QLocale(QLocale.Portuguese, QLocale.Portugal))
        self.action_fecharBaseDeDados = QAction(MainWindow)
        self.action_fecharBaseDeDados.setObjectName(u"action_fecharBaseDeDados")
        self.action_sair = QAction(MainWindow)
        self.action_sair.setObjectName(u"action_sair")
        self.action_InserirNovoSocio = QAction(MainWindow)
        self.action_InserirNovoSocio.setObjectName(u"action_InserirNovoSocio")
        icon = QIcon()
        icon.addFile(u"icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_InserirNovoSocio.setIcon(icon)
        self.action_editarDadosDeSocio = QAction(MainWindow)
        self.action_editarDadosDeSocio.setObjectName(u"action_editarDadosDeSocio")
        icon1 = QIcon()
        icon1.addFile(u"icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_editarDadosDeSocio.setIcon(icon1)
        self.action_deFicheiro = QAction(MainWindow)
        self.action_deFicheiro.setObjectName(u"action_deFicheiro")
        self.action_outraFonte = QAction(MainWindow)
        self.action_outraFonte.setObjectName(u"action_outraFonte")
        self.action_comoInserirNovoSocio = QAction(MainWindow)
        self.action_comoInserirNovoSocio.setObjectName(u"action_comoInserirNovoSocio")
        self.action_sobre = QAction(MainWindow)
        self.action_sobre.setObjectName(u"action_sobre")
        self.action_graficosEHistogramas = QAction(MainWindow)
        self.action_graficosEHistogramas.setObjectName(u"action_graficosEHistogramas")
        self.action_listagens = QAction(MainWindow)
        self.action_listagens.setObjectName(u"action_listagens")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setMidLineWidth(0)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.verticalLayout_2 = QVBoxLayout(self.page_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.pushB_novoSocio = QPushButton(self.page_main)
        self.pushB_novoSocio.setObjectName(u"pushB_novoSocio")
        font1 = QFont()
        font1.setBold(True)
        self.pushB_novoSocio.setFont(font1)
        self.pushB_novoSocio.setIcon(icon)
        self.pushB_novoSocio.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushB_novoSocio, 0, 0, 1, 1)

        self.pushB_graficos = QPushButton(self.page_main)
        self.pushB_graficos.setObjectName(u"pushB_graficos")
        self.pushB_graficos.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"icons/graph.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushB_graficos.setIcon(icon2)
        self.pushB_graficos.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushB_graficos, 1, 0, 1, 1)

        self.pushB_listagens = QPushButton(self.page_main)
        self.pushB_listagens.setObjectName(u"pushB_listagens")
        self.pushB_listagens.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushB_listagens.setIcon(icon3)
        self.pushB_listagens.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushB_listagens, 0, 1, 1, 1)

        self.pushB_pagarCotas = QPushButton(self.page_main)
        self.pushB_pagarCotas.setObjectName(u"pushB_pagarCotas")
        self.pushB_pagarCotas.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"icons/money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushB_pagarCotas.setIcon(icon4)
        self.pushB_pagarCotas.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushB_pagarCotas, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page_main)
        self.page_estatisticas = QWidget()
        self.page_estatisticas.setObjectName(u"page_estatisticas")
        self.stackedWidget.addWidget(self.page_estatisticas)
        self.page_listagens = QWidget()
        self.page_listagens.setObjectName(u"page_listagens")
        self.verticalLayout_3 = QVBoxLayout(self.page_listagens)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(self.page_listagens)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_filtroListagens = QLabel(self.splitter)
        self.label_filtroListagens.setObjectName(u"label_filtroListagens")
        self.splitter.addWidget(self.label_filtroListagens)
        self.lineE_filtroSocios = QLineEdit(self.splitter)
        self.lineE_filtroSocios.setObjectName(u"lineE_filtroSocios")
        self.splitter.addWidget(self.lineE_filtroSocios)

        self.verticalLayout_3.addWidget(self.splitter)

        self.tableV_listaSocios = QTableView(self.page_listagens)
        self.tableV_listaSocios.setObjectName(u"tableV_listaSocios")

        self.verticalLayout_3.addWidget(self.tableV_listaSocios)

        self.stackedWidget.addWidget(self.page_listagens)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 894, 27))
        self.menu_ficheiro = QMenu(self.menubar)
        self.menu_ficheiro.setObjectName(u"menu_ficheiro")
        self.menu_carregarBaseDeDados = QMenu(self.menu_ficheiro)
        self.menu_carregarBaseDeDados.setObjectName(u"menu_carregarBaseDeDados")
        self.menu_dados = QMenu(self.menubar)
        self.menu_dados.setObjectName(u"menu_dados")
        self.menu_estatisticas = QMenu(self.menubar)
        self.menu_estatisticas.setObjectName(u"menu_estatisticas")
        self.menu_ajuda = QMenu(self.menubar)
        self.menu_ajuda.setObjectName(u"menu_ajuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_ficheiro.menuAction())
        self.menubar.addAction(self.menu_dados.menuAction())
        self.menubar.addAction(self.menu_estatisticas.menuAction())
        self.menubar.addAction(self.menu_ajuda.menuAction())
        self.menu_ficheiro.addAction(self.menu_carregarBaseDeDados.menuAction())
        self.menu_ficheiro.addAction(self.action_fecharBaseDeDados)
        self.menu_ficheiro.addSeparator()
        self.menu_ficheiro.addAction(self.action_sair)
        self.menu_carregarBaseDeDados.addAction(self.action_deFicheiro)
        self.menu_carregarBaseDeDados.addAction(self.action_outraFonte)
        self.menu_dados.addAction(self.action_InserirNovoSocio)
        self.menu_dados.addAction(self.action_editarDadosDeSocio)
        self.menu_estatisticas.addAction(self.action_graficosEHistogramas)
        self.menu_estatisticas.addAction(self.action_listagens)
        self.menu_ajuda.addAction(self.action_comoInserirNovoSocio)
        self.menu_ajuda.addSeparator()
        self.menu_ajuda.addAction(self.action_sobre)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sociedade Recreativa e Cultural de Vale da Pinta", None))
        self.action_fecharBaseDeDados.setText(QCoreApplication.translate("MainWindow", u"Fechar base de dados", None))
        self.action_sair.setText(QCoreApplication.translate("MainWindow", u"&Sair", None))
        self.action_InserirNovoSocio.setText(QCoreApplication.translate("MainWindow", u"&Inserir novo s\u00f3cio", None))
#if QT_CONFIG(statustip)
        self.action_InserirNovoSocio.setStatusTip(QCoreApplication.translate("MainWindow", u"Registar novo s\u00f3cio", None))
#endif // QT_CONFIG(statustip)
        self.action_editarDadosDeSocio.setText(QCoreApplication.translate("MainWindow", u"Editar dados de s\u00f3cio", None))
#if QT_CONFIG(statustip)
        self.action_editarDadosDeSocio.setStatusTip(QCoreApplication.translate("MainWindow", u"Editar ficha de s\u00f3cio", None))
#endif // QT_CONFIG(statustip)
        self.action_deFicheiro.setText(QCoreApplication.translate("MainWindow", u"De ficheiro...", None))
        self.action_outraFonte.setText(QCoreApplication.translate("MainWindow", u"Outra fonte...", None))
        self.action_comoInserirNovoSocio.setText(QCoreApplication.translate("MainWindow", u"Como inserir novo s\u00f3cio", None))
        self.action_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre...", None))
        self.action_graficosEHistogramas.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1ficos e histogramas", None))
        self.action_listagens.setText(QCoreApplication.translate("MainWindow", u"Listagens", None))
#if QT_CONFIG(tooltip)
        self.pushB_novoSocio.setToolTip(QCoreApplication.translate("MainWindow", u"Criar novo s\u00f3cio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushB_novoSocio.setStatusTip(QCoreApplication.translate("MainWindow", u"Registar novo s\u00f3cio", None))
#endif // QT_CONFIG(statustip)
        self.pushB_novoSocio.setText(QCoreApplication.translate("MainWindow", u"Novo s\u00f3cio", None))
#if QT_CONFIG(tooltip)
        self.pushB_graficos.setToolTip(QCoreApplication.translate("MainWindow", u"Obter gr\u00e1ficos", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushB_graficos.setStatusTip(QCoreApplication.translate("MainWindow", u"Obter gr\u00e1ficos diversos", None))
#endif // QT_CONFIG(statustip)
        self.pushB_graficos.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1ficos", None))
#if QT_CONFIG(tooltip)
        self.pushB_listagens.setToolTip(QCoreApplication.translate("MainWindow", u"Obter listagens", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushB_listagens.setStatusTip(QCoreApplication.translate("MainWindow", u"Obter listagens diversas", None))
#endif // QT_CONFIG(statustip)
        self.pushB_listagens.setText(QCoreApplication.translate("MainWindow", u"Listagens", None))
#if QT_CONFIG(tooltip)
        self.pushB_pagarCotas.setToolTip(QCoreApplication.translate("MainWindow", u"Pagar cotas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushB_pagarCotas.setStatusTip(QCoreApplication.translate("MainWindow", u"Registar pagamentos de cotas", None))
#endif // QT_CONFIG(statustip)
        self.pushB_pagarCotas.setText(QCoreApplication.translate("MainWindow", u"Pagar cotas", None))
        self.label_filtroListagens.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.menu_ficheiro.setTitle(QCoreApplication.translate("MainWindow", u"&Ficheiro", None))
        self.menu_carregarBaseDeDados.setTitle(QCoreApplication.translate("MainWindow", u"Carregar base de dados", None))
        self.menu_dados.setTitle(QCoreApplication.translate("MainWindow", u"&Dados", None))
        self.menu_estatisticas.setTitle(QCoreApplication.translate("MainWindow", u"&Estat\u00edsticas", None))
        self.menu_ajuda.setTitle(QCoreApplication.translate("MainWindow", u"&Ajuda", None))
    # retranslateUi

