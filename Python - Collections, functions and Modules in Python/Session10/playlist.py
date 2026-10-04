#Q:-1

# Create a new Python file called playlist.py and define a function 
# add_song(song_name, playlist) that adds a song to the playlist list and 
# returns the updated list.

def add_song(song_name, playlist):
    playlist.append(song_name)
    return playlist


#Q:-3

# Add a function remove_song(song_name, playlist) in playlist.py that removes a song
# if it exists in the playlist and returns the updated list. Import and use this function 
# in main.py to remove 'Shape of You' from your playlist and print the result.


def remove_song(song_name, playlist):
    if song_name in playlist:
        playlist.remove(song_name)

    return playlist


#Q:-4

# Refactor your playlist.py by adding a function display_playlist(playlist) 
# that prints each song with its position number (like Spotify's queue). Import 
# and use this function in main.py after adding and removing songs.

def display_playlist(playlist):
    for position, song in enumerate(playlist, start=1):
        print(position, "-", song)