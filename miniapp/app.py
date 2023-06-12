#app.py
import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
from mini import MyWindow
from PyQt5.QtGui import QFontDatabase,QFont
app = QApplication(sys.argv)
app.setStyle('Fusion')

mw = MyWindow("관광지 추천")
mw.setStyleSheet("background-color:skyblue ;")

mw.show()
sys.exit(app.exec())

