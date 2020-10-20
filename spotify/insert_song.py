import psycopg2
from psycopg2.extras import execute_values
import pandas

DB_NAME = 'yavaoafa'
DB_USER = 'yavaoafa'
DB_PASS = 'F-Y4Brb8xA2ZsBafGe7jYgJnlg4MIHWp'
DB_HOST = 'salt.db.elephantsql.com'

# Connect to ElephantSQL - hosted PostgreSQL DB
conn = psycopg2.connect(DB_NAME=DB_NAME,
                        DB_USER=DB_USER,
                        DB_PASS=DB_PASS,
                        DB_HOST=DB_HOST)

cursor = conn.cursor()

cursor.execute("SELECT * from test_table;")

results = cursor.fetchall()
# print(results)

#### Connect to SQLite DB for Song Data ####

import sqlite3

sl_conn = sqlite3.connect('song.sqlite3')
sl_cursor = sl_conn.cursor()


query = '''
CREATE TABLE IF NOT EXISTS songs (
    acousticness float8,
    artists varchar,
    danceability float8,
    duration_ms float8,
    energy float8,
    explicit float8,
    id varchar,
    instrumentalness float8,
    key int,
    liveness float8,
    loudness float8,
    mode int,
    name varchar,
    popularity int,
    release_date varchar,
    speechiness float8,
    tempo float8,
    valence float8,
    year int
);
'''

cursor.execute(query)

CSV_FILEPATH = "song.csv"

for song in songs:
    insert_song = """
        INSERT INTO songs
        (acousticness, artists, danceability, duration_ms, energy,
        explicit, id, instrumentalness, key, liveness, loudness, mode,
        name, popularity, release_date, speechiness, tempo, valence,
        year)
        VALUES """ + str(song[1:]) + ";"
    cursor.execute(songs)

cursor.execute('SELECT * from songs;')
cursor.fetchall()
conn.commit() # actually update the database