import sys, os, time, uuid, hashlib, re
from PyQt5 import QtCore, QtGui, uic  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QComboBox, QTextEdit 
import smtplib
import imghdr
from email.message import EmailMessage



import sqlite3     #this connects the database to the program 
con = sqlite3.connect('premresults.db') #this calls the name of the database file, must be stored in the same place as py file, or directory path needed here
cur = con.cursor() #creates the cursor that can 'search' through the database for quieries 


cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))


winMain = uic.loadUiType("premLeagueHome.ui") [0]  ##this links the userinterface files to the program
emailWin = uic.loadUiType("emails.ui") [0]


class HomeScreen(QtWidgets.QMainWindow, winMain): #imports the PyQT 'main window' functionality, winMain links to UI screens above

	def __init__(self): #this is the 'attritbutes' section of the class, always started with the __init__ method
		QtWidgets.QMainWindow.__init__(self) ##setting the screen up, defining where the buttons are linking to, and where text box information is being stored 
		self.setupUi(self) #sets up the UI funnily enough!
		self.clearBtn.clicked.connect(self.clearForm) #creates a click even to intiate the method associated to that button, eg submit
		self.emailResBtn.clicked.connect(self.emailResults)
		self.liverpoolBtn.clicked.connect(self.liverpoolRes)
		self.manCityBtn.clicked.connect(self.manCityRes)
		self.chelseaBtn.clicked.connect(self.chelseaRes)
		self.tottenhamBtn.clicked.connect(self.tottenhamRes)
		self.westHamBtn.clicked.connect(self.westHamRes)
		self.arsenalBtn.clicked.connect(self.arsenalRes)
		self.manUtdBtn.clicked.connect(self.manUtdRes)
		self.newcastleBtn.clicked.connect(self.newcastleRes)


	def clearForm(self):
		self.cpointLbl.setText(" ")
		self.gdrawnLbl.setText(" ")
		self.glostLbl.setText(" ")
		self.gwonLbl.setText(" ")
		self.playLbl.setText(" ")
		self.posLbl.setText(" ")
		self.logoLbl.setPixmap(QtGui.QPixmap("footballLogo.png"))

	def emailResults(self):
		
		self.hide()
		self.newWindow = emailScreen
		self.newWindow.show()

	def liverpoolRes(self):
		currentTeam.teamsID = 3
		currentTeam.getInfo(currentTeam.teamsID)
		self.cpointLbl.setText(str(currentTeam.points))
		self.gdrawnLbl.setText(str(currentTeam.drawn))
		self.glostLbl.setText(str(currentTeam.lost))
		self.gwonLbl.setText(str(currentTeam.won))
		self.playLbl.setText(str(currentTeam.played))
		self.posLbl.setText(str(currentTeam.position))
		self.logoLbl.setPixmap(QtGui.QPixmap("%s" %currentTeam.logo))

	def manCityRes(self):
		currentTeam.teamsID = 4
		currentTeam.getInfo(currentTeam.teamsID)
		self.cpointLbl.setText(str(currentTeam.points))
		self.gdrawnLbl.setText(str(currentTeam.drawn))
		self.glostLbl.setText(str(currentTeam.lost))
		self.gwonLbl.setText(str(currentTeam.won))
		self.playLbl.setText(str(currentTeam.played))
		self.posLbl.setText(str(currentTeam.position))
		self.logoLbl.setPixmap(QtGui.QPixmap("%s" %currentTeam.logo))

	def chelseaRes(self):
		currentTeam.teamsID = 2
		currentTeam.getInfo(currentTeam.teamsID)
		self.cpointLbl.setText(str(currentTeam.points))
		self.gdrawnLbl.setText(str(currentTeam.drawn))
		self.glostLbl.setText(str(currentTeam.lost))
		self.gwonLbl.setText(str(currentTeam.won))
		self.playLbl.setText(str(currentTeam.played))
		self.posLbl.setText(str(currentTeam.position))
		self.logoLbl.setPixmap(QtGui.QPixmap("%s" %currentTeam.logo))

	def tottenhamRes(self):
		currentTeam.teamsID = 7
		currentTeam.getInfo(currentTeam.teamsID)
		self.cpointLbl.setText(str(currentTeam.points))
		self.gdrawnLbl.setText(str(currentTeam.drawn))
		self.glostLbl.setText(str(currentTeam.lost))
		self.gwonLbl.setText(str(currentTeam.won))
		self.playLbl.setText(str(currentTeam.played))
		self.posLbl.setText(str(currentTeam.position))
		self.logoLbl.setPixmap(QtGui.QPixmap("%s" %currentTeam.logo))

	def arsenalRes(self):
		currentTeam.teamsID = 1
		currentTeam.getInfo(currentTeam.teamsID)
		self.cpointLbl.setText(str(currentTeam.points))
		self.gdrawnLbl.setText(str(currentTeam.drawn))
		self.glostLbl.setText(str(currentTeam.lost))
		self.gwonLbl.setText(str(currentTeam.won))
		self.playLbl.setText(str(currentTeam.played))
		self.posLbl.setText(str(currentTeam.position))
		self.logoLbl.setPixmap(QtGui.QPixmap("%s" %currentTeam.logo))

	def newcastleRes(self):
		currentTeam.teamsID = 6
		currentTeam.getInfo(currentTeam.teamsID)
		self.cpointLbl.setText(str(currentTeam.points))
		self.gdrawnLbl.setText(str(currentTeam.drawn))
		self.glostLbl.setText(str(currentTeam.lost))
		self.gwonLbl.setText(str(currentTeam.won))
		self.playLbl.setText(str(currentTeam.played))
		self.posLbl.setText(str(currentTeam.position))
		self.logoLbl.setPixmap(QtGui.QPixmap("%s" %currentTeam.logo))

	def westHamRes(self):
		currentTeam.teamsID = 8
		currentTeam.getInfo(currentTeam.teamsID)
		self.cpointLbl.setText(str(currentTeam.points))
		self.gdrawnLbl.setText(str(currentTeam.drawn))
		self.glostLbl.setText(str(currentTeam.lost))
		self.gwonLbl.setText(str(currentTeam.won))
		self.playLbl.setText(str(currentTeam.played))
		self.posLbl.setText(str(currentTeam.position))
		self.logoLbl.setPixmap(QtGui.QPixmap("%s" %currentTeam.logo))

	def manUtdRes(self):
		currentTeam.teamsID = 5
		currentTeam.getInfo(currentTeam.teamsID)
		self.cpointLbl.setText(str(currentTeam.points))
		self.gdrawnLbl.setText(str(currentTeam.drawn))
		self.glostLbl.setText(str(currentTeam.lost))
		self.gwonLbl.setText(str(currentTeam.won))
		self.playLbl.setText(str(currentTeam.played))
		self.posLbl.setText(str(currentTeam.position))
		self.logoLbl.setPixmap(QtGui.QPixmap("%s" %currentTeam.logo))


class EmailScreen(QtWidgets.QMainWindow, emailWin): #imports the PyQT 'main window' functionality, winMain links to UI screens above

	def __init__(self): #this is the 'attritbutes' section of the class, always started with the __init__ method
		QtWidgets.QMainWindow.__init__(self) ##setting the screen up, defining where the buttons are linking to, and where text box information is being stored 
		self.setupUi(self) #sets up the UI funnily enough!
		self.clearBtn.clicked.connect(self.clearForm)
		self.sendBtn.clicked.connect(self.sendE)
		#self.email_a = self.email_add.text()
		#self.email_p = self.email_pass.text()
		#self.email_t = self.email_to.text()
		#self.subject = self.subject.text()
		#self.extraMsg = self.extraMsg.toPlainText()
		

	def clearForm(self):
		self.email_add.clear()
		self.email_pass.clear()
		self.email_to.clear()
		self.subject.clear()
		self.extraMsg.clear()

	def sendE(self):
		
		user1.email_add = self.email_add.text()
		user1.email_pass = self.email_pass.text()
		user1.email_to = self.email_to.text()
		print(user1.email_to, "hello")
		user1.subject = self.subject.text()
		user1.extraMsg = self.extraMsg.toPlainText()
		email1.emailConfirmation()

		return user1.email_add, user1.email_pass, user1.email_to, user1.subject, user1.extraMsg
		#message box


class SendEmail():
	def __init__(self):
		#self.email_address = os.environ.get('EMAIL_USER')
		#self.email_pass = os.environ.get('EMAIL_PASS')
		self.sentEmails = 0

	def emailConfirmation(self):
		self.email_pass = user1.email_pass
		self.email_address = user1.email_add

		subject = user1.subject
		body = f'Team: {currentTeam.teamName} \n Position: {currentTeam.position} \n Points: {currentTeam.points}'
		extraMs = user1.extraMsg
		msg = f'Subject: {subject} \n\n {body} \n\n {extraMs}'
		messageSent = 0
		while messageSent == 0:
			smtp = smtplib.SMTP('smtp.gmail.com', 587)

			smtp.ehlo()
			smtp.starttls()
			smtp.login(self.email_address, self.email_pass)
			smtp.sendmail(self.email_address, user1.email_to, msg)
			smtp.close()
  
			messageSent = 1
			self.sendEmails += 1
			break

class Team(): #team class that will hold the informaiton coming back from the database
	def __init__(self, teamName, position, won, played,lost,points):
		self.teamName = teamName
		self.position = position
		self.won = won
		self.drawn = played
		self.lost = lost
		self.points = points
		self.teamsID = 0
		self.logo = " "

	def getInfo(self, teamsID):
		print(teamsID)
		cur.execute(""" SELECT * FROM premstats WHERE teamID = "%d" """ % (teamsID))

		returned = cur.fetchall()
		print(returned)
		if returned != None or len(returned) < 7:
			self. teamID, self.teamName, self.position, self.played, self.won, self.drawn, self.lost, self.points, self.logo = returned[0]

		else: 
			QtWidgets.QMessageBox.information(self,"error","Nothing found in database", QMessageBox.Ok)


		return self.position, self.played, self.played, self.won, self.drawn, self.lost, self.points, self.logo


class CurrentUser():
	def __init__(self, email_add, email_pass, email_to, subject, extraMsg):
		self.email_add = email_add
		self.email_pass = email_pass
		self.email_to = email_to
		self.subject = subject
		self.extraMsg = extraMsg

	def createEmail():
		pass

currentTeam = Team(" "," ", " ", " ", " ", " ") #creates a current team object with no information 
user1 = CurrentUser(" ", " "," "," "," ")
email1 = SendEmail()


app = QtWidgets.QApplication(sys.argv) #think of this as the 'main ()' section in procedural programming. Allows you to call the program into action 
winMain = HomeScreen()
emailScreen = EmailScreen()

winMain.show()
app.exec_()
