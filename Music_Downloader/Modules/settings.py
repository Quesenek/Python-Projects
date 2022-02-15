import sqlite3

# Application Settings

# Api Key functions

def youtubeApiKey(action, data=None):

    conn = sqlite3.connect('database/settings.db')
    # print("Connection granted")
    cur = conn.cursor()

    if (action == 'show'):

        cur.execute("SELECT youtube_key FROM youtube_api WHERE youtube_id=1")
        youtube_key = cur.fetchone()

        return youtube_key[0]

    elif (action == 'update' and data):

        cur.execute("UPDATE youtube_api SET youtube_key = '%s' WHERE youtube_id = 1" % (str(data)))
        conn.commit()

        cur.execute("SELECT youtube_key FROM youtube_api WHERE youtube_id=1")
        youtube_key = cur.fetchone()

        return youtube_key[0]

    conn.close()

def spotifyClientId(action, data=None):

    conn = sqlite3.connect('database/settings.db')
    # print("Connection granted")
    cur = conn.cursor()

    if (action == 'show'):

        cur.execute("SELECT spotify_client_id FROM spotify_api_client_id WHERE spotify_id=1")
        youtube_key = cur.fetchone()

        return youtube_key[0]

    elif (action == 'update' and data):

        cur.execute("UPDATE spotify_api_client_id SET spotify_client_id = '%s' WHERE spotify_id = 1" % (str(data)))
        conn.commit()

        cur.execute("SELECT spotify_client_id FROM spotify_api_client_id WHERE spotify_id=1")
        youtube_key = cur.fetchone()

        return youtube_key[0]

    conn.close()

def spotifyClientSpecial(action, data=None):

    conn = sqlite3.connect('database/settings.db')
    # print("Connection granted")
    cur = conn.cursor()

    if (action == 'show'):

        cur.execute("SELECT spotify_client_special FROM spotify_api_client_special WHERE spotify_id=1")
        youtube_key = cur.fetchone()

        return youtube_key[0]

    elif (action == 'update' and data):

        cur.execute("UPDATE spotify_api_client_special SET spotify_client_special = '%s' WHERE spotify_id = 1" % (str(data)))
        conn.commit()

        cur.execute("SELECT spotify_client_special FROM spotify_api_client_special WHERE spotify_id=1")
        youtube_key = cur.fetchone()

        return youtube_key[0]

    conn.close()

# Directory Settings Functions

def musicPath(action, data=None):

    conn = sqlite3.connect('database/settings.db')
    # print("Connection granted")
    cur = conn.cursor()

    if (action == 'show'):

        cur.execute("SELECT music_directory_path FROM music_directory WHERE active='True'")
        music_directory = cur.fetchone()

        return music_directory[0]

    elif (action == 'set_system' and data):

        cur.execute("UPDATE music_directory SET active = 'False' WHERE active = 'True'")
        conn.commit()

        cur.execute("UPDATE music_directory SET active = 'True' WHERE operating_system = '%s'" % (str(data)))
        conn.commit()

    elif (action == 'update' and data):

        cur.execute("UPDATE music_directory SET music_directory_path = '%s' WHERE active = 'True'" % (str(data)))
        conn.commit()

        cur.execute("SELECT music_directory_path FROM music_directory WHERE active='True'")
        music_directory = cur.fetchone()

        return music_directory[0]

    conn.close()

def youtubePath(action, data=None):

    conn = sqlite3.connect('database/settings.db')
    # print("Connection granted")
    cur = conn.cursor()

    if (action == 'show'):

        cur.execute("SELECT youtube_directory_path FROM youtube_directory WHERE active='True'")
        youtube_directory = cur.fetchone()

        return youtube_directory[0]

    elif (action == 'set_system' and data):

        cur.execute("UPDATE youtube_directory SET active = 'False' WHERE active = 'True'")
        conn.commit()

        cur.execute("UPDATE youtube_directory SET active = 'True' WHERE operating_system = '%s'" % (str(data)))
        conn.commit()

    elif (action == 'update' and data):

        cur.execute("UPDATE youtube_directory SET youtube_directory_path = '%s' WHERE active = 'True'" % (str(data)))
        conn.commit()

        cur.execute("SELECT youtube_directory_path FROM youtube_directory WHERE active='True'")
        youtube_directory = cur.fetchone()

        return youtube_directory[0]

    conn.close()