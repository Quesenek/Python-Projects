import os
import sys
import sqlite3
import webbrowser
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import Modules.youtube
import Modules.music_spotify
import Modules.settings
from View.DownloaderUI import Ui_MainWindow as DownloaderUI
from View.alertBox import Ui_MainWindow as alertBoxUI



class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()

        spotify = Modules.music_spotify
        youtube = Modules.youtube
        settings = Modules.settings

        # Initiate UI's
        self.ui = DownloaderUI()
        self.alertBox = alertBox()
        self.ui.setupUi(self)
        self.centerScreen()

        # Youtube Downloader Code

        # Buttons
        self.ui.btn_youtubeChannel_updateList.clicked.connect(lambda: self.populate_listWidget_youtubeChannel())
        self.ui.btn_youtubeChannel_removeFromList.clicked.connect(lambda: self.removeFromList())
        self.ui.btn_youtubeChannel_addRemove.clicked.connect(lambda: self.btn_youtubeChannel_addRemove())
        self.ui.btn_youtubeChannel_download.clicked.connect(lambda: self.youtubeDownload())

        # Spotify Downloader Code

        # ComboBox
        getArtistsFromDB = spotify.getArtistsFromDB()
        self.ui.comboBox_musicDl_artistInDB.addItems(getArtistsFromDB)
        self.ui.comboBox_musicDl_artistInDB.setVisible(False)
        self.ui.lbl_musicDl_artistComboBoxInfo.setVisible(False)

        # Checkbox
        self.ui.checkBox_musicDl_enableComboBox.stateChanged.connect(lambda: self.checkBox_musicDl_enableComboBox_stateChanged())

        self.ui.lbl_musicDl_downloaded.setText("")

        # Buttons
        self.ui.btn_musicDl_populateLists.clicked.connect(lambda: self.btn_musicDl_populateLists())
        self.ui.btn_musicDl_toDownload.clicked.connect(lambda: self.btn_musicDl_toDownload())
        self.ui.btn_musicDl_toFound.clicked.connect(lambda: self.btn_musicDl_toFound())
        self.ui.btn_musicDl_lookupAlbum.clicked.connect(lambda: self.btn_musicDl_lookupAlbum())
        self.ui.btn_musicDl_downloadAlbums.clicked.connect(lambda: self.btn_musicDl_downloadAlbums())

        # Album Correction Code

        self.albumCorrection()

        # Settings Code

        # Youtube API
        self.ui.btn_settings_youtubeKeyShow.clicked.connect(lambda: self.youtubeApi(button='show'))
        self.ui.btn_settings_youtubeKeyUpdate.clicked.connect(lambda: self.youtubeApi(button='update'))

        # Spotify Client Id
        self.ui.btn_settings_spotifyKeyShowClientID.clicked.connect(lambda: self.spotifyClientId(button='show'))
        self.ui.btn_settings_spotifyClientIDKeyUpdate.clicked.connect(lambda: self.spotifyClientId(button='update'))

        # Spotify Client Special
        self.ui.btn_settings_spotifyKeyShowClientSpecial.clicked.connect(lambda: self.spotifyClientSpecial(button='show'))
        self.ui.btn_settings_spotifyClientSpecialKeyUpdate.clicked.connect(lambda: self.spotifyClientSpecial(button='update'))

        # Directory Code

        # Radio Buttons
        self.musicDirectory()
        self.youtubeDirectory()

        # Music
        self.ui.btn_settings_directory_music_show.clicked.connect(lambda: self.musicDirectory(button='show'))
        self.ui.btn_settings_directory_music_update.clicked.connect(lambda: self.musicDirectory(button='update'))
        self.ui.btn_settings_directory_music_operating_system.clicked.connect(lambda: self.musicDirectory(button='set_system'))

        # Youtube
        self.ui.btn_settings_directory_youtube_show.clicked.connect(lambda: self.youtubeDirectory(button='show'))
        self.ui.btn_settings_directory_youtube_update.clicked.connect(lambda: self.youtubeDirectory(button='update'))
        self.ui.btn_settings_directory_youtube_operating_system.clicked.connect(lambda: self.youtubeDirectory(button='set_system'))

    # Main Window Functions
    def centerScreen(self):
        frame = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerOfScreen = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frame.moveCenter(centerOfScreen)
        self.move(frame.topLeft())

    # Youtube Downloader Functions
    def btn_youtubeChannel_addRemove(self):
        self.alertBox.show()

    def populate_listWidget_youtubeChannel(self):
        youtube = Modules.youtube
        channels = youtube.getChannelNames()
        self.ui.listWidget_youtubeChannel.clear()

        for channel in channels:
            self.ui.listWidget_youtubeChannel.addItem(channel)

    def removeFromList(self):
        youtube = Modules.youtube

        if self.ui.listWidget_youtubeChannel.count() > 0:
            self.ui.listWidget_youtubeChannel.takeItem(self.ui.listWidget_youtubeChannel.row(self.ui.listWidget_youtubeChannel.currentItem()))




    def youtubeDownload(self):
        youtube = Modules.youtube
        channels = []
        if self.ui.listWidget_youtubeChannel.count() > 0:
            for item in range(self.ui.listWidget_youtubeChannel.count()):
                print(self.ui.listWidget_youtubeChannel.item(item).text())
                channels.append(self.ui.listWidget_youtubeChannel.item(item).text())

            youtube.getYoutube(channels)


    #  Spotify Downloader Code

    def checkBox_musicDl_enableComboBox_stateChanged(self):
        if (self.ui.checkBox_musicDl_enableComboBox.isChecked()):
            self.ui.lbl_musicDl_artistComboBoxInfo.setVisible(True)
            self.ui.comboBox_musicDl_artistInDB.setVisible(True)

            self.ui.lineEdit_musicDl_spotifyArtistId.setVisible(False)
            self.ui.lineEdit_musicDl_spotifyArtistName.setVisible(False)
            self.ui.lineEdit_musicDl_spotifyArtistId.setText("")
            self.ui.lineEdit_musicDl_spotifyArtistName.setText("")
            self.ui.lbl_musicDl_artistNameInfo.setVisible(False)
            self.ui.lbl_musicDl_artistIdInfo.setVisible(False)

        else:
            self.ui.lbl_musicDl_artistComboBoxInfo.setVisible(False)
            self.ui.comboBox_musicDl_artistInDB.setVisible(False)

            self.ui.lineEdit_musicDl_spotifyArtistId.setVisible(True)
            self.ui.lineEdit_musicDl_spotifyArtistName.setVisible(True)
            self.ui.lineEdit_musicDl_spotifyArtistId.setText("")
            self.ui.lineEdit_musicDl_spotifyArtistName.setText("")
            self.ui.lbl_musicDl_artistNameInfo.setVisible(True)
            self.ui.lbl_musicDl_artistIdInfo.setVisible(True)

    def btn_musicDl_populateLists(self):
        spotify = Modules.music_spotify
        if (self.ui.checkBox_musicDl_enableComboBox.isChecked()):
            self.populateList()
        else:

            if (not self.ui.lineEdit_musicDl_spotifyArtistId.text()):
                if (not self.ui.lineEdit_musicDl_spotifyArtistName.text()):
                    self.ui.lbl_musicDl_downloaded.setText("Enter an Artists Name or Id!!!")
                else:
                    print("Going with artist name")
                    artistResults = spotify.findArtist(self.ui.lineEdit_musicDl_spotifyArtistName.text())
                    self.ui.lineEdit_musicDl_spotifyArtistId.setText(str(artistResults[1]))
                    self.populateList()

            else:
                print("Going with artist Id")
                artistName = spotify.findArtist(name=None, id=self.ui.lineEdit_musicDl_spotifyArtistId.text())
                self.ui.lineEdit_musicDl_spotifyArtistName.setText(str(artistName))
                self.populateList()


    def populateList(self):
        spotify = Modules.music_spotify
        if (not self.ui.checkBox_musicDl_enableComboBox.isChecked()):
            self.ui.lbl_musicDl_downloaded.setText("Downloading Info From Spotify")
            QtCore.QCoreApplication.processEvents()
            spotify.doTheMusic(str(self.ui.lineEdit_musicDl_spotifyArtistName.text()))

            self.ui.lbl_musicDl_downloaded.setText("Getting Youtube Id's")
            QtCore.QCoreApplication.processEvents()
            self.getYoutubeIds(str(self.ui.lineEdit_musicDl_spotifyArtistName.text()))

            self.ui.lbl_musicDl_downloaded.setText("Populating List")
            QtCore.QCoreApplication.processEvents()
            albumList = spotify.getAlbumsFromDB(str(self.ui.lineEdit_musicDl_spotifyArtistName.text()))

        elif (self.ui.checkBox_musicDl_enableComboBox.isChecked()):
            self.ui.lbl_musicDl_downloaded.setText("Populating List")
            QtCore.QCoreApplication.processEvents()
            albumList = spotify.getAlbumsFromDB(str(self.ui.comboBox_musicDl_artistInDB.currentText().title()))

        albumNameList = []
        for item in albumList[0]:
            albumNameList.append(item)

        albumSpotifyIdList = []
        for item in albumList[1]:
            albumSpotifyIdList.append(item)

        downloadedList = []
        for item in albumList[2]:
            downloadedList.append(item)

        self.ui.listWidget_musicDl_albumsFound.clear()

        self.ui.listWidget_musicDl_albumsFound.addItems(albumNameList)

        for item in range(int(len(downloadedList))):
            self.ui.listWidget_musicDl_albumsFound.item(item).setForeground(QtGui.QColor(252, 56, 30))
            if downloadedList[item] == "True":
                font = QtGui.QFont('Sans Serif', 12, QtGui.QFont.Bold)
                self.ui.listWidget_musicDl_albumsFound.item(item).setFont(font)
                self.ui.listWidget_musicDl_albumsFound.item(item).setForeground(QtCore.Qt.green)

        self.ui.lbl_musicDl_downloaded.setText("Choose The Albums\nTo Download")
        QtCore.QCoreApplication.processEvents()

        self.ui.listWidget_musicDl_albumsFound.setCurrentRow(0)


    def getYoutubeIds(self, artist_name):
        spotify = Modules.music_spotify
        youtube = Modules.youtube

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "database/music.db")
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        cur.execute("SELECT artist_id FROM artist WHERE artist_name='%s';" % str(artist_name))
        result_artist = cur.fetchone()
        cur.execute("SELECT album_id FROM album WHERE album_artist='%s';" % str(result_artist[0]))
        result_albums = cur.fetchall()

        for id in result_albums:
            cur.execute("SELECT song_spotify_id FROM song WHERE song_album='%s';" % str(id[0]))
            result_song_spotify_id = cur.fetchall()
            cur.execute("SELECT song_name FROM song WHERE song_album='%s';" % str(id[0]))
            result_song_title = cur.fetchall()

            for result in result_song_spotify_id:
                self.ui.lbl_musicDl_downloaded.setText("Getting Youtube Id's\nAlbum-(%s/%s) Song-(%s/%s)" % (str(result_albums.index(id)+1), str(len(result_albums)), str(result_song_spotify_id.index(result)+1), str(len(result_song_spotify_id)) ))
                QtCore.QCoreApplication.processEvents()

                cur.execute("SELECT song_youtube_id FROM song WHERE song_spotify_id='%s';" % str(result[0]))
                result_song_downloaded = cur.fetchone()
                print(result_song_downloaded[0])

                if (not result_song_downloaded[0]):
                    youtube_id = youtube.youtubeSongQuery(
                        ("%s %s song" % (artist_name, str(result_song_title[result_song_spotify_id.index(result)][0]))))
                    spotify.insertYoutubeSongId(str(result[0]), youtube_id)
                else:
                    print("Passing")

        conn.close()


    def btn_musicDl_toDownload(self):
        if (self.ui.listWidget_musicDl_albumsFound.count() > 0):
            self.ui.listWidget_musicDl_albumsDownload.insertItem(
                self.ui.listWidget_musicDl_albumsFound.row(self.ui.listWidget_musicDl_albumsFound.currentItem()),
                self.ui.listWidget_musicDl_albumsFound.currentItem().text())


    def btn_musicDl_toFound(self):
        if (self.ui.listWidget_musicDl_albumsDownload.count() > 0):
            self.ui.listWidget_musicDl_albumsDownload.takeItem(
                self.ui.listWidget_musicDl_albumsDownload.row(self.ui.listWidget_musicDl_albumsDownload.currentItem()))


    def btn_musicDl_downloadAlbums(self):
        if (self.ui.listWidget_musicDl_albumsDownload.count() > 0):
            spotify = Modules.music_spotify
            youtube = Modules.youtube

            albumList = []
            if (self.ui.checkBox_musicDl_enableComboBox.isChecked()):
                albumList = spotify.getAlbumsFromDB(str(self.ui.comboBox_musicDl_artistInDB.currentText().title()))
            else:
                albumList = spotify.getAlbumsFromDB(str(self.ui.lineEdit_musicDl_spotifyArtistName.text()))

            albumNameList = []
            for item in albumList[0]:
                albumNameList.append(item)

            albumSpotifyIdList = []
            for item in albumList[1]:
                albumSpotifyIdList.append(item)

            downloadedList = []
            for item in albumList[2]:
                downloadedList.append(item)

            albumsToDownload = self.ui.listWidget_musicDl_albumsDownload.count()
            for ra in range(int(albumsToDownload)):
                if (downloadedList[albumNameList.index(self.ui.listWidget_musicDl_albumsDownload.item(ra).text())] == "True"):
                    print("Already Downloaded Moving on to the next one")
                else:
                    album = albumSpotifyIdList[albumNameList.index(self.ui.listWidget_musicDl_albumsDownload.item(ra).text())]

                    self.ui.lbl_musicDl_downloaded.setText("Downloading (%s of %s)" % (str((ra+1)), str(albumsToDownload)))
                    QtCore.QCoreApplication.processEvents()
                    youtube.downloadSongs(album)

                    self.ui.lbl_musicDl_downloaded.setText("Getting Cover Art (%s of %s)" % (str((ra+1)), str(albumsToDownload)))
                    QtCore.QCoreApplication.processEvents()
                    print(album)
                    spotify.insertIntoDatabase('coverart', str(album))

                    print("On to Album Info")
                    self.ui.lbl_musicDl_downloaded.setText("Setting Album Info (%s of %s)" % (str((ra+1)), str(albumsToDownload)))
                    QtCore.QCoreApplication.processEvents()
                    youtube.setAlbumInfo(album)

            self.ui.lbl_musicDl_downloaded.setText("Updating Database")
            spotify.insertIntoDatabase('album_downloaded')
            self.ui.lbl_musicDl_downloaded.setText("Finished")
            self.ui.listWidget_musicDl_albumsDownload.clear()
        else:
            print("Nothing Here to Download!")


    def btn_musicDl_lookupAlbum(self):
        spotify = Modules.music_spotify
        if (self.ui.listWidget_musicDl_albumsFound.count() > 0):

            if (self.ui.checkBox_musicDl_enableComboBox.isChecked()):
                albumList = spotify.getAlbumsFromDB(str(self.ui.comboBox_musicDl_artistInDB.currentText().title()))

            elif (not self.ui.checkBox_musicDl_enableComboBox.isChecked()):
                albumList = spotify.getAlbumsFromDB(str(self.ui.lineEdit_musicDl_spotifyArtistName.text()))

            albumSpotifyIdList = []
            for item in albumList[1]:
                albumSpotifyIdList.append(item)

            url = "https://open.spotify.com/album/%s" % str(albumSpotifyIdList[self.ui.listWidget_musicDl_albumsFound.row(
            self.ui.listWidget_musicDl_albumsFound.currentItem())])
            webbrowser.open_new_tab(url)

    def albumCorrection(self):
        spotify = Modules.music_spotify

        self.ui.comboBox_albumCorrection_artist.addItems(spotify.getArtistsFromDB())
        self.comboBox_albumCorrection_artist_stateChanged()

        self.ui.comboBox_albumCorrection_artist.currentIndexChanged.connect(lambda: self.comboBox_albumCorrection_artist_stateChanged())
        self.ui.comboBox_albumCorrection_album.currentIndexChanged.connect(lambda: self.comboBox_albumCorrection_album_stateChanged())
        self.ui.comboBox_albumCorrection_song.currentIndexChanged.connect(lambda: self.comboBox_albumCorrection_song_stateChanged())
        self.ui.btn_albumCorrection_youtubeWebSearch.clicked.connect(lambda: self.btn_albumCorrection_youtubeWebSearch())
        self.ui.btn_albumCorrection_updateSong.clicked.connect(lambda: self.btn_albumCorrection_updateSong())

        self.ui.lineEdit_albumCorrection_song_name
        self.ui.lineEdit_albumCorrection_song_spotify_Id
        self.ui.lineEdit_albumCorrection_song_youtube_id

    # Button click functions

    def btn_albumCorrection_youtubeWebSearch(self):
        if (self.ui.lineEdit_albumCorrection_song_name.text() and self.ui.lineEdit_albumCorrection_song_spotify_Id.text()):
            url = "https://www.youtube.com/results?search_query=%s %s song" % (str(self.ui.comboBox_albumCorrection_artist.currentText()), str(self.ui.lineEdit_albumCorrection_song_name.text()))
            webbrowser.open_new_tab(url)

    def btn_albumCorrection_updateSong(self):
        spotify = Modules.music_spotify
        if (self.ui.lineEdit_albumCorrection_song_name.text() and self.ui.lineEdit_albumCorrection_song_spotify_Id.text() and self.ui.lineEdit_albumCorrection_song_youtube_id.text()):
            updateSong = [self.ui.lineEdit_albumCorrection_song_youtube_id.text(), self.ui.lineEdit_albumCorrection_song_spotify_Id.text()]
            spotify.insertIntoDatabase('updateYoutubeId', updateSong)

            self.ui.lbl_AlbumCorrection_completionText.setText("%s updated" % str(self.ui.lineEdit_albumCorrection_song_name.text()))

    # State Changes for comboboxes

    def comboBox_albumCorrection_artist_stateChanged(self):
        spotify = Modules.music_spotify
        self.ui.lbl_AlbumCorrection_completionText.setText("----------")
        self.ui.comboBox_albumCorrection_album.clear()
        for item in spotify.getAlbumsFromDB(self.ui.comboBox_albumCorrection_artist.currentText())[0]:
            self.ui.comboBox_albumCorrection_album.addItem(str(item))

        self.comboBox_albumCorrection_album_stateChanged()

    def comboBox_albumCorrection_album_stateChanged(self):
        spotify = Modules.music_spotify

        self.ui.comboBox_albumCorrection_song.clear()

        album = spotify.getAlbumsFromDB(self.ui.comboBox_albumCorrection_artist.currentText())

        albumSpotifyId = []
        for id in album[1]:
            albumSpotifyId.append(id)

        print(str(len(albumSpotifyId)))

        if len(albumSpotifyId) > 0:
            for item in spotify.getSongsFromDB(albumSpotifyId[self.ui.comboBox_albumCorrection_album.currentIndex()])[0]:
                self.ui.comboBox_albumCorrection_song.addItem(str(item))

        self.comboBox_albumCorrection_song_stateChanged()

    def comboBox_albumCorrection_song_stateChanged(self):
        spotify = Modules.music_spotify


        album = spotify.getAlbumsFromDB(self.ui.comboBox_albumCorrection_artist.currentText())

        albumSpotifyId = []
        for id in album[1]:
            albumSpotifyId.append(id)

        if len(albumSpotifyId) > 0:
            song = spotify.getSongsFromDB(albumSpotifyId[self.ui.comboBox_albumCorrection_album.currentIndex()])

            songName = []
            songSpotifyId = []
            songYoutubeId = []

            for name in song[0]:
                songName.append(name)
            for spotifyId in song[1]:
                songSpotifyId.append(spotifyId)
            for id in song[2]:
                songYoutubeId.append(id)

            if len(songName) > 0 and len(songSpotifyId) > 0 and len(songYoutubeId) > 0:
                self.ui.lineEdit_albumCorrection_song_name.setText(songName[self.ui.comboBox_albumCorrection_song.currentIndex()])
                self.ui.lineEdit_albumCorrection_song_spotify_Id.setText(songSpotifyId[self.ui.comboBox_albumCorrection_song.currentIndex()])
                self.ui.lineEdit_albumCorrection_song_youtube_id.setText(songYoutubeId[self.ui.comboBox_albumCorrection_song.currentIndex()])

    # Settings Functions

    def youtubeApi(self, button):
        settings = Modules.settings
        if (button == 'show'):
            self.ui.lineEdit_settings_youtube.setText(str(settings.youtubeApiKey('show')))
        elif (button == 'update'):
            self.ui.lineEdit_settings_youtube.setText(str(settings.youtubeApiKey('update', str(self.ui.lineEdit_settings_youtube.text()))))
            self.ui.lbl_settings_youtubeConfirmation.setText("Youtube Key Updated")

    def spotifyClientId(self, button):
        settings = Modules.settings
        if (button == 'show'):
            self.ui.lineEdit_settings_spotifyClientId.setText(str(settings.spotifyClientId('show')))
        elif (button == 'update'):
            self.ui.lineEdit_settings_spotifyClientId.setText(str(settings.spotifyClientId('update', str(self.ui.lineEdit_settings_spotifyClientId.text()))))
            self.ui.lbl_settings_spotifyClientIdConfirmation.setText("Spotify Client Id Updated")

    def spotifyClientSpecial(self, button):
        settings = Modules.settings
        if (button == 'show'):
            self.ui.lineEdit_settings_spotifyClientSpecialId.setText(str(settings.spotifyClientSpecial('show')))
        elif (button == 'update'):
            self.ui.lineEdit_settings_spotifyClientSpecialId.setText(str(settings.spotifyClientSpecial('update', str(self.ui.lineEdit_settings_spotifyClientSpecialId.text()))))
            self.ui.lbl_settings_spotifyClientSpecialConfirmation.setText("Spotify Client Special Updated")

    def musicDirectory(self, button=None):
        settings = Modules.settings

        music_radioButton_group = QtWidgets.QButtonGroup(self.ui.centralwidget)
        music_radioButton_group.addButton(self.ui.radioButton_settings_directory_music_windows)
        music_radioButton_group.addButton(self.ui.radioButton_settings_directory_music_linux)

        if (button == 'set_system'):
            settings.musicPath('set_system', music_radioButton_group.checkedButton().text().replace("&", ""))

        elif (button == 'show'):
            self.ui.lineEdit_settings_directory_music.setText(str(settings.musicPath('show')))

        elif (button == 'update'):
            self.ui.lineEdit_settings_directory_music.setText(str(settings.musicPath('update', str(self.ui.lineEdit_settings_directory_music.text()))))

    def youtubeDirectory(self, button=None):
        settings = Modules.settings

        youtube_radioButton_group = QtWidgets.QButtonGroup(self.ui.centralwidget)
        youtube_radioButton_group.addButton(self.ui.radioButton_settings_directory_youtube_windows)
        youtube_radioButton_group.addButton(self.ui.radioButton_settings_directory_youtube_linux)

        if (button == 'set_system'):
            settings.youtubePath('set_system', youtube_radioButton_group.checkedButton().text().replace("&", ""))

        elif (button == 'show'):
            self.ui.lineEdit_settings_directory_youtube.setText(str(settings.youtubePath('show')))

        elif (button == 'update'):
            self.ui.lineEdit_settings_directory_youtube.setText(str(settings.youtubePath('update', str(self.ui.lineEdit_settings_directory_youtube.text()))))

# AlertBox Class
class alertBox(QtWidgets.QMainWindow):
    def __init__(self):
        super(alertBox, self).__init__()

        spotify = Modules.music_spotify
        youtube = Modules.youtube
        settings = Modules.settings

        self.alertBoxUI = alertBoxUI()
        self.alertBoxUI.setupUi(self)
        self.centerScreen()

        self.alertBoxUI.lbl_alertBox_info.setVisible(False)
        self.alertBoxUI.comboBox_alertBox_delete.setVisible(False)
        self.alertBoxUI.lineEdit_alertBox_data.setVisible(False)

        self.getChannelNames()

        comboBoxList = ['Insert', 'Delete']
        self.alertBoxUI.comboBox_alertBox_typeOfAction.addItems(comboBoxList)
        self.alertBoxUI.comboBox_alertBox_typeOfAction.currentIndexChanged.connect(lambda: self.comboBox_alertBox_typeOfAction_stateChanged())
        self.comboBox_alertBox_typeOfAction_stateChanged()

        self.alertBoxUI.btn_alertBox_exit.clicked.connect(lambda: self.btn_alertBox_exit())

    # Window Functions

    def centerScreen(self):
        frame = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerOfScreen = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frame.moveCenter(centerOfScreen)
        self.move(frame.topLeft())

    def comboBox_alertBox_typeOfAction_stateChanged(self):
        typeOfAction = self.alertBoxUI.comboBox_alertBox_typeOfAction.currentText()
        if (typeOfAction == "Insert"):
            self.alertBoxUI.lineEdit_alertBox_data.clear()

            self.alertBoxUI.lbl_alertBox_info.setVisible(True)
            self.alertBoxUI.lineEdit_alertBox_data.setVisible(True)
            self.alertBoxUI.comboBox_alertBox_delete.setVisible(False)

            self.alertBoxUI.lbl_alertBox_info.setText("Enter the URL for the Youtube Channel")
            QtCore.QCoreApplication.processEvents()
            self.alertBoxUI.btn_alertBox_enter.clicked.connect(lambda: self.YoutubeChannel())
            self.alertBoxUI.lbl_alertBox_Inserted.setText("----------")
            QtCore.QCoreApplication.processEvents()

        if (typeOfAction == "Delete"):
            self.alertBoxUI.lbl_alertBox_info.setVisible(True)
            self.alertBoxUI.lineEdit_alertBox_data.setVisible(False)
            self.alertBoxUI.comboBox_alertBox_delete.setVisible(True)

            self.alertBoxUI.lbl_alertBox_info.setText("Pick a Youtube Channel to Delete")
            QtCore.QCoreApplication.processEvents()
            self.alertBoxUI.lbl_alertBox_Inserted.setText("----------")
            QtCore.QCoreApplication.processEvents()

    def btn_alertBox_exit(self):
        self.close()

    # Youtube Functions

    def getChannelNames(self):
        youtube = Modules.youtube

        channels = youtube.getChannelNames()
        self.alertBoxUI.comboBox_alertBox_delete.clear()

        for channel in channels:
            self.alertBoxUI.comboBox_alertBox_delete.addItem(channel)

    def YoutubeChannel(self):
        youtube = Modules.youtube
        action = self.alertBoxUI.comboBox_alertBox_typeOfAction.currentText()
        if (action == "Insert"):
            getTheChannel = self.alertBoxUI.lineEdit_alertBox_data.text()

            self.alertBoxUI.lbl_alertBox_Inserted.setText("Inserting Channel")
            QtCore.QCoreApplication.processEvents()

            youtube.AddChannel(getTheChannel)

            self.alertBoxUI.comboBox_alertBox_delete.clear()
            self.getChannelNames()

            self.alertBoxUI.lbl_alertBox_Inserted.setText("Channel Inserted")
            QtCore.QCoreApplication.processEvents()
        elif (action == "Delete"):
            self.alertBoxUI.lbl_alertBox_Inserted.setText("Deleting Channel")
            QtCore.QCoreApplication.processEvents()

            youtube.RemoveChannel(self.alertBoxUI.comboBox_alertBox_delete.currentText())

            self.alertBoxUI.comboBox_alertBox_delete.clear()
            self.getChannelNames()

            self.alertBoxUI.lbl_alertBox_Inserted.setText("Channel Deleted")
            QtCore.QCoreApplication.processEvents()


def main():
    app = QtWidgets.QApplication(sys.argv)
    myApp = MainScreen()
    myApp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()