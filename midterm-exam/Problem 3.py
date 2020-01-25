"""
You are creating a song playlist for your next party. You have a collection of songs that can be represented as a list of tuples. Each tuple has the following elements:

    name: the first element, representing the song name (non-empty string)
    song_length: the second, element representing the song duration (float >= 0)
    song_size: the third, element representing the size on disk (float >= 0)

You want to try to optimize your playlist to play songs for as long as possible while making sure that the songs you pick do not take up more than a given amount of space on disk (the sizes should be less than or equal to the max_disk_size).

You decide the best way to achieve your goal is to start with the first song in the given song list. If the first song doesn't fit on disk, return an empty list. If there is enough space for this song, add it to the playlist.

For subsequent songs, you choose the next song such that its size on disk is smallest and that the song hasn't already been chosen. You do this until you cannot fit any more songs on the disk.

Write a function implementing this algorithm, that returns a list of the song names in the order in which they were chosen, with the first element in the list being the song chosen first. Assume song names are unique and all the songs have different sizes on disk and different durations.

You may not mutate any of the arguments.
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    final_playlist = []
    freespace = max_size
    my_songs = songs.copy()
    if songs[0][2] <= freespace:
        final_playlist.append(songs[0][0])
        freespace -= songs[0][2]
    else:
        return []
    my_songs.remove(songs[0])
    names_sizes = dict()
    for index in range(len(my_songs)):
        names_sizes[index] = my_songs[index][2]
    list_sizes = sorted(list(names_sizes.values()))
    indexes_ordered_by_size = []
    for size in list_sizes:
        for item in names_sizes:
            if names_sizes[item] == size:
                indexes_ordered_by_size.append(item)
                names_sizes.pop(item)
                break
    for index in indexes_ordered_by_size:
        if my_songs[index][2] <= freespace:
            final_playlist.append(my_songs[index][0])
            freespace -= my_songs[index][2]
        if not freespace:
            break
    return final_playlist