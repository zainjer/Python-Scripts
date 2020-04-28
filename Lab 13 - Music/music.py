# The following program is licensed to @Zainjer
# Any attempts on duplication or Unauthorized distribution of this program will result in a Lawsuit.
# Contact him at https://www.linkedin.com/in/zainjer/
# Or track him on https://github.com/zainjer


import csv

# Design Structure -------------------------------
class Track:
    title = "Dummy Title"
    duration = 90
    genre = "Dummy Genre"

    def __init__(self, title=None, duration=None, genre=None):
        self.title = title
        self.duration = duration
        self.genre = genre


class Album:
    title = "Dummy Album Title"
    tracks_dictionary = dict()

    def __init__(self, title):
        self.title = title

    def add_track(self, track):
        if track.title not in self.tracks_dictionary:
            self.tracks_dictionary[track.title] = tr


class Artist:
    name = "Dummy Name"
    album_dictionary = dict()

    def __init__(self, name):
        self.name = name

    def add_album(self, album_name,album):
       if album_name not in self.album_dictionary:
           self.album_dictionary[album_name] = album


# ----------------------Main Program----------------------------


# Counter Variables for required output
counter_Artist = 0
counter_Album = 0
counter_Track = 0

# The Dictionary for All the artists in file
artist_dictionary = dict()

# For storing file data
reader = []

# Reading contents of 'music.csv' and storing it in list 'reader' as Lines
with open("music.csv", 'r', encoding="utf-8") as csv_file:
    reader.__iadd__(csv.reader(csv_file))


# Logic loop that iterates through every line, in list 'reader'
# Determines the line's contents and adds them to their respective dictionaries
# while avoiding duplicates and updating Counter Variables
for row in reader:
    if row[2] not in artist_dictionary:
        ar = Artist(row[2])
        artist_dictionary[row[2]] = ar
        counter_Artist +=1
    else:
        ar = artist_dictionary[row[2]]

    if row[3] not in ar.album_dictionary:
        al = Album(row[3])
        ar.add_album(row[3], al)
        counter_Album += 1
    else:
        al = Artist.album_dictionary[row[3]]

    if row[0] not in al.tracks_dictionary:
        tr = Track(row[0], row[1], row[4])
        al.add_track(tr)
        counter_Track += 1

# Printing out the required output.
print("Tracks: "+str(counter_Track)+"\nAlbums: "+str(counter_Album)+"\nArtists: "+str(counter_Artist))