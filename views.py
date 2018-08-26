import os
import pandas as pd
from functools import partial

class Views:
	def view_menu(self):
		self.menu_grid.addWidget(self.u.UQtxt("MENU_STD_TITLE",title="Choisissez une action"))
		# self.menu_grid.addWidget(self.u.UQbut("MENU_STD_BUT",title="Import de fichier",connect2=["clicked",self.view_add_processing]))
		self.menu_grid.addWidget(self.u.UQbut("MENU_STD_BUT",title="Info client",connect2=["clicked",self.view_box_client_add]))
		self.menu_grid.addWidget(self.u.UQbut("MENU_STD_BUT",title="Mesures",connect2=["clicked",self.view_box_client_measures]))
	
	def view_box_client_add(self):
		self.tools_remove_items(self.content_grid)
		grid = self.content_grid
		items = self.bdd_curs.request("SELECT user_id, printf('%s %s',firstname,lastname) as name FROM users")
		items.insert(0,[0,"Nouveau client"])
		items= list(map(list,zip(*items)))
		grid.addWidget(self.u.UQcombo(style="field",items=items[1],connect2=["changed",partial(self.sig_load_client,items[0])]),1,0,1,2)
		grid.addWidget(self.u.UQtxt(style="label",title="Prénom"),2,0)		
		grid.addWidget(self.u.UQtxtedit(style="field"),2,1)
		grid.addWidget(self.u.UQtxt(style="label",title="Nom"),2,2)
		grid.addWidget(self.u.UQtxtedit(style="field"),2,3)
		grid.addWidget(self.u.UQtxt(style="label",title="Téléphone 1"),3,0)
		grid.addWidget(self.u.UQtxtedit(style="field"),3,1)		
		grid.addWidget(self.u.UQtxt(style="label",title="Téléphone 2"),3,2)
		grid.addWidget(self.u.UQtxtedit(style="field"),3,3)
		grid.addWidget(self.u.UQtxt(style="label",title="Adresse"),4,0)
		grid.addWidget(self.u.UQplaintxtedit(style="field"),5,0,1,grid.columnCount())
		grid.addWidget(self.u.UQbut("STD_BUTTON",title="Sauvegarder",connect2=["clicked",partial(self.sig_create_user,items[0])]),6,0)
		grid.addWidget(self.u.UQtxt("BOX_STD_TITLE",title="Info client"),0,0,1,grid.columnCount())

	def view_box_client_measure(self):
		self.tools_remove_items(self.content_grid)
		grid = self.content_grid
		items = self.bdd_curs.request("SELECT user_id, printf('%s %s',firstname,lastname) as name FROM users")
		items.insert(0,[0,"Nouveau client"])
		items= list(map(list,zip(*items)))
		grid.addWidget(self.u.UQcombo(style="field",items=items[1],connect2=["changed",partial(self.sig_load_client,items[0])]),1,0,1,2)
		grid.addWidget(self.u.UQtxt("BOX_STD_TITLE",title="Info client"),0,0,1,grid.columnCount())

	def view_box_client_measures(self,user_id = None):
		self.tools_remove_items(self.content_grid)
		grid = self.content_grid
		items = self.bdd_curs.request("SELECT printf('%s %s',firstname,lastname) as name, cast(user_id as text) FROM users")
		w = self.u.UQcombo(style="field",items=items,connect2=["changed",self.sig_load_measures])
		# print(list(map(list,zip(*items)))[1].index(user_id))
		if user_id is False: user_id = items[0][1]
		else:
			w.setCurrentIndex(list(map(list,zip(*items)))[1].index(str(user_id)))
		grid.addWidget(w,1,0,1,3) 
		measures = self.bdd_curs.request("""
			SELECT title,value,md.mid FROM measures_desc as md 
			LEFT JOIN measures m ON m.mid = md.mid and m.user_id = """ + str(user_id) + """
			ORDER BY rank
		""")
		for i in range(len(measures)):
			grid.addWidget(self.u.UQtxt(style="label",title=measures[i][0]),2+i,0)
			grid.addWidget(self.u.UQtxtedit(name_id=measures[i][2],style="label",title=measures[i][1]),2+i,1)
			grid.addWidget(self.u.UQtxt(style="label",title="cm"),2+i,2)
		i += 3
		grid.addWidget(self.u.UQbut("STD_BUTTON",title="Sauvegarder",connect2=["clicked",self.sig_save_measures]),i,0)
		grid.addWidget(self.u.UQtxt("BOX_STD_TITLE",title="Mesures"),0,0,1,grid.columnCount())