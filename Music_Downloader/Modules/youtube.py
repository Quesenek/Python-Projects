import mutagen.mp4 as mutagen
import urllib.request
import sqlite3
import arrow
import sys
from unidecode import unidecode
import youtube_dl
import os
import traceback
from googleapiclient.discovery import build
import time

def getYoutube(rawChannelsList):
    print("Run Youtube")

    channelNames = []
    channel_ids = [] 
    conn = sqlite3.connect('..\\database\\youtube.db')
    print("Connection granted")
    cur = conn.cursor()

    for item in rawChannelsList:
        sys.stdout.write("At index: " + str(rawChannelsList.index(item)) + ", the Channel name is: " + str(item))

        cur.execute("SELECT channel_author_id FROM channels where channel_name='%s';" % str(item))
        channel = cur.fetchone()
        channel_ids.append(cleanStrings("database", str(channel[0])))

    conn.close()
    youtubeDownloadQuery(channel_ids)

def getChannelNames():
    print("Run Channel Names")

    channels = []
    channelList = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../database/youtube.db")
    conn = sqlite3.connect(path)
    print ("Connection granted")
    cur = conn.cursor()

    cur.execute("SELECT channel_name FROM channels;")
    channels = cur.fetchall()
    conn.close()

    for channel in channels:
        channelList.append(str(channel[0]))

    return(channelList)

def RemoveChannel(channel):
    print("Run Remove Channel Name")

    conn = sqlite3.connect("..\\database\\youtube.db")
    print ("Connection granted")
    cur = conn.cursor()

    cur.execute("DELETE FROM channels WHERE channel_name='%s';" % str(channel))
    conn.commit()
    cur.execute("SELECT channel_name FROM channels WHERE channel_name='%s';" % str(channel))
    removeTest = cleanStrings('database', str(cur.fetchone()))
    print(removeTest)
    if (removeTest == "None"):
        print("Channel %s was Removed" % str(channel))

        totalChannels = []
        getDatabaseChannels = []
        cur.execute("SELECT * FROM channels;")
        getDatabaseChannels = cur.fetchall()

        for theChannels in getDatabaseChannels:
            totalChannels.append(theChannels)

        cur.execute("UPDATE sqlite_sequence SET seq = '%s' WHERE name = 'channels';" % str(len(totalChannels)))
        conn.commit()

    else:
        print("Channel %s was not Removed: removeTest = %s" % (str(channel), str(removeTest)))

    conn.close()

def AddChannel(channelURL):
    print("Run Add Channel")

    thischannel_id = ""
    thischannel_name = ""

    conn = sqlite3.connect('..\\database\\youtube.db')
    print ("Connection granted")
    cur = conn.cursor()

    url = str(channelURL)
    url = url.replace('https://www.youtube.com/watch?v=', '')
    print ("URL to be found: %s" % str(url))

    DEVELOPER_KEY = "AIzaSyCNGlSDTeAi0zt8Y1TrvV4jhJ_72v1JcrQ"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerkey=DEVELOPER_KEY)
    # Retrieve the contentDetails part of the channel resource for the
    # authenticated user's channel.

    print("Getting Video from youtube")
    theid_response = youtube.videos().list(
        id=url,
        part="snippet"
    ).execute()
    print("Got Video from youtube")
    for video in theid_response["items"]:
        # From the API response, extract the playlist ID that identifies the list
        # of videos uploaded to the authenticated user's channel.
        thischannel_id = video["snippet"]["channelId"]
        thischannel_name = video["snippet"]["channelTitle"]

        cur.execute("INSERT INTO channels ('channel_name', 'channel_author_id') VALUES ('%s', '%s')" % (str(thischannel_name), str(thischannel_id)))
        conn.commit()
        cur.execute("SELECT channel_name FROM channels WHERE channel_author_id='%s'" % str(thischannel_id))
        insertTest = cleanStrings('database', str(cur.fetchone()))
        conn.close()

        if (insertTest == thischannel_name):
            print("The Channel (%s) with id (%s) has been added to the database" % (str(thischannel_name), str(thischannel_id)))
        else:
            print("Something must have gone wrong, %s isn't in the channels list" % str(thischannel_name))

def getYoutubeSong(song):
    youtubeSongQuery(song)

def downloadYoutubeSong(song):
    print(song)

def getYoutubeApiKey(type, key=None):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../database/settings.db")
    conn = sqlite3.connect(path)
    print ("Connection granted")
    cur = conn.cursor()

    if (type == 'set' and key != None):
        cur.execute("SELECT youtube_id FROM youtube_api;")
        result = cur.fetchone()
        print(result)
        if (result == None):
            cur.execute("INSERT INTO youtube_api ('youtube_key') VALUES ('%s')" % (str(key)))
            conn.commit()
            print("Inserted the key for the first time")
        else:
            print("Already set the key")

    if (type == 'get'):
        cur.execute("SELECT youtube_key FROM youtube_api;")
        result = cur.fetchone()
        return result[0]

    if (type == 'update' and key != None):
        cur.execute("UPDATE youtube_api SET youtube_key = '%s' WHERE youtube_id = 1" % (str(key)))
        conn.commit()

    conn.close()

def setAlbumInfo(album):
    conn = sqlite3.connect('database/music.db')
    # print("Connection granted")
    cur = conn.cursor()
    conn_settings = sqlite3.connect('database/settings.db')
    # print("Connection granted")
    cur_settings = conn_settings.cursor()

    cur_settings.execute("SELECT music_directory_path FROM music_directory WHERE active='True'")
    result_directory = cur_settings.fetchone()

    cur.execute("SELECT album_artist FROM album WHERE album_spotify_id='%s'" % str(album))
    result_art_id = cur.fetchone()

    cur.execute("SELECT artist_name FROM artist WHERE artist_id='%s'" % str(result_art_id[0]))
    result_art_name = cur.fetchone()

    cur.execute("SELECT album_name FROM album WHERE album_spotify_id='%s'" % str(album))
    result_alb_name = cur.fetchone()

    cur.execute("SELECT album_id FROM album WHERE album_spotify_id='%s'" % str(album))
    result_alb_id = cur.fetchone()

    cur.execute("SELECT album_number_songs FROM album WHERE album_spotify_id='%s'" % str(album))
    result_alb_number_songs = cur.fetchone()

    print(result_alb_number_songs[0])

    cur.execute("SELECT album_coverart FROM album WHERE album_spotify_id='%s'" % str(album))
    result_alb_coverart = cur.fetchone()

    try:
        coverArtDirectory = "%s%s/cover_art" % (str(result_directory[0]), str(result_art_name[0]))
        coverArtName = "%s.jpg" % str(result_alb_name[0])
        if not os.path.exists(coverArtDirectory):
            os.makedirs(coverArtDirectory)

        if coverArtName not in coverArtDirectory:
            urllib.request.urlretrieve("%s" % str(result_alb_coverart[0]), "%s/%s" % (str(coverArtDirectory), str(coverArtName)))
            print("Cover Art Downloaded Fine!")

        directory = "%s%s/%s" % (str(result_directory[0]), str(result_art_name[0]), str(result_alb_name[0]))
        directoryResults = os.listdir(directory)
        for re in directoryResults:
            print("PreCleaned: " + re)
            cleanResult = re.replace('.m4a', '')
            print("Cleaned: " + cleanResult)

            cur.execute("SELECT song_name FROM song WHERE song_album='%s' AND song_name='%s'" % (str(result_alb_id[0]), str(cleanResult)))
            result_song_name = cur.fetchone()
            cur.execute("SELECT song_track_number FROM song WHERE song_album='%s' AND song_name='%s'" % (str(result_alb_id[0]), str(cleanResult)))
            result_song_track_number = cur.fetchone()
            cur.execute("SELECT song_spotify_id FROM song WHERE song_album='%s' AND song_name='%s'" % (str(result_alb_id[0]), str(cleanResult)))
            result_song_spotify_id = cur.fetchone()

            if (result_song_track_number != None):
                # print(str(result_song_track_number[0]))

                coverArtLocation = "%s/%s" % (str(coverArtDirectory), str(coverArtName))

                song = mutagen.MP4("%s/%s" % (str(directory), str(re)))

                song['\xa9nam'] = result_song_name[0]
                song['\xa9alb'] = result_alb_name[0]
                song['\xa9ART'] = result_art_name[0]
                song['trkn'] = [(int(result_song_track_number[0]), int(result_alb_number_songs[0]))]

                with open(coverArtLocation, "rb") as f:
                    song["covr"] = [mutagen.MP4Cover(f.read(), imageformat=mutagen.MP4Cover.FORMAT_JPEG)]

                song.save()

    except FileNotFoundError as err:
        print("Sorry File Not found: {0}".format(err))



    #
    # savedir = "/home/que/Music/MusicLibrary/Artists/%s/%s/" % (str(art_id[0]), str(alb_name[0]))
    # savename = "%s%s" % (fileName, audioType)

    conn.close()
    conn_settings.close()

def listeningSocket():
    print("listening Socket function")

    # channel_list = ['Goblins From Mars']
    #
    # getYoutube(channel_list)

    AddChannel("https://www.youtube.com/watch?v=SlA9HLlFRkw")
    RemoveChannel("Audio Library – No Copyright Music")

def youtubeSongQuery(songName):
    print ("youtube Query function")

    DEVELOPER_KEY = "%s" % getYoutubeApiKey('get')
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    # Retrieve the contentDetails part of the channel resource for the
    # authenticated user's channel.

    print(songName)

    song_response = youtube.search().list(
        part='snippet',
        maxResults=1,
        q='%s' % str(songName),
        type='video'
    ).execute()
    for song in song_response["items"]:
        return (str(song['id']['videoId']))

def youtubeDownloadQuery(channelNamesList):
    print ("youtube Query function")

    queryVideoNameResults = []
    urlList = []
    queryChannelNameResults = []

    print ("Going into the youtube getter: Number of channels " + str(len(channelNamesList)))
    for names in channelNamesList:
        print ("Going into the youtube getter")
        DEVELOPER_KEY = "%s" % getYoutubeApiKey('get')
        YOUTUBE_API_SERVICE_NAME = "youtube"
        YOUTUBE_API_VERSION = "v3"

        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)
        # Retrieve the contentDetails part of the channel resource for the
        # authenticated user's channel.

        channels_response = youtube.channels().list(
            id=names,
            part="contentDetails"
        ).execute()
        for channel in channels_response["items"]:
            # From the API response, extract the playlist ID that identifies the list
            # of videos uploaded to the authenticated user's channel.
            uploads_list_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]

            # Retrieve the list of videos uploaded to the authenticated user's channel.
            playlistitems_list_request = youtube.playlistItems().list(
                playlistId=uploads_list_id,
                part="snippet",
                maxResults=50
            )

            while playlistitems_list_request:
                playlistitems_list_response = playlistitems_list_request.execute()

                # Print information about each video.
                for playlist_item in playlistitems_list_response["items"]:
                    title = playlist_item["snippet"]["title"]
                    video_id = playlist_item["snippet"]["resourceId"]["videoId"]
                    print ("Adding: %s (%s) to the list" % (unidecode(title), unidecode(video_id)))

                    queryVideoNameResults.append(unidecode(title))
                    urlList.append(unidecode(video_id))
                    queryChannelNameResults.append(unidecode(names))

                playlistitems_list_request = youtube.playlistItems().list_next(
                    playlistitems_list_request, playlistitems_list_response)


    cleanArray(queryVideoNameResults, queryChannelNameResults, urlList)

def downloadSongs(album):
    print("youtube Song download function")  # create directory
    albumToDL = album

    conn = sqlite3.connect('database/music.db')
    # print("Connection granted")
    cur = conn.cursor()

    conn_settings = sqlite3.connect('database/settings.db')
    # print("Connection granted")
    cur_settings = conn_settings.cursor()

    cur_settings.execute("SELECT music_directory_path FROM music_directory WHERE active='True'")
    result_directory = cur_settings.fetchone()

    cur.execute("SELECT album_id FROM album WHERE album_spotify_id='%s'" % str(album))
    alb_id = cur.fetchone()
    print("\n" + str(alb_id[0]))
    cur.execute("SELECT album_name FROM album WHERE album_spotify_id='%s'" % str(album))
    alb_name = cur.fetchone()
    print(alb_name[0])
    cur.execute("SELECT album_artist FROM album WHERE album_spotify_id='%s'" % str(album))
    alb_artist = cur.fetchone()
    cur.execute("SELECT artist_name FROM artist WHERE artist_id='%s'" % str(alb_artist[0]))
    art_id = cur.fetchone()
    print(art_id[0] + "\n")

    cur.execute("SELECT song_spotify_id FROM song WHERE song_album='%s'" % str(alb_id[0]))
    song_spotify_id = cur.fetchall()

    for id in song_spotify_id:
        cur.execute("SELECT song_name FROM song WHERE song_spotify_id='%s'" % str(id[0]))
        song_name = cur.fetchone()
        cur.execute("SELECT song_youtube_id FROM song WHERE song_spotify_id='%s'" % str(id[0]))
        song_youtube_id = cur.fetchone()
        print("%s, %s" % (str(song_name[0]), str(song_youtube_id[0])))

        fileName = str(song_name[0])
        audioType = '.m4a'
        savedir = "%s/%s/%s/" % (str(result_directory[0]), str(art_id[0]), str(alb_name[0]))
        savename = "%s%s" % (fileName, audioType)
        if not os.path.exists(savedir):
            os.makedirs(savedir)

        checkCurrentDirFiles = os.listdir(savedir)
        dirCurrentFile = savename
        if dirCurrentFile in checkCurrentDirFiles:
            print("I'm already in here!\n")
            print("I'm going to skip downloading this one again and go to the next one!\n")
            continue
        else:
            # create YouTube downloader
            options = {
                'format': '140/22/18/212/136/135/134/133/160',  # choice of quality
                'extractaudio': True,  # only keep the audio
                'audioformat': ".mp3",  # convert to mp3
                'writethumbnail': True,
                'postprocessors': [
                    # 'key': 'FFmpegExtractAudio',
                    # 'preferredcodec': 'mp3',
                    # 'preferredquality': '192',},
                    {'key': 'EmbedThumbnail', }, ],
                # 'outtmpl': '%(title)s',  # name the file the ID of the video
                'outtmpl': 'tmpSong',  # name the file the ID of the video
                'noplaylist': True, }  # only download single song, not playlist
            ydl = youtube_dl.YoutubeDL(options)

            with ydl:
                # download video
                try:
                    result = ydl.extract_info('https://www.youtube.com/watch?v=%s' % str(song_youtube_id[0]),
                                              download=True)

                    print("Test Name: " + result['title'][0])

                    os.rename('tmpSong', "%s%s" % (str(savedir), str(savename)))
                    print("Downloaded and converted %s successfully!" % savename)
                except Exception as e:
                    print("Can't download audio! %s\n" % traceback.format_exc())

        fileNames = os.listdir(savedir)
        dirContains = savename
        if dirContains not in fileNames:
            myPath = os.path.dirname(os.path.realpath(sys.argv[0]))
            print(dirContains)
            if dirContains in myPath:
                print("its in here mate")
            print("%s, %s, %s isn't in here!" % (fileName, str(song_youtube_id[0]), str(alb_name[0])))

        else:
            print("I downloaded %s, %s, %s fine don't worry about this one!\n" % (
            fileName, str(song_youtube_id[0]), str(alb_name[0])))

            cur.execute("UPDATE song SET song_downloaded = 'True' WHERE song_spotify_id = '%s'" % (str(id[0])))
            conn.commit()
    conn.close()
    conn_settings.close()

def downloadYoutube(urlList):
    print ("youtube video download function")

    conn = sqlite3.connect('..\\database\\youtube.db')
    print("Connection granted")
    cur = conn.cursor()

    conn_settings = sqlite3.connect('database/settings.db')
    # print("Connection granted")
    cur_settings = conn_settings.cursor()

    for url in urlList:
        # create directory
        urlToDL = url

        cur_settings.execute("SELECT youtube_directory_path FROM youtube_directory WHERE active='True'")
        result_directory = cur_settings.fetchone()

        cur.execute("SELECT video_name FROM youtube_videos where video_url='%s';" % str(urlToDL))
        videoName = cur.fetchall()
        videoName = cleanStrings("video", str(videoName))

        cur.execute("SELECT channel_name FROM youtube_videos where video_url='%s';" % str(urlToDL))
        channelNameID = cur.fetchall()
        channelNameID = cleanStrings("database", str(channelNameID))

        cur.execute("SELECT channel_name FROM channels where channel_id=%s;" % int(int(channelNameID)))
        channelName = cur.fetchall()
        channelName = cleanStrings("database", str(channelName))

        fileName = videoName
        audioType = '.m4a'
        savedir = "%s/%s/" % (str(result_directory[0]), str(channelName))
        savename = "%s%s" % (fileName, audioType)
        if not os.path.exists(savedir):
            os.makedirs(savedir)

        checkCurrentDirFiles = os.listdir(savedir)
        dirCurrentFile = savename
        if dirCurrentFile in checkCurrentDirFiles:
            print ("I'm already in here!\n")
            print ("I'm going to skip downloading this one again and go to the next one!\n")
            continue
        else:
            # create YouTube downloader
            options = {
                'format': '140/22/18/212/136/135/134/133/160',  # choice of quality
                'extractaudio': True,  # only keep the audio
                'audioformat': ".mp3",  # convert to mp3
                'writethumbnail': True,
                'postprocessors': [
                    # 'key': 'FFmpegExtractAudio',
                    # 'preferredcodec': 'mp3',
                    # 'preferredquality': '192',},
                    {'key': 'EmbedThumbnail', }, ],
                'outtmpl': 'tmpSong',  # name the file the ID of the video
                'noplaylist': True, }  # only download single song, not playlist
            ydl = youtube_dl.YoutubeDL(options)

            with ydl:
                # download video
                try:
                    result = ydl.extract_info('https://www.youtube.com/watch?v=%s' % urlToDL, download=True)
                    os.rename('tmpSong', "%s%s" % (str(savedir), str(savename)))
                    print ("Downloaded and converted %s successfully!" % savename)
                except Exception as e:
                    print ("Can't download audio! %s\n" % traceback.format_exc())

        fileNames = os.listdir(savedir)
        dirContains = savename
        if dirContains not in fileNames:
            myPath = os.path.dirname(os.path.realpath(sys.argv[0]))
            print(dirContains)
            if dirContains in myPath:
                print("its in here mate")
            print ("%s, %s, %s isn't in here!" % (fileName, urlToDL, channelName))
            # urlList.append(urlToDL)
            print ("Something Happened! I'm going to try and download it again later!")

            cur.execute("INSERT INTO videos_not_downloaded (vnd_name, vnd_url, channel_name) VALUES ('%s', '%s', %s);" %
                (fileName, urlToDL, int(int(channelNameID))))
            conn.commit()
            print ("For now I'm going to add %s, %s, %s to the database I'll try again next time!" % (fileName, urlToDL, channelName))

        else:
            print ("I downloaded %s, %s, %s fine don't worry about this one!" % (fileName, urlToDL, channelName))
    conn.close()
    conn_settings.close()

def soundcloudQuery():
    print ("soundcloud Query function")

def compareAndCommitToDB(songTitleList, channelNameList, urlList):
    print ("Compare and then Commit To Database function")

    conn = sqlite3.connect('..\\database\\youtube.db')
    print ("Connection granted")

    finalUrlDLList = []

    cur = conn.cursor()
    cur.execute("SELECT video_url FROM youtube_videos;")

    oldMusic = cur.fetchall()

    for x in range(0, len(oldMusic)):

        oldMusic[x] = cleanStrings("database", str(oldMusic[x]))

    for url in urlList:
        if str(url) not in str(oldMusic):

            cur.execute("SELECT channel_id FROM channels WHERE channel_author_id='%s';" % str(channelNameList[urlList.index(str(url))]))
            channel_name = cur.fetchone()
            print ("Channel name Length: " + str(len(channel_name)))

            resultchannel_name = cleanStrings("database", str(channel_name[0]))

            timestamp = arrow.utcnow()
            timestamp = timestamp.timestamp

            print ("Song: " + songTitleList[urlList.index(url)] + " Channel ID: " + str(resultchannel_name) + " Time Stamp: " + str(timestamp) + " URL: " + url)

            cur.execute("INSERT INTO youtube_videos (video_name, channel_name, datetime_added, video_url) VALUES ('%s', %s, %s, '%s');" %
                        (songTitleList[urlList.index(url)],  int(resultchannel_name), timestamp, str(url)))
            conn.commit()
            finalUrlDLList.append(urlList[urlList.index(url)])


        else:
            print ("Video is already in the Database!")

    print ("Closing Connection")
    conn.close()
    print ("Connection Closed")

    for urls in finalUrlDLList:
        print (urls + str(finalUrlDLList.index(urls)))
    downloadYoutube(finalUrlDLList)

def cleanArray(rawSongList, channelNameList, urlList):
    print ("split array function")

    songTitleList = []

    for song in rawSongList:
        songTitleList.append(cleanStrings("song", unidecode(song)))

    compareAndCommitToDB(songTitleList, channelNameList, urlList)

def cleanStrings(typeOfCleaning, item):

    if (typeOfCleaning == "database"):
        removeCharacters = str(item)
        removeCharacters = removeCharacters.replace("(", "")
        removeCharacters = removeCharacters.replace("'", "")
        removeCharacters = removeCharacters.replace(",", "")
        removeCharacters = removeCharacters.replace(")", "")
        removeCharacters = removeCharacters.replace("]", "")
        removeCharacters = removeCharacters.replace("[", "")

        cleanString = removeCharacters.strip()

        return (cleanString)

    elif (typeOfCleaning == "video"):
        removeCharacters = str(item)
        removeCharacters = removeCharacters.replace("(", "")
        removeCharacters = removeCharacters.replace("'", "")
        removeCharacters = removeCharacters.replace('"', "")
        removeCharacters = removeCharacters.replace(",", "")
        removeCharacters = removeCharacters.replace(")", "")
        removeCharacters = removeCharacters.replace("[", "")
        removeCharacters = removeCharacters.replace("]", "")
        removeCharacters = removeCharacters.replace("/", "")
        removeCharacters = removeCharacters.replace("\\", "")
        removeCharacters = removeCharacters.replace(":", "")
        removeCharacters = removeCharacters.replace(";", "")
        removeCharacters = removeCharacters.replace("{", "")
        removeCharacters = removeCharacters.replace("}", "")
        removeCharacters = removeCharacters.replace("?", "")
        removeCharacters = removeCharacters.replace("*", "")

        cleanString = removeCharacters.strip()

        return (cleanString)

    elif (typeOfCleaning == "song"):
        songs = str(item)
        songs = songs.replace("'", '')
        songs = songs.replace(",", '')
        songs = songs.replace(".", '')
        songs = songs.replace("%", '')
        songs = songs.replace("$", 's')
        songs = songs.replace("_", '-')
        songs = songs.replace("*", '')
        songs = songs.replace("  ", ' ')
        songs = songs.replace("&", 'and')
        songs = songs.replace("Feat ", 'ft ')
        songs = songs.replace("feat ", 'ft ')

        cleanString = songs.strip()

        return (cleanString)

    elif (typeOfCleaning == "spaces"):
        songs = str(item)
        songs = songs.replace(" ", '')

        cleanString = songs.strip()

        return (cleanString)




# def Main():
#     listeningSocket()
#
# if __name__ == '__main__':
#     Main()
