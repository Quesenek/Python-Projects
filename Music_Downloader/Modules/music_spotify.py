import spotipy
import sqlite3
import os
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
from View.DownloaderUI import Ui_MainWindow as DownloaderUI
import main
from spotipy.oauth2 import SpotifyClientCredentials

class sKeys():

    def spotifyKeys(self, setKey, myCIdKey=None, myCSKey=None):

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../database/settings.db")
        conn = sqlite3.connect(path)
        # print("Connection granted")
        cur = conn.cursor()

        if (setKey == "cId"):
            cur.execute("SELECT spotify_id FROM spotify_api_client_id")
            result = cur.fetchone()
            if (result == None):
                cur.execute("INSERT INTO spotify_api_client_id ('spotify_client_id') VALUES ('%s')" % str(myCIdKey))
                conn.commit()
            else:
                cur.execute("UPDATE spotify_api_client_id SET spotify_client_id = '%s' WHERE spotify_id = 1" % str(myCIdKey))
                conn.commit()
        if (setKey == "cSec"):
            cur.execute("SELECT spotify_id FROM spotify_api_client_special")
            result = cur.fetchone()
            if (result == None):
                cur.execute("INSERT INTO spotify_api_client_special ('spotify_client_special') VALUES ('%s')" % str(myCSKey))
                conn.commit()
            else:
                cur.execute("UPDATE spotify_api_client_special SET spotify_client_special = '%s' WHERE spotify_id = 1" % str(myCSKey))
                conn.commit()

        conn.close()

def showSpotifyKeys(pick):

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../database/settings.db")
    conn = sqlite3.connect(path)
    # print("Connection granted")
    cur = conn.cursor()

    if (pick == 'cId'):
        cur.execute("SELECT spotify_client_id FROM spotify_api_client_id WHERE spotify_id = 1")
        clientId = cleanStrings('database', str(cur.fetchone()))

        return clientId
    elif (pick == 'cSec'):
        cur.execute("SELECT spotify_client_special FROM spotify_api_client_special WHERE spotify_id = 1")
        clientSecret = cleanStrings('database', str(cur.fetchone()))
        return clientSecret

    conn.close()

def spotifyInfo():
    # Authorize the account: spotipy.oauth2.SpotifyClientCredentials(client_id=None, client_secret=None, proxies=None)
    client_credentials_manager = SpotifyClientCredentials(showSpotifyKeys('cId'), showSpotifyKeys('cSec'))
    # Create the spotify instance with the authorized account
    s = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return s

def findAlbumCoverArt(album_id):

    spotify = spotifyInfo()
    alb_uri = "spotify:album:%s" % str(album_id)
    results = spotify.album(alb_uri)
    # print(results['images'][0]['url'])
    return results['images'][0]['url']



def findArtist(name=None, id=None):

    spotify = spotifyInfo()

    if (name != None):
        artistKey = spotify.search(q="artist:%s" % str(name), type='artist')

        items = artistKey['artists']['items']
        if (len(items) > 0):
            artist = items[0]
            artist_name = artist['name']
            artist_id = artist['id']

            return artist_name, artist_id

    if (id != None and name == None):

        artistKey = spotify.artist(id)
        return artistKey['name']


def findAlbums(artist_id):

    spotify = spotifyInfo()

    uri = "spotify:artist:%s" % str(artist_id)

    results = spotify.artist_albums(uri, album_type='album')

    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    results_single = spotify.artist_albums(uri, album_type='single')

    albums_single = results_single['items']
    while results_single['next']:
        results_single = spotify.next(results_single)
        albums_single.extend(results['items'])

    albs = []
    albs_id = []
    for album in albums:
        if ('US' in album['available_markets']):
            albs.append(str(album['name']))
            albs_id.append(str(album['id']))

    for album in albums_single:
        if ('US' in album['available_markets']):
            albs.append(str(album['name']))
            albs_id.append(str(album['id']))

    print(str(int(len(albs_id))), str(int(len(albs))))

    return  albs, albs_id, str(int(len(albs)))


def findSongs(albumId):

    spotify = spotifyInfo()

    results = spotify.album_tracks(albumId, limit=50, offset=0)
    songs = results['items']
    while results['next']:
        results = spotify.next(results)
        songs.extend(results['items'])

    songId = []
    songName = []
    songTrackNumber = []

    for song in songs:
        songId.append(str(song['id']))
        songName.append(str(song['name']))

    for i in range(int(len(songName))):
        songTrackNumber.append(str(i+1))

    return songId, songName, songTrackNumber, str(int(len(songName)))

def doTheMusic(artist_name):

    artistList = findArtist(artist_name)

    print("%s, %s" % (str(artistList[0]), str(artistList[1])))

    albumList = findAlbums(str(artistList[1]))

    info_album_title =[]
    info_album_id = []
    info_album_numberOfAlbs = albumList[2]

    artist_database = [str(artistList[0]), str(artistList[1]), str(info_album_numberOfAlbs)]
    insertIntoDatabase('artist', artist_database)

    for row in range(0, int(info_album_numberOfAlbs)):
        info_album_title.append(str(albumList[0][row]))
        info_album_id.append(str(albumList[1][row]))

    print(str(int(len(info_album_id))))

    for row in range(int(info_album_numberOfAlbs)):
        print("album Title: %s Album id: %s" % (str(info_album_title[row]), str(info_album_id[row])))


    for albums in info_album_id:

        songList = findSongs(str(albums))

        print("\nAlbum Number: %s, Album: %s, Songs in album: %s \n" % (str(info_album_id.index(albums) + 1), info_album_title[info_album_id.index(albums)], str(int(songList[3]))))

        album_database = [str(info_album_title[info_album_id.index(albums)]), str(albums), str(int(songList[3])), str(artistList[1]), "false"]
        insertIntoDatabase('album', album_database)

        info_song_id = []
        info_song_name = []
        info_song_trackNumber = []
        info_album_numberOfTracks = int(songList[3])

        for row in range(0, info_album_numberOfTracks):
            info_song_id.append(str(songList[0][row]))
            info_song_name.append(str(songList[1][row]))
            info_song_trackNumber.append(str(songList[2][row]))

        print("|-------------------------------------------------------------------------------------------|")
        for row in range(int(len(info_song_name))):
            print("track Number: %s Name: %s, Id: %s" % (str(info_song_trackNumber[row]), str(info_song_name[row]), str(info_song_id[row])))
            song_database = [str(info_song_name[row]), str(info_song_trackNumber[row]), str(info_song_id[row]), str(albums), "false"]
            insertIntoDatabase('song', song_database)
        print("|-------------------------------------------------------------------------------------------|")

    return "done"

def insertYoutubeSongId(songId, youtubeId):

    data = []
    data.append(songId)
    data.append(youtubeId)
    insertIntoDatabase('youtubeId', data)


def insertIntoDatabase(type, data=None):

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../database/music.db")
    conn = sqlite3.connect(path)
    # print("Connection granted")
    cur = conn.cursor()

    if (type == 'artist'):
        cur.execute("SELECT artist_name FROM artist WHERE artist_name='%s';" % str(data[0]))
        existsCheck = cur.fetchone()

        if (existsCheck == None):
            print("Inserting Values: %s, %s, %s Into DB" % (str(data[0]), str(data[1]), str(data[2])))
            cur.execute("INSERT INTO artist ('artist_name', 'artist_spotify_id', 'artist_number_albums') VALUES ('%s', '%s', '%s');"
                        % (str(data[0]), str(data[1]), str(data[2])))
            conn.commit()

    if (type == 'album'):
        cur.execute("SELECT album_spotify_id FROM album WHERE album_spotify_id='%s';" % str(data[1]))
        existsCheck = cur.fetchone()

        if (existsCheck == None):
            cur.execute("SELECT artist_id FROM artist WHERE artist_spotify_id='%s';" % str(data[3]))
            album_artist = cur.fetchone()
            album_artist = cleanStrings('database', str(album_artist))

            print("Inserting Values: %s, %s, %s, %s, %s Into DB" %
                  (str(data[0]), str(data[1]), str(data[2]), str(album_artist), str(data[4])))
            cur.execute("INSERT INTO album ('album_name', 'album_spotify_id', 'album_number_songs', 'album_artist', 'album_downloaded') VALUES ('%s', '%s', '%s', '%s', '%s');"
                        % (cleanStrings('song', str(data[0])), str(data[1]), str(data[2]), str(int(album_artist)), str(data[4])))
            conn.commit()

    if (type == 'song'):
        cur.execute("SELECT song_spotify_id FROM song WHERE song_spotify_id='%s';" % str(data[2]))
        existsCheck = cur.fetchone()

        if (existsCheck == None):
            cur.execute("SELECT album_id FROM album WHERE album_spotify_id='%s';" % str(data[3]))
            song_album = cur.fetchone()
            song_album = cleanStrings('database', str(song_album))

            print("Inserting Values: %s, %s, %s, %s, %s Into DB" %
                  (str(data[0]), str(data[1]), str(data[2]), str(song_album), str(data[4])))
            cur.execute("INSERT INTO song ('song_name', 'song_track_number', 'song_spotify_id', 'song_album', 'song_downloaded') VALUES ('%s', '%s', '%s', '%s', '%s');"
                        % (cleanStrings('song', str(data[0])), str(data[1]), str(data[2]), str(song_album), str(data[4])))
            conn.commit()

    if (type == 'youtubeId'):
        print(data[0])
        print(data[1])
        cur.execute("SELECT song_youtube_id FROM song WHERE song_spotify_id ='%s'" % str(data[0]))
        result = cur.fetchone()
        cur.execute("SELECT song_youtube_id_manual_change FROM song WHERE song_spotify_id ='%s'" % str(data[0]))
        result_manualChange = cur.fetchone()

        if (str(result_manualChange[0]) == "True"):
            print("id changed by user cannot change it")
        else:
            if (str(result[0]) == str(data[1])):
                print("Youtube Id Already assigned to that song")
            else:
                cur.execute("UPDATE song SET song_youtube_id = '%s' WHERE song_spotify_id = '%s'" % (str(data[1]), str(data[0])))
                conn.commit()

    if (type == 'album_downloaded'):

        cur.execute("SELECT album_spotify_id FROM album")
        result_getAlbums = cur.fetchall()

        for album in result_getAlbums:
            cur.execute("SELECT album_id FROM album WHERE album_spotify_id ='%s'" % str(album[0]))
            result_getAlbId = cur.fetchone()

            cur.execute("SELECT song_downloaded FROM song WHERE song_album ='%s'" % str(result_getAlbId[0]))
            result_getIfSongDownloaded = cur.fetchall()

            if any("false" in r for r in result_getIfSongDownloaded):
                print('Not All Songs in this Album have been Downloaded')
            else:
                print("True for: %s" % str(result_getAlbId[0]))
                cur.execute("UPDATE album SET album_downloaded = 'True' WHERE album_id = '%s'" % (str(result_getAlbId[0])))
                conn.commit()
    if (type == 'coverart'):

        # Album Id
        coverart = findAlbumCoverArt('%s' % str(data))

        print("Coverart: %s, Data: %s" % (str(coverart), str(data)))

        cur.execute("UPDATE album SET album_coverart = '%s' WHERE album_spotify_id = '%s'" % (str(coverart), str(data)))
        conn.commit()

    if (type == 'updateYoutubeId'):

        cur.execute("UPDATE song SET song_youtube_id = '%s' WHERE song_spotify_id = '%s'" % (str(data[0]), str(data[1])))
        conn.commit()
        cur.execute("UPDATE song SET song_youtube_id_manual_change = 'True' WHERE song_spotify_id = '%s'" % (str(data[1])))
        conn.commit()


    conn.close()

def getArtistsFromDB():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../database/music.db")
    conn = sqlite3.connect(path)
    # print("Connection granted")
    cur = conn.cursor()

    cur.execute("SELECT artist_name FROM artist")
    result_getArtists = cur.fetchall()

    getArtist = []

    for re in result_getArtists:
        print(re[0])
        getArtist.append(re[0])

    conn.close()

    return getArtist

def getAlbumsFromDB(artist):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../database/music.db")
    conn = sqlite3.connect(path)
    # print("Connection granted")
    cur = conn.cursor()

    cur.execute("SELECT artist_id FROM artist WHERE artist_name='%s'" % str(artist))
    result_artistId = cur.fetchone()

    cur.execute("SELECT album_spotify_id FROM album WHERE album_artist='%s'" % str(result_artistId[0]))
    result_getAlbumId = cur.fetchall()

    getAlbumNames = []
    getAlbumSpotifyId = []
    getDownloaded = []

    for re in result_getAlbumId:
        cur.execute("SELECT album_name FROM album WHERE album_spotify_id='%s' AND album_artist='%s'" % (str(re[0]), str(result_artistId[0])))
        result_getAlbums = cur.fetchone()
        cur.execute("SELECT album_downloaded FROM album WHERE album_spotify_id='%s' AND album_artist='%s'" % (str(re[0]), str(result_artistId[0])))
        result_getDownloaded = cur.fetchone()

        getAlbumNames.append(result_getAlbums[0])
        getAlbumSpotifyId.append(re[0])
        getDownloaded.append(result_getDownloaded[0])

    conn.close()

    return getAlbumNames, getAlbumSpotifyId,  getDownloaded

def getSongsFromDB(albumId):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../database/music.db")
    conn = sqlite3.connect(path)
    # print("Connection granted")
    cur = conn.cursor()

    cur.execute("SELECT album_id FROM album WHERE album_spotify_id='%s'" % str(albumId))
    result_albumId = cur.fetchone()

    cur.execute("SELECT song_name FROM song WHERE song_album='%s'" % str(result_albumId[0]))
    result_songName = cur.fetchall()

    cur.execute("SELECT song_spotify_id FROM song WHERE song_album='%s'" % str(result_albumId[0]))
    result_songSpotifyId = cur.fetchall()

    cur.execute("SELECT song_youtube_id FROM song WHERE song_album='%s'" % str(result_albumId[0]))
    result_songYoutubeId = cur.fetchall()

    songName = []
    songSpotifyId = []
    songYoutubeid = []

    for re in range(int(len(result_songSpotifyId))):
        songName.append(result_songName[re][0])
        songSpotifyId.append(result_songSpotifyId[re][0])
        songYoutubeid.append(result_songYoutubeId[re][0])

    return songName, songSpotifyId, songYoutubeid


# def getSongsFromDB(album):
#     conn = sqlite3.connect('database/music.db')
#     # print("Connection granted")
#     cur = conn.cursor()
#
#     cur.execute("SELECT album_id FROM album WHERE album_spotify_id='%s'" % str(album))
#     result_getAlbumSpotifyId = cur.fetchone()
#
#     cur.execute("SELECT song_spotify_id FROM song WHERE song_album='%s'" % str(result_getAlbumSpotifyId[0]))
#     result_getSongSpotifyId = cur.fetchall()
#
#     songSpotifyId = []
#     songName = []
#
#     for re in result_getSongSpotifyId:
#
#         cur.execute("SELECT song_name FROM song WHERE song_spotify_id='%s'" % str(re[0]))
#         result_getSongName = cur.fetchone()
#
#     conn.close()



def cleanStrings(typeOfCleaning, item):

    if (typeOfCleaning == "database"):
        removeCharacters = str(item)
        removeCharacters = removeCharacters.replace("'", "")
        removeCharacters = removeCharacters.replace(",", "")
        removeCharacters = removeCharacters.replace(".", "")
        removeCharacters = removeCharacters.replace("(", "")
        removeCharacters = removeCharacters.replace(")", "")
        removeCharacters = removeCharacters.replace("]", "")
        removeCharacters = removeCharacters.replace("[", "")

        cleanString = removeCharacters.strip()

        return (cleanString)

    if (typeOfCleaning == "song"):
        removeCharacters = str(item)
        removeCharacters = removeCharacters.replace("'", "")
        removeCharacters = removeCharacters.replace("/", "")
        removeCharacters = removeCharacters.replace("\\", "")

        cleanString = removeCharacters.strip()

        return (cleanString)