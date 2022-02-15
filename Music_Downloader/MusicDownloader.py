from Modules import music_spotify
from Modules import youtube
import inspect
import sqlite3

def main():
    searchSpotify = music_spotify
    searchYoutube = youtube

    # search.sKeys().spotifyKeys(setKey="cId", myCIdKey="a5b93cf77ee84d688fafb74cc5be802f")
    # search.sKeys().spotifyKeys(setKey="cSec", myCSKey="138d5c9161604f6bab28a7a421d0b780")
    # print(search.showSpotifyKeys('cId'))

    # keyboard = ""
    # for i in range(5):
    #     keyboard = input("Type in an Artist name: ")
    #
    #     if keyboard == "break":
    #         break
    #
    #     search.doTheMusic(keyboard)




    # artist_name = "Amon Amarth"

    # searchSpotify.doTheMusic(name)

    # searchSpotify.findAlbumCoverArt('5LlHYLimFw8u8SPzbNAUhG')
    #
    #
    # conn = sqlite3.connect('database/music.db')
    # cur = conn.cursor()
    #
    # cur.execute("SELECT album_spotify_id FROM album")
    # result = cur.fetchall()
    #
    # for re in result:
    #     cur.execute("SELECT album_name FROM album WHERE album_spotify_id='%s'" % str(re[0]))
    #     result_name = cur.fetchone()
    #
    #     print("%s\n%s" % (str(result_name[0]), str(searchSpotify.findAlbumCoverArt(re[0]))))
    #
    #     cur.execute("UPDATE album SET album_coverart = '%s' WHERE album_spotify_id = '%s'" % (str(searchSpotify.findAlbumCoverArt(re[0])), str(re[0])))
    #     conn.commit()
    # conn.close()


    #
    # alb = "0zE3gloYXf05t9Juv5Rpsy"
    #
    # songList = []
    # songList.append(alb)
    #
    # searchYoutube.downloadSongs(songList)
    #
    # conn.close()

    # searchSpotify.insertIntoDatabase('album_downloaded')

    # searchYoutube.getAlbumInfo(alb)

    # getYoutubeIds(artist_name)

    # print(searchYoutube.youtubeSongQuery(("%s the %s" % (artist_name, "Arrival Of The Fimble Winter"))))

def youtubetest():

    searchSpotify = music_spotify
    searchYoutube = youtube

    print (searchYoutube.youtubeSongQuery("Amon Amarth Once Sent From The Golden Hall song"))


def getYoutubeIds(artist_name):
    searchSpotify = music_spotify
    searchYoutube = youtube

    conn = sqlite3.connect('database/music.db')
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
            youtube_id = searchYoutube.youtubeSongQuery(("%s %s song"  % (artist_name, str(result_song_title[result_song_spotify_id.index(result)][0]))))
            # if (youtube_id == None):
            #     print("This equals None Yo Retrying")
            #     youtube_id = searchYoutube.youtubeSongQuery(("%s the %s song" % (artist_name, str(result_song_title[result_song_spotify_id.index(result)][0]))))
            #     searchSpotify.insertYoutubeSongId(str(result[0]), youtube_id)
            # else:
            searchSpotify.insertYoutubeSongId(str(result[0]), youtube_id)

    conn.close()