# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novo_socio.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QLocale, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QCalendarWidget, QCheckBox, QComboBox, QDialogButtonBox, QFormLayout, QHBoxLayout,
                               QDialog, QLabel, QLayout, QLineEdit, QSpinBox, QTextEdit, QVBoxLayout, QWidget,
                               QMessageBox, QTableView, )
from PySide6.QtSql import (QSqlQuery, QSqlQueryModel, QSqlRelationalTableModel, QSqlRelation)

from database.database_model import my_model


class Ui_janela_novoSocio(QDialog):

    def __init__(self, db, socio=None):
        super().__init__()
        self.setupUi(self)
        self.socio = socio
        self.db = db
        self.build_slots()

        # Preencher a comboB_cota com as cotas existentes na base de dados
        query_cotas = QSqlQuery("SELECT * FROM Cota", db=self.db)
        while query_cotas.next():
            self.comboB_cota.addItem(
                str(query_cotas.value("nome")) + " - " + str(query_cotas.value("valor")) + "€"
            )

        if self.socio is not None:
            self.preencher_dados_socio()
        else:
            # Descobrir o próximo número de sócio e adicionar ao formulário
            query_cotas = QSqlQuery("SELECT seq FROM sqlite_sequence WHERE name = 'Socio'", db=self.db)
            model = QSqlQueryModel()
            model.setQuery(query_cotas)
            next_id = model.data(model.index(0, 0)) + 1
            self.spinB_numero.setValue(next_id)

    def parse_data(self):
        if self.socio is None:
            self.socio = dict()
        self.socio['id'] = self.spinB_numero.value()
        self.socio['nome'] = self.lineE_nome.text() or None
        self.socio['morada'] = self.lineE_morada.text()
        self.socio['localidade'] = self.lineE_localidade.text()
        self.socio['nif'] = self.lineE_nif.text()
        self.socio['contacto'] = self.lineE_contacto.text()
        self.socio['ultima_cota_paga'] = self.calendarWidget.selectedDate().toPython().strftime("%m/%Y")
        self.socio['data_admissao'] = self.calendarWidget.selectedDate().toPython().strftime("%d/%m/%Y")
        if self.checkB_ativo.isChecked():
            self.socio['ativo'] = 1
        else:
            self.socio['ativo'] = 0
        self.socio['notas'] = self.textE_notas.toPlainText()
        nome_da_cota = self.comboB_cota.currentText().split(' - ')[0]
        query_cotas = QSqlQuery("SELECT id FROM Cota WHERE nome LIKE '%{}%'".format(nome_da_cota), db=self.db)
        query_cotas.first()
        cota_id = query_cotas.value(0)
        self.socio['cota'] = cota_id

    def build_slots(self):
        self.spinB_numero.valueChanged.connect(self.check_num_socio)
        self.checkB_num_socio.stateChanged.connect(self.spinB_numero.setEnabled)
        self.checkB_num_socio.stateChanged.connect(lambda state: self.check_num_socio(state=state))

    def check_num_socio(self, value=None, state=None):
        """
        Método para avisar o utilizador quando escolher um número de sócio já existente
        :param state: valor do checkBox checkB_num_socio
        :param value: valor da spinBox spinB_numero
        :return: Bool
        """
        query = QSqlQuery("SELECT id FROM Socio", self.db)
        font = self.spinB_numero.font()
        font.setPointSize(14)
        if state == Qt.CheckState.Checked or self.checkB_num_socio.isChecked():
            while query.next():
                if value == query.value(0):
                    self.spinB_numero.setStyleSheet("background-color: red;")
                    self.spinB_numero.setToolTip("Sócio já existe")
                    break
                else:
                    self.spinB_numero.setStyleSheet("background-color: white;")
                    self.spinB_numero.setToolTip("")
        else:
            self.spinB_numero.setStyleSheet("background-color: white;")
            query = QSqlQuery("SELECT seq FROM sqlite_sequence WHERE name='Socio'", self.db)
            query.first()
            next_id = int(query.value(0))+1
            self.spinB_numero.setValue(next_id)
        self.spinB_numero.setFont(font)

    def setupUi(self, janela_novoSocio):
        if not janela_novoSocio.objectName():
            janela_novoSocio.setObjectName(u"janela_novoSocio")
        janela_novoSocio.resize(928, 854)
        font = QFont()
        font.setPointSize(14)
        janela_novoSocio.setFont(font)
        janela_novoSocio.setFocusPolicy(Qt.TabFocus)
        janela_novoSocio.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"../icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        janela_novoSocio.setWindowIcon(icon)
        janela_novoSocio.setLocale(QLocale(QLocale.Portuguese, QLocale.Portugal))

        # Definição do layout
        self.verticalLayout = QVBoxLayout(janela_novoSocio)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(janela_novoSocio)
        self.label_titulo.setObjectName(u"label_titulo")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_titulo.setFont(font1)
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.label_titulo.setMargin(15)
        self.verticalLayout.addWidget(self.label_titulo)

        # Criar um QHBoxLayout para dispor a linha do número de sócio
        self.layout_num_socio = QHBoxLayout()
        self.label_numero = QLabel(janela_novoSocio)
        self.label_numero.setObjectName(u"label_numero")
        self.spinB_numero = QSpinBox(janela_novoSocio)
        self.spinB_numero.setObjectName(u"spinB_numero")
        self.spinB_numero.setEnabled(False)
        self.checkB_num_socio = QCheckBox("Inserir manualmente", janela_novoSocio)
        self.checkB_num_socio.setChecked(False)
        self.layout_num_socio.addWidget(self.label_numero)
        self.layout_num_socio.addWidget(self.spinB_numero)
        self.layout_num_socio.addWidget(self.checkB_num_socio)
        self.verticalLayout.addLayout(self.layout_num_socio)


        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(20, 20, 20, 20)

        self.label_nome = QLabel(janela_novoSocio)
        self.label_nome.setObjectName(u"label_nome")
        self.lineE_nome = QLineEdit(janela_novoSocio)
        self.lineE_nome.setObjectName(u"lineE_nome")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_nome)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineE_nome)

        self.label_morada = QLabel(janela_novoSocio)
        self.label_morada.setObjectName(u"label_morada")
        self.lineE_morada = QLineEdit(janela_novoSocio)
        self.lineE_morada.setObjectName(u"lineE_morada")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_morada)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineE_morada)

        self.label_localidade = QLabel(janela_novoSocio)
        self.label_localidade.setObjectName(u"label_localidade")
        self.lineE_localidade = QLineEdit(janela_novoSocio)
        self.lineE_localidade.setObjectName(u"lineE_localidade")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_localidade)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineE_localidade)

        self.label_contacto = QLabel(janela_novoSocio)
        self.label_contacto.setObjectName(u"label_contacto")
        self.lineE_contacto = QLineEdit(janela_novoSocio)
        self.lineE_contacto.setObjectName(u"lineE_contacto")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_contacto)
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineE_contacto)

        self.label_nif = QLabel(janela_novoSocio)
        self.label_nif.setObjectName(u"label_nif")
        self.lineE_nif = QLineEdit(janela_novoSocio)
        self.lineE_nif.setObjectName(u"lineE_nif")
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_nif)
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineE_nif)

        self.label_dataAdmicao = QLabel(janela_novoSocio)
        self.label_dataAdmicao.setObjectName(u"label_dataAdmicao")
        self.calendarWidget = QCalendarWidget(janela_novoSocio)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_dataAdmicao)
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.calendarWidget)

        self.label_notas = QLabel(janela_novoSocio)
        self.label_notas.setObjectName(u"label_notas")
        self.textE_notas = QTextEdit(janela_novoSocio)
        self.textE_notas.setObjectName(u"textE_notas")
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_notas)
        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.textE_notas)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.comboB_cota = QComboBox(janela_novoSocio)
        self.comboB_cota.setObjectName(u"comboB_cota")
        self.comboB_cota.setMaxVisibleItems(5)
        self.comboB_cota.setMaxCount(10)
        self.comboB_cota.setInsertPolicy(QComboBox.NoInsert)
        self.checkB_ativo = QCheckBox(janela_novoSocio)
        self.checkB_ativo.setObjectName(u"checkB_ativo")
        self.checkB_ativo.setChecked(True)
        self.horizontalLayout_2.addWidget(self.comboB_cota)
        self.horizontalLayout_2.addWidget(self.checkB_ativo)

        self.formLayout.setLayout(9, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(janela_novoSocio)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Save)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label_nome.setBuddy(self.lineE_nome)
        self.label_morada.setBuddy(self.lineE_morada)
        self.label_localidade.setBuddy(self.lineE_localidade)
        self.label_contacto.setBuddy(self.lineE_contacto)
        self.label_nif.setBuddy(self.lineE_nif)
        self.label_dataAdmicao.setBuddy(self.calendarWidget)
        self.label_notas.setBuddy(self.textE_notas)
        self.label_numero.setBuddy(self.spinB_numero)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineE_nome, self.lineE_morada)
        QWidget.setTabOrder(self.lineE_morada, self.lineE_localidade)
        QWidget.setTabOrder(self.lineE_localidade, self.lineE_contacto)
        QWidget.setTabOrder(self.lineE_contacto, self.lineE_nif)
        QWidget.setTabOrder(self.lineE_nif, self.calendarWidget)
        QWidget.setTabOrder(self.calendarWidget, self.textE_notas)
        QWidget.setTabOrder(self.textE_notas, self.comboB_cota)
        QWidget.setTabOrder(self.comboB_cota, self.checkB_ativo)
        QWidget.setTabOrder(self.checkB_ativo, self.spinB_numero)

        self.retranslateUi(janela_novoSocio)

        QMetaObject.connectSlotsByName(janela_novoSocio)
    # setupUi

    def retranslateUi(self, janela_novoSocio):
        janela_novoSocio.setWindowTitle(QCoreApplication.translate("janela_novoSocio", u"Novo s\u00f3cio - SRCVP", None))
        self.label_titulo.setText(QCoreApplication.translate("janela_novoSocio", u"Novo s\u00f3cio", None))
        self.label_nome.setText(QCoreApplication.translate("janela_novoSocio", u"Nome: ", None))
        self.label_morada.setText(QCoreApplication.translate("janela_novoSocio", u"Morada: ", None))
        self.label_localidade.setText(QCoreApplication.translate("janela_novoSocio", u"Localidade: ", None))
        self.label_contacto.setText(QCoreApplication.translate("janela_novoSocio", u"Contacto: ", None))
        self.label_nif.setText(QCoreApplication.translate("janela_novoSocio", u"NIF: ", None))
        self.label_dataAdmicao.setText(QCoreApplication.translate("janela_novoSocio", u"Data de admiss\u00e3o: ", None))
        self.label_notas.setText(QCoreApplication.translate("janela_novoSocio", u"Notas / Observa\u00e7\u00f5es: ", None))
#if QT_CONFIG(tooltip)
        self.comboB_cota.setToolTip(QCoreApplication.translate("janela_novoSocio", u"Escolha a cota...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboB_cota.setStatusTip(QCoreApplication.translate("janela_novoSocio", u"Escolher a cota para o s\u00f3cio", None))
#endif // QT_CONFIG(statustip)
        self.comboB_cota.setCurrentText("")
        self.checkB_ativo.setText(QCoreApplication.translate("janela_novoSocio", u"S\u00f3cio ativo ?", None))
        self.label_numero.setText(QCoreApplication.translate("janela_novoSocio", u"N\u00famero: ", None))
    # retranslateUi

    def preencher_dados_socio(self):
        self.spinB_numero.setValue(self.socio['id'])
        self.lineE_nome.setText(self.socio['nome'])
        self.lineE_morada.setText(self.socio['morada'] or "")
        self.lineE_localidade.setText(self.socio['localidade'] or "")
        self.lineE_nif.setText(self.socio['nif'] or "")
        self.lineE_contacto.setText(self.socio['contacto'] or "")
        #self.calendarWidget.selectedDate().fromString(self.socio['data_admissao'], "%d/%m/%Y")

    def save_database(self):
        query = QSqlQuery(db=self.db)
        query.prepare(
            "INSERT INTO Socio ("
            "id, nome, morada, localidade, nif, contacto, ultima_cota_paga, data_admissao, ativo, notas, cota"
            ") "
            "VALUES ("
            ":id, :nome, :morada, :localidade, :nif, :contacto, :ultima_cota_paga, :data_admissao, :ativo, :notas,"
            ":cota)"
        )
        query.bindValue(":id", self.socio['id'])
        query.bindValue(":nome", self.socio['nome'])
        query.bindValue(":morada", self.socio['morada'])
        query.bindValue(":localidade", self.socio['localidade'])
        query.bindValue(":nif", self.socio['nif'])
        query.bindValue(":contacto", self.socio['contacto'])
        query.bindValue(":ultima_cota_paga", self.socio['ultima_cota_paga'])
        query.bindValue(":data_admissao", self.socio['data_admissao'])
        query.bindValue(":ativo", self.socio['ativo'])
        query.bindValue(":notas", self.socio['notas'])
        query.bindValue(":cota", self.socio['cota'])
        try:
            query.exec()
            if query.lastError().text() != '':
                raise IndexError(query.lastError().nativeErrorCode())
            return True
        except IndexError as e:
            if e.args[0] == '1299':
                mensagem = 'O nome do sócio não pode ficar em branco'
            elif e.args[0] == '1555':
                mensagem = 'O número de sócio já existe, tem de escolher outro'
            else:
                mensagem = 'Ocorreu um erro a gravar o sócio na base de dados'
            message = QMessageBox(self)
            message.setWindowTitle("Novo Sócio - SRCVP")
            message.setText(mensagem)
            message.setIcon(QMessageBox.Icon.Critical)
            message.exec()
            return False

    def accept(self) -> None:
        self.parse_data()
        if self.save_database():
            super(Ui_janela_novoSocio, self).accept()

    def reject(self) -> None:
        message = QMessageBox(self)
        message.setWindowTitle("Novo Sócio - SRCVP")
        message.setText("Pretende descartar dados do sócio?")
        message.setInformativeText("Se escolher Ok, vai perder os dados já inseridos")
        message.setIcon(QMessageBox.Icon.Warning)
        message.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        resposta = message.exec()
        if resposta == QMessageBox.StandardButton.Ok:
            self.socio = None
            super(Ui_janela_novoSocio, self).reject()
