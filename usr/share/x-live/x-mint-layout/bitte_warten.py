import sys 
import os
import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                             QLineEdit, QListWidget, QPushButton, QSlider, 
                             QVBoxLayout, QWidget, QMessageBox)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        faktor = app.desktop().height()/720
        self.faktor = app.desktop().height()/720
        breite = int(250 * faktor)
        hoehe = int(60 * faktor)
        bts=int(16 * faktor)
        sts=int(24 * faktor)
        btn_sel_color = '#1f8973'
        pos_x = int((app.desktop().width()-breite)/2)
        pos_y = int((app.desktop().height()-hoehe)/2)
        # color yellow #635313
        # color green #0ca057
      
        #  StyleSheet 
        
        self.ssbtn1=str("""
            QWidget {
            background-color: #130343;
            }
            QLabel {
            font-size: """ + str(sts) + """px; 
            text-align: left;      
            border-radius: 10px;
            background-color: """ + btn_sel_color  + """;
            border: 2px solid """ + btn_sel_color  + """;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            """)
            

        # Erstelle ein Layout für das Hauptfenster
        layout = QVBoxLayout()
        self.label = QLabel("bitte warten", self)
        self.label.setStyleSheet(self.ssbtn1)
        layout.addWidget(self.label)

        # Setze das Layout für das Hauptfenster
        self.setLayout(layout)

        self.setWindowTitle('ComboBox Beispiel')
        self.setGeometry(pos_x, pos_y,breite,hoehe)
        self.setWindowIcon(QIcon.fromTheme('settings'))  # Setze das systemweite Theme-Icon als Fenstericon
        self.setWindowTitle("X-Mint Einstellungstool")
        self.setMinimumSize(breite, hoehe)  # Festlegen der Größe auf 600x400 Pixel
        self.setFixedWidth(breite)
        self.setStyleSheet("background: rgba(80,80, 80, 00);")  # Hintergrundfarbe festlegen

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # Entfernt die Fensterdekoration
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
