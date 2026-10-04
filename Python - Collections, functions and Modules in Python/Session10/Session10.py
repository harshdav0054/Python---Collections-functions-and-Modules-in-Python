# #Q:-2

# # In a separate file main.py, import the add_song function from playlist.py and
# # use it to add three songs ('Kesariya', 'Shape of You', 'Believer') to an empty
# # playlist, then print the final playlist.

# from playlist import add_song

# playlist = []

# playlist = add_song("Kesariya", playlist)
# playlist = add_song("Shape of You", playlist)
# playlist = add_song("Believer", playlist)

# print("Final Playlist:", playlist)


# #Q:-3

# from playlist import add_song, remove_song

# playlist = []

# playlist = add_song("Kesariya", playlist)
# playlist = add_song("Shape of You", playlist)
# playlist = add_song("Believer", playlist)

# print("Before Removing:", playlist)

# playlist = remove_song("Shape of You", playlist)

# print("After Removing:", playlist)



#Q:-4

from playlist import add_song, remove_song, display_playlist

playlist = []

playlist = add_song("Kesariya", playlist)
playlist = add_song("Shape of You", playlist)
playlist = add_song("Believer", playlist)

playlist = remove_song("Shape of You", playlist)

display_playlist(playlist)