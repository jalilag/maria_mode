import os
import pandas as pd
from functools import partial

class Views:
	def view_menu(self):
		self.menu_grid.addWidget(self.u.UQtxt("MENU_STD_TITLE",title="Choisissez une action"))
		# self.menu_grid.addWidget(self.u.UQbut("MENU_STD_BUT",title="Import de fichier",connect2=["clicked",self.view_add_processing]))
		self.menu_grid.addWidget(self.u.UQbut("MENU_STD_BUT",title="Info client",connect2=["clicked",self.view_box_client_add]))
	
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
		# grid.addWidget(self.u.UQtxt(style="label",title="Description du modèle"),6,0)
		# grid.addWidget(self.u.UQplaintxtedit(style="field"),7,0,1,grid.columnCount())
		# grid.addWidget(self.u.UQtxt(style="label",title="Prix en Dirham"),8,0)
		# grid.addWidget(self.u.UQtxtedit(style="field"),8,1)
		# grid.addWidget(self.u.UQtxt(style="label",title="Avance reçue en Dirham"),8,2)
		# grid.addWidget(self.u.UQtxtedit(style="field"),8,3)
		# grid.addWidget(self.u.UQtxt(style="label",title="Veuillez remplir les informations suivantes"),1,0,1,grid.columnCount())
		self.content_grid.addWidget(self.u.UQtxt("BOX_STD_TITLE",title="Info client"),0,0,1,grid.columnCount())
		# grid.addWidget(self.u.UQtxt("SUBBOX_STD_TITLE",title="Base de conception"),0,0,1,grid.columnCount())




				

