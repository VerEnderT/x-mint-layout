import sys
import subprocess, os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider, QLineEdit, QListWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap


# Pfad zum gewünschten Arbeitsverzeichnis
arbeitsverzeichnis = os.path.expanduser('/usr/share/x-live/x-mint-layout')

# Das Arbeitsverzeichnis festlegen
os.chdir(arbeitsverzeichnis)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        #  skalierungsberechnung
        self.faktor=app.desktop().height()/720
        self.breite = int(470*self.faktor)
        self.hoehe = int(400*self.faktor)
        bts=int(16*self.faktor)
        sts=int(12*self.faktor)
        x = int(app.desktop().width()/2-self.breite/2)
        y = int(app.desktop().height()/2-self.hoehe/2)
        btn_sel_color = "#0ca057"
      
        #  StyleSheet für kategorieButtons
        self.ssbtn=str("""
            QPushButton {
            font-size: """ + str(sts) + """px; 
            text-align: left;      
            border-radius: 10px;
            background-color: #131313;
            border: 5px solid #131313;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(sts)/12*18)) + """px;  
            background-color: #1b1b1b;
            border: 5px solid #1b1b1b;
            }
            """)
        
        self.ssbtn1=str("""
            QPushButton {
            font-size: """ + str(int(sts*1.1)) + """px; 
            text-align: center;      
            border-radius: 10px;
            background-color: #131313;
            border: 0px solid #131313;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(sts*1.3)) + """px;  
            background-color: #1b1b1b;
            border: 0px solid #1b1b1b;
            }
            """)
            
        self.ssbtn2=str("""
            QWidget {
            background-color: #130343;
            }
            QPushButton {
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
            QPushButton:hover {
            font-size: """ + str(int(int(sts)/14*15)) + """px;  
            background-color: #1b1b1b;
            border: 2px solid #1b1b1b;
            }
            """)
        
        #  StyleSheet für Kategorieinhalt
        self.sscat=str("""
            QWidget {
            font-size: """ + str(sts) + """px; 
            text-align: left;      
            border-radius: 10px;
            background-color: #232323;
            border: 0px solid #131313;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton {
            font-size: """ + str(sts) + """px; 
            text-align: left;      
            border-radius: """ + str(int(int(sts)/2)) + """px;
            background-color: #232323;
            border: 0px solid #030303;
            padding-top: 2px;
            padding-left: 5px;
            padding-right: 5px;
            padding-bottom: 2px;
            color: white;
            }
            QPushButton:hover {
            font-size: """ + str(int(int(sts)/12*18)) + """px;  
            background-color: #2b2b2b;
            border: 0px solid #2b2b2b;
            }
            """)

        mainLayout = QHBoxLayout() 
        oberlayout = QVBoxLayout()
        self.title_pic = QLabel(self)
        pixmap = QPixmap('./images/title.png')
        self.pb = int(int(self.breite) * 0.95)
        self.ph = int(self.pb / 4.25)
        self.title_pic.setPixmap(pixmap.scaled(self.pb, self.ph))
        self.title_pic.setStyleSheet("background: rgba(80,80, 80, 0);")
        oberlayout.addWidget(self.title_pic)
        oberlayout.addLayout(mainLayout)
        self.setLayout(oberlayout)
        #self.setLayout(mainLayout)

        categoryLayout = QVBoxLayout()
        mainLayout.addLayout(categoryLayout)

        contentLayout = QVBoxLayout()
        mainLayout.addLayout(contentLayout)
        
        categories = ["Default", "Duo", "Comunity", "Oldschool"]

        # Erstellen der Kategorie-Buttons
        self.categoryButtons = []
        for category in categories:
            button = QPushButton(category)
            button.setFixedWidth(int(100*self.faktor))  # Kategorienbreite auf 150px festlegen
            button.setStyleSheet(self.ssbtn)  # stylesheet für kategoriebutton festlegen
            button.clicked.connect(lambda checked, cat=category: self.onCategoryClicked(cat))
            categoryLayout.addWidget(button)
            self.categoryButtons.append(button)

        categoryLayout.addStretch(1)  # Elastischer Bereich am Ende des categoryLayout

        self.contents = {"Default": self.createContent1,
                         "Duo": self.createContent2,
                         "Comunity": self.createContent3,
                         "Oldschool": self.createContent4}

        self.contentWidget = None
     
        self.setWindowIcon(QIcon('./images/x-mint-layout.png'))  # Setze das systemweite Theme-Icon als Fenstericon
        self.setWindowTitle("X-Mint Desktop-Layouts")
        self.setGeometry(x , y, self.breite, self.hoehe)
        self.setFixedSize(self.breite, self.hoehe)  # Festlegen der Größe auf 600x400 Pixel    
        self.setStyleSheet("background-color: rgba(80, 80, 80, 35);")  # Hintergrundfarbe festlegen0
        self.setWindowOpacity(0.95) # komplettes fenster transparenz
        self.show()

        # Die erste Kategorie standardmäßig auswählen
        if self.categoryButtons:
            self.categoryButtons[0].click()

    def createContent1(self):
        for x in self.categoryButtons:
            x.setStyleSheet(self.ssbtn)
        self.categoryButtons[0].setStyleSheet(self.ssbtn2)
        layout1 = QLabel(self)
        pixmap = QPixmap('/usr/share/x-live/layouts/images/X-Mint.png')
        layout1.setPixmap(pixmap.scaled(int(327*self.faktor), int(185*self.faktor) ))
        layout1.setStyleSheet("background: rgba(180,180, 180, 150);")
        layout1.setFixedHeight(int(190*self.faktor))
        layout1.setFixedWidth(int(327*self.faktor))
        Title = QLabel(self,text="X-Mint Default")
        Title.setStyleSheet(self.sscat)
        Description = QLabel(self,text="Default ist das Standartdesign von X-Mint\n")
        Description.setStyleSheet(self.ssbtn)

        button = QPushButton(self,text="anwenden")
        button.setFixedSize(int(80*self.faktor), int(20*self.faktor))  
        button.setStyleSheet(self.ssbtn1)  
        button.clicked.connect(lambda: self.activate_layout("X-Mint"))

        title_button_layout= QHBoxLayout()

        title_button_layout.addWidget(Title)
        title_button_layout.addStretch()
        title_button_layout.addWidget(button)

        layout = QVBoxLayout()
        layout.addWidget(layout1)
        layout.addLayout(title_button_layout)
        layout.addWidget(Description)

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(self.sscat)

        return widget

    def createContent2(self):
        for x in self.categoryButtons:
            x.setStyleSheet(self.ssbtn)
        self.categoryButtons[1].setStyleSheet(self.ssbtn2)
        layout1 = QLabel(self)
        pixmap = QPixmap('/usr/share/x-live/layouts/images/X-Mint-Duo.png')
        layout1.setPixmap(pixmap.scaled(int(327*self.faktor), int(185*self.faktor) ))
        layout1.setStyleSheet("background: rgba(180,180, 180, 150);")
        layout1.setFixedHeight(int(190*self.faktor))
        layout1.setFixedWidth(int(327*self.faktor))
        Title = QLabel(self,text="X-Mint Duo")
        Title.setStyleSheet(self.sscat)
        Description = QLabel(self,text="Duo ist an das Layout von MacOs angelehnt.\n")
        Description.setStyleSheet(self.ssbtn)

        button = QPushButton(self,text="anwenden")
        button.setFixedSize(int(80*self.faktor), int(20*self.faktor))  
        button.setStyleSheet(self.ssbtn1)  
        button.clicked.connect(lambda: self.activate_layout("X-Mint-Duo"))

        title_button_layout= QHBoxLayout()

        title_button_layout.addWidget(Title)
        title_button_layout.addStretch()
        title_button_layout.addWidget(button)

        layout = QVBoxLayout()
        layout.addWidget(layout1)
        layout.addLayout(title_button_layout)
        layout.addWidget(Description)

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(self.sscat)

        return widget

    def createContent3(self):
        for x in self.categoryButtons:
            x.setStyleSheet(self.ssbtn)
        self.categoryButtons[2].setStyleSheet(self.ssbtn2)
        layout1 = QLabel(self)
        pixmap = QPixmap('/usr/share/x-live/layouts/images/X-Mint-Comunity.png')
        layout1.setPixmap(pixmap.scaled(int(327*self.faktor), int(185*self.faktor) ))
        layout1.setStyleSheet("background: rgba(180,180, 180, 150);")
        layout1.setFixedHeight(int(190*self.faktor))
        layout1.setFixedWidth(int(327*self.faktor))
        Title = QLabel(self,text="X-Mint Comunity")
        Title.setStyleSheet(self.sscat)
        Description = QLabel(self,text="Comunity ist dem Layout von Ubuntu nachempfunden\n")
        Description.setStyleSheet(self.ssbtn)

        button = QPushButton(self,text="anwenden")
        button.setFixedSize(int(80*self.faktor), int(20*self.faktor))  
        button.setStyleSheet(self.ssbtn1)  
        button.clicked.connect(lambda: self.activate_layout("X-Mint-Comunity"))

        title_button_layout= QHBoxLayout()

        title_button_layout.addWidget(Title)
        title_button_layout.addStretch()
        title_button_layout.addWidget(button)

        layout = QVBoxLayout()
        layout.addWidget(layout1)
        layout.addLayout(title_button_layout)
        layout.addWidget(Description)

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(self.sscat)

        return widget
        
    def createContent4(self):
        for x in self.categoryButtons:
            x.setStyleSheet(self.ssbtn)
        self.categoryButtons[3].setStyleSheet(self.ssbtn2)
        layout1 = QLabel(self)
        pixmap = QPixmap('/usr/share/x-live/layouts/images/X-Mint-Oldschool.png')
        layout1.setPixmap(pixmap.scaled(int(327*self.faktor), int(185*self.faktor) ))
        layout1.setStyleSheet("background: rgba(180,180, 180, 150);")
        layout1.setFixedHeight(int(190*self.faktor))
        layout1.setFixedWidth(int(327*self.faktor))
        Title = QLabel(self,text="X-Mint Oldschool")
        Title.setStyleSheet(self.sscat)
        Description = QLabel(self,text="Oldschool ist ähnlich früheren Windows Layout.\n")
        Description.setStyleSheet(self.ssbtn)

        button = QPushButton(self,text="anwenden")
        button.setFixedSize(int(80*self.faktor), int(20*self.faktor))  
        button.setStyleSheet(self.ssbtn1)  
        button.clicked.connect(lambda: self.activate_layout("X-Mint-Oldschool"))

        title_button_layout= QHBoxLayout()

        title_button_layout.addWidget(Title)
        title_button_layout.addStretch()
        title_button_layout.addWidget(button)

        layout = QVBoxLayout()
        layout.addWidget(layout1)
        layout.addLayout(title_button_layout)
        layout.addWidget(Description)

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet(self.sscat)

        return widget

    def onCategoryClicked(self, category):
        contentCreator = self.contents.get(category)
        if contentCreator:
            contentWidget = contentCreator()
            if self.contentWidget:
                self.contentWidget.setParent(None)
                self.contentWidget.deleteLater()
            contentLayout = self.layout().itemAt(1).layout()
            contentLayout.addWidget(contentWidget, alignment=Qt.AlignTop)  # Inhalts-Widget oben ausrichten
            self.contentWidget = contentWidget

    def start_warten(self):
        subprocess.Popen("python3 ./bitte_warten.py", shell=True)

    def kill_warten(self):
        subprocess.Popen("pkill -f bitte_warten.py", shell=True)
    
    def activate_layout(self, layout):
        self.start_warten()
        os.system("xfce4-panel-profiles load /usr/share/x-live/layouts/"+layout+".tar.bz2")
        self.kill_warten()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
