# ex 8.7
def make_album(artist_name, album_title, num_songs=None):
    album_info = {'artist': artist_name, 'album': album_title}
    if num_songs: 
        album_info = {'artist': artist_name, 'album': album_title, 'songs': num_songs}    
    return album_info

album = make_album("Tom Misch", "Beats Tape 2", '9')
print(album)

album = make_album("Erykah Badu", "Appletree")
print(album)

album = make_album("Anita Baker", "Rapture")
print(album)
