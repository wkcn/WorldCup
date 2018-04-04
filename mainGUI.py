# -*- coding: utf-8 -*-

from ui import *
import random
from time import sleep
import sys
from run import MainFunc


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

def qtStr(s):
	if s is None:
		s="N/A"
	try:
		s+" "
		return _translate("MainWindow", s, None)
	except:
		return _translate("MainWindow", str(s), None)


class RunThread(QtCore.QThread):
    def __init__(self,parent=None):
        super(RunThread, self).__init__(parent)
        self.mf = MainFunc()

    def run(self):
    	self.mf.next_step()


class GUI(QtGui.QMainWindow,Ui_MainWindow):
	def __init__(self):
		super(GUI,self).__init__()
		self.setupUi(self)
		self.labels = {
			11 : self.finalLabel,
			21 : self.label2_1,
			22 : self.label2_2,
			41 : self.label4_1,
			42 : self.label4_2,
			43 : self.label4_3,
			44 : self.label4_4,
			81 : self.label8_1,
			82 : self.label8_2,
			83 : self.label8_3,
			84 : self.label8_4,
			85 : self.label8_5,
			86 : self.label8_6,
			87 : self.label8_7,
			88 : self.label8_8,
		}
		self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint|QtCore.Qt.WindowCloseButtonHint)
		self.beginBTN.clicked.connect(self.run)
		self.speedBTN.clicked.connect(self.chageSpeed)
		self.speedBTN.setDisabled(True)


	def setTime(self,par):
		[month,day] = par
		# 月份和日期需要用字符串
		self.dateBoard.setText(qtStr("%s月%s日"%(month,day)))


	def setNowPlaying(self,par):
		if(par=="cln"):
			self.team_1.setText(qtStr(" "))
			self.team_2.setText(qtStr(" "))
			return
		[host,guest] = par
		# 设置对战双方的国旗，国家拼音名
		self.team_1.setPixmap(QtGui.QPixmap('./image/guoqi/%s.png'%host))
		self.team_2.setPixmap(QtGui.QPixmap('./image/guoqi/%s.png'%guest))


	def setPoints(self,par):
		[hp,gp] = par
		# 设置比分，两个数字
		self.team_3.setText(qtStr(str(hp)))
		self.team_4.setText(qtStr(str(gp)))


	def setLive(self,s):
		# 直播板，每句话自动添加到已有文字首
		# cln代表清屏
		if s=="cln":
			self.textEdit.setText(qtStr(""))
			return
		# 这里要用UTF-8的字符串编码，每次添加的字符串会自动换行
		s += self.textEdit.toPlainText().toUtf8()
		self.textEdit.setText(qtStr(s))


	def setPic(self,par):
		# 设置正在对战的国旗，接受一个list，包含两个国家的名字拼音
		[num,team] = par
		# num代表了要更改哪个标签,具体由self.labels里决定
		self.labels[num].setPixmap(QtGui.QPixmap('./image/guoqi/%s.png'%team))


	def fillTeamList(self,teams):
		# 填充队伍排名列表，每个队伍是一个字典，包含以下9个键
		i=0
		for team in teams:
			self.teamList.setItem(i, 0, QtGui.QTableWidgetItem(qtStr(team.info['gp'])))
			self.teamList.setItem(i, 1, QtGui.QTableWidgetItem(qtStr(team.country)))
			self.teamList.setItem(i, 2, QtGui.QTableWidgetItem(qtStr(team.info['w'])))
			self.teamList.setItem(i, 3, QtGui.QTableWidgetItem(qtStr(team.info['d'])))
			self.teamList.setItem(i, 4, QtGui.QTableWidgetItem(qtStr(team.info['l'])))
			self.teamList.setItem(i, 5, QtGui.QTableWidgetItem(qtStr(team.info['gf'])))
			self.teamList.setItem(i, 6, QtGui.QTableWidgetItem(qtStr(team.info['ga'])))
			self.teamList.setItem(i, 7, QtGui.QTableWidgetItem(qtStr(team.info['gd'])))
			self.teamList.setItem(i, 8, QtGui.QTableWidgetItem(qtStr(team.info['pts'])))
			i+=1


	def fillPersonalList(self,people):
		# 填充个人排名列表，每个人是一个字典，包含以下4个键
		i=0

		self.teamList_2.setRowCount(len(people))

		for person in people:
			self.teamList_2.setItem(i, 0, QtGui.QTableWidgetItem(qtStr(person['name'])))
			self.teamList_2.setItem(i, 1, QtGui.QTableWidgetItem(qtStr(person['tm'])))
			self.teamList_2.setItem(i, 2, QtGui.QTableWidgetItem(qtStr(person['pos'])))
			self.teamList_2.setItem(i, 3, QtGui.QTableWidgetItem(qtStr(person['g'])))
			i+=1


	def shake(self,f1,f2):
		b=3
		self.timer=QtCore.QTimer()
		self.shaking = [self.labels[f1],self.labels[f2]]
		(x1,y1) = self.coor1 = (self.labels[f1].x(), self.labels[f1].y())
		(x2,y2) = self.coor2 = (self.labels[f2].x(), self.labels[f2].y())
		def fun():
			x = random.randint(-b, b)
			y = random.randint(-b, b)
			self.shaking[0].move(x1+x, y1+y)
			x = random.randint(-b, b)
			y = random.randint(-b, b)
			self.shaking[1].move(x2+x, y2+y)
		self.timer.timeout.connect(fun)
		self.timer.start(50)


	def stopShaking(self):
		self.timer.stop()
		self.shaking[0].move(self.coor1[0], self.coor1[1])
		self.shaking[1].move(self.coor2[0], self.coor2[1])


	def setTitle(self,title):
		self.playingGame.setText(qtStr(title))


	def cleanPic(self,num):
		for i in range(num):
			self.labels[num*10+1+i].setText(qtStr(" "))


	def chageSpeed(self):
		default = 0.2
		if self.speedBTN.text().toUtf8() == "1X 倍速":
			self.thread.mf.speed = default / 2
			self.speedBTN.setText(qtStr("2X 倍速"))
		elif self.speedBTN.text().toUtf8() == "2X 倍速":
			self.thread.mf.speed = default / 4
			self.speedBTN.setText(qtStr("4X 倍速"))
		elif self.speedBTN.text().toUtf8() == "4X 倍速":
			self.thread.mf.speed = default / 8
			self.speedBTN.setText(qtStr("8X 倍速"))
		elif self.speedBTN.text().toUtf8() == "8X 倍速":
			self.thread.mf.speed = default / 16
			self.speedBTN.setText(qtStr("16X 倍速"))
		elif self.speedBTN.text().toUtf8() == "16X 倍速":
			self.thread.mf.speed = default / 32
			self.speedBTN.setText(qtStr("32X 倍速"))
		elif self.speedBTN.text().toUtf8() == "32X 倍速":
			self.thread.mf.speed = default / 1
			self.speedBTN.setText(qtStr("1X 倍速"))


	def clean(self):
		self.setupUi(self)
		self.beginBTN.clicked.connect(self.run)
		self.speedBTN.clicked.connect(self.chageSpeed)
		self.speedBTN.setDisabled(True)


	def end(self):
		self.beginBTN.setDisabled(False)
		self.speedBTN.setDisabled(True)


	def run(self):
		if self.beginBTN.text().toUtf8() == "开始比赛":
			self.thread = RunThread()
			self.thread.mf.setPicSignal.connect(self.setPic)
			self.thread.mf.fillTeamListSignal.connect(self.fillTeamList)
			self.thread.mf.fillPersonalListSignal.connect(self.fillPersonalList)
			self.thread.mf.setTimeSignal.connect(self.setTime)
			self.thread.mf.setPointsSignal.connect(self.setPoints)
			self.thread.mf.setNowPlayingSignal.connect(self.setNowPlaying)
			self.thread.mf.setLiveSignal.connect(self.setLive)
			self.thread.mf.endSignal.connect(self.end)
			self.thread.mf.setTitleSignal.connect(self.setTitle)
			self.thread.start()
			self.beginBTN.setText(qtStr("清空数据"))
			self.beginBTN.setDisabled(True)
			self.speedBTN.setDisabled(False)
		else:
			self.clean()
			self.beginBTN.setText(qtStr("开始比赛"))


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon("./image/logo.png"))
	splash=QtGui.QSplashScreen(QtGui.QPixmap("./image/logo.png"))
	splash.show()
	app.processEvents()
	MainWindow = GUI()
	sleep(3)
	MainWindow.show()
	splash.finish(MainWindow)
	sys.exit(app.exec_())