# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PythonApplication1 import *

#from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
#from PySide2.QtCore import QFile
#from PySide2.QtUiTools import QUiLoader
from PyQt5 import uic, QtGui, QtCore
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
    QPushButton, QAction, QLineEdit, QMessageBox)

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication

##Form, _ =uic.loadUiType('form.ui')
class Widget(QMainWindow):
    def __init__(self):
        #uic.loadUi('form.ui', self)
        super(Widget, self).__init__()
     ##   self.load_ui('form.ui', self)
       # uic.
        
        uic.loadUi('form.ui',self)
 ##       self.setup
    #    self.ui=Widget()
       # self.load_ui('form.ui')
        self.model1=SportDB()
        self.model2=TrainDB()
        self.model3=TranspDB()
        self.model4=GumDB()
        self.model5=SponDB()
        self.model6=ClubDB()
        self.model2.addListener(self.updateTr)
        self.model1.addListener(self.updateSprt)
        self.model3.addListener(self.update_car)
        self.model4.addListener(self.update_gm)
        self.model5.addListener(self.update_spn)
        self.model6.addListener(self.update_clb)
#Trainer button
        self.pushButton.clicked.connect(self.deleteTr)
        self.pushButton_2.clicked.connect(self.changeTr)
        self.pushButton_3.clicked.connect( self.addTr)
        self.pushButton_19.clicked.connect( self.prevTr)
        self.pushButton_20.clicked.connect( self.nextTr)
#Sportsmen button
        self.pushButton_4.clicked.connect(self.addSprt)
        self.pushButton_5.clicked.connect(self.changeSprt)
        self.pushButton_6.clicked.connect( self.deleteSprt)
        self.pushButton_21.clicked.connect( self.prevSprt)
        self.pushButton_22.clicked.connect( self.nextSprt)
#Gum button
        self.pushButton_7.clicked.connect(self.change_gm)
        self.pushButton_8.clicked.connect(self.add_gm)
        self.pushButton_9.clicked.connect( self.delete_gm)
        self.pushButton_29.clicked.connect( self.prev_gm)
        self.pushButton_30.clicked.connect( self.next_gm)
#Club button
        self.pushButton_10.clicked.connect(self.add_clb)
        self.pushButton_11.clicked.connect(self.change_clb)
        self.pushButton_12.clicked.connect( self.delete_clb)
        self.pushButton_27.clicked.connect( self.prev_clb)
        self.pushButton_28.clicked.connect( self.next_clb)
#Transport button
        self.pushButton_13.clicked.connect(self.add_car)
        self.pushButton_14.clicked.connect(self.change_car)
        self.pushButton_15.clicked.connect( self.delete_car)
        self.pushButton_25.clicked.connect( self.prev_car)
        self.pushButton_26.clicked.connect( self.next_car)
#Sponsor button
        self.pushButton_16.clicked.connect(self.add_spn)
        self.pushButton_17.clicked.connect(self.change_spn)
        self.pushButton_18.clicked.connect( self.delete_spn)
        self.pushButton_23.clicked.connect( self.prev_spn)
        self.pushButton_24.clicked.connect( self.next_spn)


 ##       self.lineEdit.textEdited.connect(self.addTr)
    ##    self.ui.pushButton_16.clicked.connect(self.add_spn)

        self.show()
##    #Trainer
    def prevTr(self):
        self.model2.prev()
    def nextTr(self):
        self.model2.next()
    def addTr(self):
        self.model2.add_train(str(self.lineEdit_2.text()),str( self.lineEdit_3.text()),int(self.lineEdit_4.text()),str(self.lineEdit_5.text()))
        print(self.lineEdit_2.text())
    def deleteTr(self):
        self.model2.delete_train(int(self.lineEdit.text()))
    def changeTr(self):
        self.model2.change_train(int(self.lineEdit.text()),str(self.lineEdit_5.text()))
    def updateTr(self, model2):
        self.lineEdit.setText(str(model2.id))
        self.lineEdit_2.setText(str(model2.lastname))
        self.lineEdit_3.setText(str(model2.firstname))
        self.lineEdit_4.setText(str(model2.year_bday))
        self.lineEdit_5.setText(str(model2.rank))
    ##Sportsmen
    def prevSprt(self):
        self.model1.prev()
    def nextSprt(self):
        self.model1.next()
    def addSprt(self):
        self.model1.add_sp(str(self.lineEdit_7.text()),str( self.lineEdit_8.text()),str(self.lineEdit_9.text()),int(self.lineEdit_10.text()),int(self.lineEdit_11.text()),int(self.lineEdit_12.text()),int(self.lineEdit_13.text()),int(self.lineEdit_14.text()))
        print(self.lineEdit_2.text())
    def deleteSprt(self):
        self.model1.delete_sp(int(self.lineEdit_6.text()))
    def changeSprt(self):
        self.model1.change_sp(int(self.lineEdit_6.text()),int(self.lineEdit_11.text()),int(self.lineEdit_12.text()))
    def updateSprt(self, model1):
        self.lineEdit_6.setText(str(model1.id))
        self.lineEdit_7.setText(str(model1.lastname))
        self.lineEdit_8.setText(str(model1.firstname))
        self.lineEdit_9.setText(str(model1.role))
        self.lineEdit_10.setText(str(model1.year_bday))
        self.lineEdit_11.setText(str(model1.height))
        self.lineEdit_12.setText(str(model1.weight))
        self.lineEdit_13.setText(str(model1.date_hw))
        self.lineEdit_14.setText(str(model1.number))
    #Gum
    def prev_gm(self):
        self.model4.prev()
    def next_gm(self):
        self.model4.next()
    def add_gm(self):
        self.model4.add_gum(str(self.lineEdit_15.text()),str(self.lineEdit_17.text()),int(self.lineEdit_18.text()),int(self.lineEdit_19.text()),int(self.lineEdit_20.text()))
    def delete_gm(self):
        self.model4.delete_gum(int(self.lineEdit_16.text()))
    def change_gm(self):
        self.model4.change_gum(int(self.lineEdit_16.text()),str(self.lineEdit_15.text()),str(self.lineEdit_17.text()),int(self.lineEdit_18.text()),int(self.lineEdit_19.text()),int(self.lineEdit_20.text()))
    def update_gm(self, model4):
        self.lineEdit_16.setText(str(model4.id))
        self.lineEdit_15.setText(str(model4.name_gum))
        self.lineEdit_17.setText(str(model4.address))
        self.lineEdit_18.setText(str(model4.capacity))
        self.lineEdit_19.setText(str(model4.phone_number))
        self.lineEdit_20.setText(str(model4.category))
##Club
    def prev_clb(self):
        self.model6.prev()
    def next_clb(self):
        self.model6.next()
    def add_clb(self):
        self.model6.add_club(str(self.lineEdit_27.text()),int(self.lineEdit_28.text()),str(self.lineEdit_29.text()),str(self.lineEdit_21.text()),str(self.lineEdit_22.text()),str(self.lineEdit_23.text()),str(self.lineEdit_25.text()),str(self.lineEdit_24.text()))
    def delete_clb(self):
        self.model6.delete_club(int(self.lineEdit_26.text()))
    def change_clb(self):
        self.model6.change_club(str(self.lineEdit_27.text()),int(self.lineEdit_28.text()),str(self.lineEdit_29.text()),str(self.lineEdit_21.text()),str(self.lineEdit_22.text()),str(self.lineEdit_23.text()),str(self.lineEdit_25.text()),str(self.lineEdit_24.text()))
    def update_clb(self, model6):
        
        self.lineEdit_26.setText(str(model6.id))
        self.lineEdit_27.setText(str(model6.nameClub))
        self.lineEdit_28.setText(str(model6.year_create))
        self.lineEdit_29.setText(str(model6.city))
        self.lineEdit_25.setText(str(model6.gum))
        self.lineEdit_24.setText(str(model6.sportsmen))
        self.lineEdit_23.setText(str(model6.trainer))
        self.lineEdit_22.setText(str(model6.type_car))
        self.lineEdit_21.setText(str(model6.name_spon))
##Transport
    def prev_car(self):
        self.model3.prev()
    def next_car(self):
        self.model3.next()
    def add_car(self):
        self.model3.add_trans(str(self.lineEdit_31.text()),int(self.lineEdit_32.text()))
    def delete_car(self):
        self.model3.delete_trans(int(self.lineEdit_30.text()))
    def change_car(self):
        self.model3.change_trans(int(self.lineEdit_30.text()),str(self.lineEdit_31.text()), str(self.lineEdit_32.text()))
    def update_car(self, model3):
        
        self.lineEdit_30.setText(str(model3.id))
        self.lineEdit_31.setText(str(model3.typ_tr))
        self.lineEdit_32.setText(str(model3.capacity_tr))

    #sponsor
    def prev_spn(self):
        self.model5.prev()
    def next_spn(self):
        self.model5.next()
    def add_spn(self):
        self.model5.add_spon(str(self.lineEdit_34.text()))
    def delete_spn(self):
        self.model5.delete_spon(int(self.lineEdit_33.text()))
    def change_spn(self):
        self.model5.change_spon(int(self.lineEdit_33.text()),str(self.lineEdit_34.text()))
    def update_spn(self, model5):
        
        self.lineEdit_33.setText(str(model5.id))
        self.lineEdit_34.setText(str(model5.name_sponsor))

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app=QtWidgets.QApplication([])
    #app=QtGui.QGuiApplication
    #app=QtGui.qap
   # app=QtGui.QApplication([])
   # app = QApplication([])
    widget = Widget()
  #  widget.show()
    sys.exit(app.exec_())
