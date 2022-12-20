'''
Created on 1 nov. 2022

@author: engelus
'''

import sys
from PyQt5.QtWidgets import  QApplication
from Vistas.vLogin import ventanaLogin
import sys
import os
from Vistas.vCRUDpeli import *
BD = "./Cinemar.db"
ICON = "./Assets/cine.png"

app = QApplication(sys.argv)
mainwindow = PantallaModi()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")