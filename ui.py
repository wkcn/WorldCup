# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 768)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.background = QtGui.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(236, 0, 788, 444))
        self.background.setAlignment(QtCore.Qt.AlignCenter)
        self.background.setObjectName(_fromUtf8("background"))
        self.teamList = QtGui.QTableWidget(self.centralwidget)
        self.teamList.setGeometry(QtCore.QRect(0, 484, 613, 284))
        self.teamList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.teamList.setAlternatingRowColors(True)
        self.teamList.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.teamList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.teamList.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.teamList.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.teamList.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.teamList.setShowGrid(True)
        self.teamList.setGridStyle(QtCore.Qt.NoPen)
        self.teamList.setRowCount(32)
        self.teamList.setObjectName(_fromUtf8("teamList"))
        self.teamList.setColumnCount(9)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList.setHorizontalHeaderItem(8, item)
        self.teamList.horizontalHeader().setCascadingSectionResizes(True)
        self.teamList.horizontalHeader().setDefaultSectionSize(50)
        self.teamList.horizontalHeader().setHighlightSections(False)
        self.teamList.horizontalHeader().setMinimumSectionSize(32)
        self.teamList.horizontalHeader().setSortIndicatorShown(True)
        self.teamList.setColumnWidth(1,150)
        self.dateBoard = QtGui.QLabel(self.centralwidget)
        self.dateBoard.setGeometry(QtCore.QRect(0, 0, 236, 100))
        font = QtGui.QFont()
        font.setPointSize(33)
        font.setBold(True)
        font.setWeight(75)
        self.dateBoard.setFont(font)
        self.dateBoard.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dateBoard.setFrameShape(QtGui.QFrame.WinPanel)
        self.dateBoard.setFrameShadow(QtGui.QFrame.Plain)
        self.dateBoard.setAlignment(QtCore.Qt.AlignCenter)
        self.dateBoard.setObjectName(_fromUtf8("dateBoard"))
        self.playingGame = QtGui.QLabel(self.centralwidget)
        self.playingGame.setGeometry(QtCore.QRect(0, 100, 236, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.playingGame.setFont(font)
        self.playingGame.setAlignment(QtCore.Qt.AlignCenter)
        self.playingGame.setObjectName(_fromUtf8("playingGame"))
        self.beginBTN = QtGui.QPushButton(self.centralwidget)
        self.beginBTN.setGeometry(QtCore.QRect(0, 404, 118, 40))
        self.beginBTN.setObjectName(_fromUtf8("beginBTN"))
        self.speedBTN = QtGui.QPushButton(self.centralwidget)
        self.speedBTN.setGeometry(QtCore.QRect(118, 404, 118, 40))
        self.speedBTN.setObjectName(_fromUtf8("speedBTN"))
        self.finalLabel = QtGui.QLabel(self.centralwidget)
        self.finalLabel.setGeometry(QtCore.QRect(582, 78, 96, 58))
        self.finalLabel.setText(_fromUtf8(""))
        self.finalLabel.setObjectName(_fromUtf8("finalLabel"))
        self.label4_1 = QtGui.QLabel(self.centralwidget)
        self.label4_1.setGeometry(QtCore.QRect(393, 124, 96, 58))
        self.label4_1.setText(_fromUtf8(""))
        self.label4_1.setObjectName(_fromUtf8("label4_1"))
        self.label4_2 = QtGui.QLabel(self.centralwidget)
        self.label4_2.setGeometry(QtCore.QRect(393, 262, 96, 58))
        self.label4_2.setText(_fromUtf8(""))
        self.label4_2.setObjectName(_fromUtf8("label4_2"))
        self.label4_3 = QtGui.QLabel(self.centralwidget)
        self.label4_3.setGeometry(QtCore.QRect(770, 124, 96, 58))
        self.label4_3.setText(_fromUtf8(""))
        self.label4_3.setObjectName(_fromUtf8("label4_3"))
        self.label4_4 = QtGui.QLabel(self.centralwidget)
        self.label4_4.setGeometry(QtCore.QRect(770, 262, 96, 58))
        self.label4_4.setText(_fromUtf8(""))
        self.label4_4.setObjectName(_fromUtf8("label4_4"))
        self.label8_1 = QtGui.QLabel(self.centralwidget)
        self.label8_1.setGeometry(QtCore.QRect(286, 90, 96, 58))
        self.label8_1.setText(_fromUtf8(""))
        self.label8_1.setObjectName(_fromUtf8("label8_1"))
        self.label8_2 = QtGui.QLabel(self.centralwidget)
        self.label8_2.setGeometry(QtCore.QRect(286, 158, 96, 58))
        self.label8_2.setText(_fromUtf8(""))
        self.label8_2.setObjectName(_fromUtf8("label8_2"))
        self.label8_3 = QtGui.QLabel(self.centralwidget)
        self.label8_3.setGeometry(QtCore.QRect(286, 226, 96, 58))
        self.label8_3.setText(_fromUtf8(""))
        self.label8_3.setObjectName(_fromUtf8("label8_3"))
        self.label8_4 = QtGui.QLabel(self.centralwidget)
        self.label8_4.setGeometry(QtCore.QRect(286, 294, 96, 58))
        self.label8_4.setText(_fromUtf8(""))
        self.label8_4.setObjectName(_fromUtf8("label8_4"))
        self.label8_5 = QtGui.QLabel(self.centralwidget)
        self.label8_5.setGeometry(QtCore.QRect(877, 90, 96, 58))
        self.label8_5.setText(_fromUtf8(""))
        self.label8_5.setObjectName(_fromUtf8("label8_5"))
        self.label8_8 = QtGui.QLabel(self.centralwidget)
        self.label8_8.setGeometry(QtCore.QRect(877, 294, 96, 58))
        self.label8_8.setText(_fromUtf8(""))
        self.label8_8.setObjectName(_fromUtf8("label8_8"))
        self.label8_6 = QtGui.QLabel(self.centralwidget)
        self.label8_6.setGeometry(QtCore.QRect(877, 158, 96, 58))
        self.label8_6.setText(_fromUtf8(""))
        self.label8_6.setObjectName(_fromUtf8("label8_6"))
        self.label8_7 = QtGui.QLabel(self.centralwidget)
        self.label8_7.setGeometry(QtCore.QRect(877, 226, 96, 58))
        self.label8_7.setText(_fromUtf8(""))
        self.label8_7.setObjectName(_fromUtf8("label8_7"))
        self.label2_1 = QtGui.QLabel(self.centralwidget)
        self.label2_1.setGeometry(QtCore.QRect(497, 192, 96, 58))
        self.label2_1.setText(_fromUtf8(""))
        self.label2_1.setObjectName(_fromUtf8("label2_1"))
        self.label2_2 = QtGui.QLabel(self.centralwidget)
        self.label2_2.setGeometry(QtCore.QRect(664, 192, 96, 58))
        self.label2_2.setText(_fromUtf8(""))
        self.label2_2.setObjectName(_fromUtf8("label2_2"))
        self.team_1 = QtGui.QLabel(self.centralwidget)
        self.team_1.setGeometry(QtCore.QRect(4, 140, 96, 58))
        self.team_1.setAlignment(QtCore.Qt.AlignCenter)
        self.team_1.setObjectName(_fromUtf8("team_1"))
        self.team_2 = QtGui.QLabel(self.centralwidget)
        self.team_2.setGeometry(QtCore.QRect(136, 140, 96, 58))
        self.team_2.setAlignment(QtCore.Qt.AlignCenter)
        self.team_2.setObjectName(_fromUtf8("team_2"))
        self.VS_label = QtGui.QLabel(self.centralwidget)
        self.VS_label.setGeometry(QtCore.QRect(100, 140, 36, 58))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.VS_label.setFont(font)
        self.VS_label.setAlignment(QtCore.Qt.AlignCenter)
        self.VS_label.setObjectName(_fromUtf8("VS_label"))
        self.team_3 = QtGui.QLabel(self.centralwidget)
        self.team_3.setGeometry(QtCore.QRect(4, 198, 96, 58))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.team_3.setFont(font)
        self.team_3.setAlignment(QtCore.Qt.AlignCenter)
        self.team_3.setObjectName(_fromUtf8("team_3"))
        self.team_4 = QtGui.QLabel(self.centralwidget)
        self.team_4.setGeometry(QtCore.QRect(136, 198, 96, 58))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.team_4.setFont(font)
        self.team_4.setAlignment(QtCore.Qt.AlignCenter)
        self.team_4.setObjectName(_fromUtf8("team_4"))
        self.VS_label_2 = QtGui.QLabel(self.centralwidget)
        self.VS_label_2.setGeometry(QtCore.QRect(100, 198, 36, 58))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.VS_label_2.setFont(font)
        self.VS_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.VS_label_2.setObjectName(_fromUtf8("VS_label_2"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 256, 236, 147))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.teamsLabel = QtGui.QLabel(self.centralwidget)
        self.teamsLabel.setGeometry(QtCore.QRect(0, 444, 613, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.teamsLabel.setFont(font)
        self.teamsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.teamsLabel.setObjectName(_fromUtf8("teamsLabel"))
        self.personalLabel = QtGui.QLabel(self.centralwidget)
        self.personalLabel.setGeometry(QtCore.QRect(613, 444, 411, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.personalLabel.setFont(font)
        self.personalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.personalLabel.setObjectName(_fromUtf8("personalLabel"))
        self.teamList_2 = QtGui.QTableWidget(self.centralwidget)
        self.teamList_2.setGeometry(QtCore.QRect(613, 484, 411, 284))
        self.teamList_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.teamList_2.setAlternatingRowColors(True)
        self.teamList_2.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.teamList_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.teamList_2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.teamList_2.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.teamList_2.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.teamList_2.setShowGrid(True)
        self.teamList_2.setGridStyle(QtCore.Qt.NoPen)
        self.teamList_2.setRowCount(10)
        self.teamList_2.setObjectName(_fromUtf8("teamList_2"))
        self.teamList_2.setColumnCount(4)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teamList_2.setHorizontalHeaderItem(3, item)
        self.teamList_2.horizontalHeader().setCascadingSectionResizes(True)
        self.teamList_2.horizontalHeader().setDefaultSectionSize(50)
        self.teamList_2.horizontalHeader().setHighlightSections(False)
        self.teamList_2.horizontalHeader().setMinimumSectionSize(32)
        self.teamList_2.horizontalHeader().setSortIndicatorShown(True)
        self.teamList_2.setColumnWidth(0,100)
        self.teamList_2.setColumnWidth(1,130)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "2014 FIFA World Cup", None))
        self.background.setPixmap(QtGui.QPixmap('./image/background.jpg'))
        self.teamList.setSortingEnabled(True)
        item = self.teamList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Gp", None))
        item = self.teamList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Team", None))
        item = self.teamList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "W", None))
        item = self.teamList.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D", None))
        item = self.teamList.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "L", None))
        item = self.teamList.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "GF", None))
        item = self.teamList.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "GA", None))
        item = self.teamList.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "GD", None))
        item = self.teamList.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Pts", None))
        self.dateBoard.setText(_translate("MainWindow", "赛程日期", None))
        self.playingGame.setText(_translate("MainWindow", "等待比赛开始...", None))
        self.beginBTN.setText(_translate("MainWindow", "开始比赛", None))
        self.speedBTN.setText(_translate("MainWindow", "1X 倍速", None))
        self.team_1.setText(_translate("MainWindow", "对战球队", None))
        self.team_2.setText(_translate("MainWindow", "对战球队", None))
        self.VS_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">V</p><p align=\"center\">S</p></body></html>", None))
        self.team_3.setText(_translate("MainWindow", "0", None))
        self.team_4.setText(_translate("MainWindow", "0", None))
        self.VS_label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">:</p></body></html>", None))
        self.teamsLabel.setText(_translate("MainWindow", "队伍排名", None))
        self.personalLabel.setText(_translate("MainWindow", "个人排名", None))
        self.teamList_2.setSortingEnabled(True)
        item = self.teamList_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.teamList_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Team", None))
        item = self.teamList_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Pos", None))
        item = self.teamList_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "G", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
