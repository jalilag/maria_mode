from PyQt5.QtWidgets import QWidget,QLabel,QInputDialog,QFileDialog
from PyQt5.QtGui import QPixmap,QTransform
from PyQt5.QtCore import Qt,pyqtSignal
from functools import partial
import time
import os
from pynput.mouse import Listener
import pynput.mouse as pymouse
import pynput.keyboard as pykeyboard

class Signals:
	def sig_create_user(self,items):
		i = self.content_grid.get_widget_by_pos(1,0).currentIndex()
		prenom = self.content_grid.get_widget_by_pos(2,1).text()
		nom = self.content_grid.get_widget_by_pos(2,3).text()
		tel1 = self.content_grid.get_widget_by_pos(3,1).text()		
		tel2 = self.content_grid.get_widget_by_pos(3,3).text()		
		adresse = self.content_grid.get_widget_by_pos(5,0).toPlainText()
		if self.error_manage(1,self.check_is_empty(prenom),"Prenom"): return
		if self.error_manage(1,self.check_is_empty(nom),"Nom"): return
		if i == 0:
			self.bdd_curs.insert("users",["firstname","lastname","phone1","phone2","address"],[prenom,nom,tel1,tel2,adresse])
		else:
			self.bdd_curs.update("users",["firstname","lastname","phone1","phone2","address"],[prenom,nom,tel1,tel2,adresse],'user_id='+str(items[i]))
		self.view_box_client_add()

	def sig_load_client(self,items):
		grid = self.content_grid
		i = grid.get_widget_by_pos(1,0).currentIndex()
		if i > 0:
			data = self.bdd_curs.select("users","firstname,lastname,phone1,phone2,address","user_id="+str(items[i]),print_req =True)[0]		
			grid.get_widget_by_pos(2,1).setText(data[0])
			grid.get_widget_by_pos(2,3).setText(data[1])
			grid.get_widget_by_pos(3,1).setText(data[2])
			grid.get_widget_by_pos(3,3).setText(data[3])
			grid.get_widget_by_pos(5,0).setPlainText(data[4])
