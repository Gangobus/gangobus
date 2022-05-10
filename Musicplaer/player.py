# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import res_rc
import sys, os, time
import threading
from functools import partial
import pygame
from pygame import mixer, USEREVENT

import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

pygame.init()
mixer.init()

class QCustomQWidget(QWidget):
    def __init__(self, parent=None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel = QLabel()
        self.textDownQLabel = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)

        self.allQVBoxLayout1 = QHBoxLayout()
        self.pushButton = QPushButton()
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")
        self.iconNotAdded = QIcon()
        self.iconNotAdded.addFile(u":/icons/heart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconAdded = QIcon()
        self.iconAdded.addFile(u":/icons/heart (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(self.iconNotAdded)
        self.pushButton.setIconSize(QSize(20, 20))

        self.added = False
        self.showed = True
        self.pushButton2 = QPushButton()
        self.pushButton2.setObjectName(u"pushButton")
        self.pushButton2.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton2.setIcon(icon)
        self.pushButton2.setIconSize(QSize(15, 15))
        self.allQVBoxLayout1.addWidget(self.pushButton2, 0)

        self.allQVBoxLayout1.addWidget(self.pushButton, 0)

        self.allQHBoxLayout = QHBoxLayout()
        self.iconQLabel = QLabel()
        #self.allQHBoxLayout.addWidget(self.iconQLabel, 0)

        self.allQHBoxLayout.addLayout(self.allQVBoxLayout1, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        self.songPath = ""

        self.pushButton.clicked.connect(self.addToFavourite)
        self.id = 0
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: #B9007F;
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: #B9007F;
        ''')
        self.setStyleSheet('''
            border: none;
        ''')
        self.pushButton.setStyleSheet('''
        QPushButton:disabled {
color:#ff0000;
}''')
        self.songsList = []
        self.favouriteSongsList = []
    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def getAddButton(self):
        return self.pushButton

    def getRemoveButton(self):
        return self.pushButton2

    def setSongPath(self, text):
        self.songsList.append(text)

    def getSongPath(self):
        return self.songsList

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

    def setAdded(self, isAdded):
        self.added = isAdded
        if isAdded == True:
            self.pushButton.setIcon(self.iconAdded)
        else:
            self.pushButton.setIcon(self.iconNotAdded)



    def addToFavourite(self):
        if self.added == False:
            self.pushButton.setIcon(self.iconAdded)
            self.added = True
        else:
            self.pushButton.setIcon(self.iconNotAdded)
            self.added = False

    def deleteFavouriteSong(self):
        pass

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(351, 542)
        Form.setStyleSheet(u"QPushButton{\n"
                           "	border: none;\n"
                           "    background-color: #3cbaa2;\n"
                           "	border-radius: 10;\n"
                           "}\n"
                           "\n"
                           "QPushButton:hover{\n"
                           "	border: none;\n"
                           "    background-color: rgb(41, 41, 61);\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed{\n"
                           "	border: none;\n"
                           "	background-color: rgb(40, 40, 60);\n"
                           "}\n"
                           "\n"
                           "QWidget{\n"
                           "	background-color: rgb(45,45,70)\n"
                           "}\n"
                           "\n"
                           "QLabel{\n"
                           "	color: #B9007F;\n"
                           "	font: 10pt \"Bauhaus 93\";\n"
                           "}"
                           "QListWidget"
                           "{"
                           "Outline: 0px"
                           "}"
                           "QListWidget::item:selected"
                           "{"
                           "border-bottom: 1px solid #B9007F;"
                           "}"

                           )
        self.pushButton = QPushButton(Form)
        self.pushButton.setDisabled(True)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 140, 51, 41))
        self.pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/play (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 10, 41, 41))
        icon1 = QIcon()
        icon1.addFile(u":/icons/add-to-playlist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 140, 61, 41))
        icon2 = QIcon()
        icon2.addFile(u":/icons/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(20, 20))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(220, 140, 61, 41))
        self.pushButton_4.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(20, 20))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(300, 140, 41, 41))
        self.iconVolume = QIcon()
        self.iconVolume.addFile(u":/icons/volume.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(self.iconVolume)
        self.pushButton_5.setIconSize(QSize(20, 20))
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 140, 41, 41))
        icon5 = QIcon()
        icon5.addFile(u":/icons/repeat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(20, 20))
        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(20, 200, 311, 22))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
                                            "    border: none;\n"
                                            "    height: 10px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                            "    background:  rgb(40, 40, 60);\n"
                                            "    margin: 0;\n"
                                            "	border-radius: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::handle:horizontal {\n"
                                            "    background-color: #B9007F;\n"
                                            "    border: none;\n"
                                            "	height:: 10px;\n"
                                            "    width: 10px;\n"
                                            "    margin: 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
                                            "    border-radius: 5px;\n"
                                            "}")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.verticalSlider = QSlider(Form)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(300, 20, 41, 101))
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical {\n"
                                          "    border: none;\n"
                                          "    width: 10px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                          " background:  rgb(40, 40, 60);\n"
                                          "    margin: 0;\n"
                                          "	border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QSlider::handle:vertical {\n"
                                          "    background-color: #B9007F;\n"
                                          "    border: none;\n"
                                          "	height: 10px;\n"
                                          "    width: 10px;\n"
                                          "    margin: 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
                                          "    border-radius: 5px;\n"
                                          "}")
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalScrollBar = QScrollBar()
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(330, 260, 20, 221))
        self.verticalScrollBar.setStyleSheet(u"QScrollBar::vertical{\n"
                                             "    background-color:  rgb(40, 40, 60);;\n"
                                             "	border: none;\n"
                                             "	border-top-left-radius: 6px;\n"
                                             "	border-top-right-radius: 6px;\n"
                                             "	border-bottom-left-radius: 6px;\n"
                                             "	border-bottom-right-radius: 6px;\n"
                                             "	width: 14px;\n"
                                             "	margin: 0px 4px 0 4px;\n"
                                             "}\n"
                                             "QScrollBar::handle::vertical{\n"
                                             "    background-color: #B9007F;\n"
                                             "	border-radius: 6px;\n"
                                             "	\n"
                                             "}\n"
                                             "\n"
                                             " QScrollBar::sub-line::vertical{\n"
                                             "	background: none;\n"
                                             "	margin: 0px 4px 0 4px;\n"
                                             "	border-top-left-radius: 6px;\n"
                                             "	border-top-right-radius: 6px;\n"
                                             "    height: 10px;\n"
                                             "	subcontrol-position: top;\n"
                                             "	subcontrol-origin: margin;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar::sub-line::vertical:hover{    \n"
                                             "	background-color: #B9007F;\n"
                                             "}\n"
                                             " QScrollBar::add-line::vertical:hover{\n"
                                             "    background-color: #B9007F;\n"
                                             "}\n"
                                             "\n"
                                             " QScrollBar::add-line::vertical{\n"
                                             "	margin: 0px 4px 0 4px;\n"
                                             "	background: none;\n"
                                             "	border-bottom-left-radius: 6px;\n"
                                             "	border-bottom-right-radius: 6px;\n"
                                             "	height: 10px;\n"
                                             "	subcontrol-position"
                                             ": bottom;\n"
                                             "	subcontrol-origin: margin;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar:up-arrow::vertical, QScrollBar::down-arrow::vertical{\n"
                                             "	background: none;\n"
                                             "}\n"
                                             "\n"
                                             "QScrollBar::add-page::vertical, QScrollBar::sub-page::vertical{\n"
                                             "	background: none;\n"
                                             "}")
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 61, 61))
        self.label.setStyleSheet(u"border-radius: 30px;")
        self.label.setPixmap(QPixmap(u":/icons/album.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 60, 191, 21))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 100, 191, 21))
        self.listWidget = QListWidget(Form)
        self.listWidget.itemClicked.connect(self.currentRowChange)
        self.listWidget.currentRowChanged.connect(self.selectionChanged)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setVerticalScrollBar(self.verticalScrollBar)
        self.listWidget.setStyleSheet("""
        border-top: 1px solid  #B9007F;
        border-bottom: 1px solid #B9007F;
         
          """)
        self.listWidget.setGeometry(QRect(20, 240, 311, 271))
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(70, 10, 41, 41))
        self.iconArtist = QIcon()
        self.iconArtist.addFile(u":/icons/artist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(self.iconArtist)
        self.pushButton_7.setIconSize(QSize(20, 20))

        self.retranslateUi(Form)


        self.songsListWidget =QCustomQWidget()
        self.favoriteSongsListWidget = QCustomQWidget()

        self.verticalSlider.valueChanged.connect(self.volumeChanged)
        self.verticalSlider.setValue(99)
        self.horizontalSlider.sliderPressed.connect(self.takedChangeTrue)
        self.horizontalSlider.sliderReleased.connect(self.takedChangeFalse)
        self.horizontalSlider.sliderMoved.connect(self.posChanged)

        self.iconMute = QIcon()
        self.iconMute.addFile(u":/icons/mute.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconPlay = QIcon()
        self.iconPlay.addFile(u":/icons/play (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconPause = QIcon()
        self.iconPause.addFile(u":/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconRepeat = QIcon()
        self.iconRepeat.addFile(u":/icons/repeat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconPlaylist = QIcon()
        self.iconPlaylist.addFile(u":/icons/playlist.png", QSize(), QIcon.Normal, QIcon.Off)



        self.pushButton_4.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.clicked.connect(self.selectNextSong)
        self.pushButton_3.clicked.connect(self.selectPrevSong)
        self.pushButton.clicked.connect(self.playClicked)
        self.pushButton_2.clicked.connect(partial(self.loadSongsList))
        self.pushButton_5.clicked.connect(self.mute)
        self.pushButton_6.clicked.connect(self.loopClicked)
        self.pushButton_7.clicked.connect(self.clickFav)


        # self.myQListWidget = QListWidget()

        # self.setCentralWidget(self.myQListWidget)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Track Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"0.0 | 0.0", None))
        self.pushButton_7.setText("")

    # retranslateUi



class MyWin(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.favoriteSongs = {}
        self.currentSong = []
        self.song = mixer
        self.songLength = 0
        self.paused = False
        self.taked = False
        self.loaded = False
        self.looped = False
        self.paused = False
        self.muted = False
        self.favorite = False
        self.isPlaying = False

        self.favIds = []
        self.fileNames = {}
        self.oldVolume = 0
        self.volume = 99
        self.loops = 0
        self.oldpos = 0
        self.newpos = 0
        self.currentPos = 0
        self.angle = 0
        self.listWidgetFavSongs = {}
        self.MUSIC_END_EVENT = USEREVENT + 1
        self.musicThread = threading.Thread()
        self.RotateDiscThread = threading.Thread()
        self.runStringThread = threading.Thread()
        self.albumPixmap = QPixmap(u":/icons/album.png")

    def closeEvent(self, event):
        self.song.music.stop()
        self.isPlaying = False


    def selectPrevSong(self):
        if self.listWidget.currentRow() - 1 >= 0:
            self.listWidget.setCurrentRow(self.listWidget.currentRow() - 1)

    def selectNextSong(self):
        if self.listWidget.currentRow() + 1 < self.listWidget.count():
            self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)

    def currentRowChange(self):
        pass

    def selectionChanged(self):
        source = []
        self.isPlaying = False
        if self.favorite == False:
            source = self.fileNames
        else:
            source = self.favoriteSongs


        if self.listWidget.currentRow() != -1:
            self.loaded = False
            idd = self.listWidget.currentRow()
            values = source.keys()
            values_list = list(values)
            a_value = values_list[idd]
            songName = source.get(a_value)
            songName = songName[songName.rfind('/') + 1:len(songName) - 4]
            self.pushButton.setDisabled(False)
            self.pushButton_3.setDisabled(False)
            self.pushButton_4.setDisabled(False)
            self.label_2.setText(songName)
            self.currentSong =[source.get(a_value), a_value, songName, self.favorite]
            self.songLength = mixer.Sound(self.currentSong[0]).get_length()


            self.playClicked()

            #print( "selectionChanged", self.currentSong)

    def fillSongsList(self, source):
        for key in source.keys():
            songName = source.get(key)[source.get(key).rfind('/') + 1:len(source.get(key)) - 4]
            self.songsListWidget = QCustomQWidget()
            self.songsListWidget.setTextUp(songName)
            #songLength = mixer.Sound(source.get(key)).get_length()

            #self.songsListWidget.setTextDown(str(int(songLength // 60)) + "." + str(int(songLength % 60)))
            self.songsListWidget.setId(key)
            a = self.songsListWidget.getId()

            self.songsListWidget.getRemoveButton().clicked.connect(partial(self.removeSong, a, source))
            if self.favorite == False:
                self.songsListWidget.getAddButton().clicked.connect(partial(self.addToFavourite, a, source))
                if self.favoriteSongs.get(key) is not None:
                    self.songsListWidget.setAdded(True)
            else:
                self.songsListWidget.getAddButton().clicked.connect(partial(self.removeSongFromFav, a, source))
                self.songsListWidget.setAdded(True)

            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.listWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(self.songsListWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.listWidget.addItem(myQListWidgetItem)
            self.listWidget.setItemWidget(myQListWidgetItem, self.songsListWidget)
        if len(self.currentSong) != 0:
            if self.currentSong[1] in source:
                pass
                #print("fav key by index", list(source.values())[list(source.keys()).index(self.currentSong[1])])
                self.listWidget.setCurrentRow(list(source.keys()).index(self.currentSong[1]))

    def removeSongFromFav(self, idn, source):
        source.pop(idn)
        self.printSongsList()


    def printSongsList(self):
        tmp_currentSong = self.currentSong


        self.listWidget.clear()
        self.currentSong = tmp_currentSong
        print(self.currentSong)

        if self.favorite == False:
            self.fillSongsList(self.fileNames)
        else:
            self.fillSongsList(self.favoriteSongs)

    def clickFav(self):
        if self.favorite == False:
            self.pushButton_7.setIcon(self.iconPlaylist)
            self.favorite = True
        else:
            self.pushButton_7.setIcon(self.iconArtist)
            self.favorite = False
        self.printSongsList()

    def removeSong(self, idn, source):
        source.pop(idn)
        if self.favorite:
            if len(self.fileNames) > 0:
                self.fileNames.pop(idn)
        else:
            if len(self.favoriteSongs) > 0:
                self.favoriteSongs.pop(idn)
        self.printSongsList()

    def addToFavourite(self, idn, source):

        #dopisat logiky serdechka v fav liste
        if self.favoriteSongs.get(idn) is None:
            self.favoriteSongs[idn] = self.fileNames[idn]
        else:
            self.favoriteSongs.pop(idn)

        file = open("FavouriteSongs.fav", "w")
        for key in self.favoriteSongs.keys():
            file.write(self.favoriteSongs[key] + "\n")
        #print(self.favoriteSongs)

    def loadSongsList(self):
        self.pushButton_2.setStyleSheet(
            """
        QWidget { 
         background-color: rgb(45,45,70);
         border: none; color:#B9007F;
        } 
        QLineEdit { 
         background-color: rgb(42, 42, 63);
         border-radius: 5px;
        }
        QComboBox { 
         background-color: rgb(42, 42, 63);
         border-radius: 5px;
        }
        QListView { 
         background-color: rgb(42, 42, 63);
         border-radius: 5px;
        }
        QTableView { 
         background-color: rgb(42, 42, 63);
         border-radius: 5px;
        }
        QToolButton#backButton {
         background-color: rgb(42, 42, 63);
        border: 1px solid #fff;
        border-radius: 5px;
        /* since Qt 5.15 you can directly use "icon:" */
    }

        """)
        fileDialog = QFileDialog(Form)
        fileDialog.setViewMode(QFileDialog.List)
        if self.favorite == False:
             filenames = fileDialog.getOpenFileNames(self.pushButton_2, options=QFileDialog.DontUseNativeDialog, filter="Music (*.mp3)")[0]
             for i in range(len(filenames)):
                self.fileNames[i] = filenames[i]
             #print("source ", self.fileNames)
        else:
            source = open(fileDialog.getOpenFileName(self.pushButton_2, options=QFileDialog.DontUseNativeDialog, filter="Favourite (*.fav)")[0], "r")
            favSongs = source.readlines()
            for i in range(len(favSongs)):
                self.favoriteSongs[i] = favSongs[i].rstrip()
            print("source ", self.favoriteSongs)
        self.printSongsList()

    def loopClicked(self):
        if self.looped == False:
            self.looped = True
            self.loops = -1
            self.pushButton_6.setStyleSheet("""background-color: rgba(185, 0, 127, 50);""")
        else:
            self.looped = False
            self.pushButton_6.setStyleSheet("""background-color: rgb(45,45,70);""")

    def takedChangeTrue(self):
        self.oldpos = self.song.music.get_pos()
        self.taked = True

    def takedChangeFalse(self):
        self.taked = False

    def dynamicMove(self):
        pos = 0
        while self.isPlaying:
            self.song.music.set_volume(self.volume / 100)
            for event in pygame.event.get():
                if event.type == self.MUSIC_END_EVENT or pos >= self.songLength:
                    self.loaded = False
                    self.horizontalSlider.setValue(0)
                    self.pushButton.setIcon(self.iconPlay)
                    if self.looped == True:
                        #print(self.currentSong)
                        self.playSong()
                    else:
                        self.selectNextSong()
                        self.isPlaying = False
                        break
            if self.song.music.get_busy() == True:
                if self.taked == False:

                    pos = (self.song.music.get_pos() // 1000) + (self.newpos - self.oldpos // 1000)
                    #print(pos)
                    # print(self.newpos, self.oldpos, self.newpos - self.oldpos)
                    self.horizontalSlider.setValue(pos)
                    songLength = str(int(self.songLength // 60)) + "." + str(int(self.songLength % 60))
                    currentTime = str(int(pos // 60)) + "." + str(int(pos % 60))
                    self.label_3.setText(songLength + " | " + currentTime)


    def rotateDisc(self):
        running = True
        while self.isPlaying:
            for event in pygame.event.get():
                if event.type == self.MUSIC_END_EVENT:
                    if self.looped == False:
                        running = False
            if self.song.music.get_busy() == True:
                    if self.angle < 360:
                        self.angle += 0.1
                    else:
                        self.angle = 0
                    t = QTransform().rotate(self.angle)
                    self.label.setPixmap(self.albumPixmap.transformed(t))

    def runString(self):
        toLeft = True
        window = 26
        print("start runstring thread")
        while self.isPlaying:
            songname = self.currentSong[2]
            for event in pygame.event.get():
                if event.type == self.MUSIC_END_EVENT:
                    if self.looped == False:
                        self.isPlaying = False
                        return
            if self.song.music.get_busy() == True:
                for i in range(len(self.currentSong[2]) - window + 1):
                    if i + window < len(self.currentSong[2]):
                        self.label_2.setText(self.currentSong[2][i:i + window + 1])
                        time.sleep(0.25)
                    else:

                        # print(i + window, len(songname), i + window < len(songname) - window + 1, "big sleep")
                        time.sleep(1)
                        self.label_2.setText(self.currentSong[2][0:26])
                        break


    def playSong(self):
        self.horizontalSlider.setDisabled(False)
        self.song.music.load(self.currentSong[0])
        self.newpos = 0
        self.oldpos = 0
        self.horizontalSlider.setMaximum(self.songLength)
        self.pushButton.setIcon(self.iconPause)
        self.song.music.play()
        self.loaded = True
        self.isPlaying = True

    def playClicked(self):
        if self.loaded == False:
            self.playSong()
            mixer.music.set_endevent(self.MUSIC_END_EVENT)

            #self.RotateDiscThread = threading.Thread(target=self.rotateDisc, args=())
            self.musicThread = threading.Thread(target=self.dynamicMove, args=())
            self.musicThread.start()

            if len(self.currentSong[2]) > 26:
                self.label_2.setText(self.currentSong[2][0:26])
                self.runStringThread = threading.Thread(target=self.runString, args=())
                self.runStringThread.start()
            else:
                self.label_2.setText(self.currentSong[2])
            #self.RotateDiscThread.start()

            #print("loaded")
        else:
            if self.paused == False:
                self.pushButton.setIcon(self.iconPlay)
                self.song.music.pause()
                self.paused = True
                #print("paused")
            else:
                self.pushButton.setIcon(self.iconPause)
                self.song.music.unpause()
                self.paused = False
                #print("unpaused")

    def posChanged(self):
        pos = self.horizontalSlider.value()
        self.newpos = pos
        # print(pos)
        self.song.music.set_pos(pos)

    def mute(self):
        if self.muted == False:
            self.oldVolume = self.verticalSlider.value()
            self.volume = 0
            self.verticalSlider.setValue(self.volume)
            self.muted = True
        else:
            self.verticalSlider.setValue(self.oldVolume)
            self.pushButton_5.setIcon(self.iconVolume)
            self.muted = False

    def volumeChanged(self):
        self.volume = self.verticalSlider.value()
        #print(self.volume)
        # print(pos)
        if self.volume == 0:
            self.muted = True
            self.pushButton_5.setIcon(self.iconMute)
        else:
            self.muted = False
            self.pushButton_5.setIcon(self.iconVolume)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = MyWin()
    #ui = Ui_Form()
    #ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
