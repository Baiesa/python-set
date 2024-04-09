'''
Task 1: Artist Lineup Compilation
You are provided with a list of artist names scheduled to perform at different stages of the music festival. Using a loop, 
compile these artist names into a set to create a unique lineup without duplicates.
'''

# artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
# unique_artists = set()

# for artis in artist_names:
#     unique_artists.add(artis)
#     print("Unique names without duplicate: ",unique_artists)

'''
Task 2: Genre Sorting
You have a list of genres associated with each artist. Using a loop with sets, 
categorize artists by their genres, creating a set for each genre.
'''

# artists_genres = {
#     "The Lumineers": "Folk",
#     "Tame Impala": "Psychedelic Rock",
#     "Billie Eilish": "Pop",
#     "Arctic Monkeys": "Indie Rock"
# }

# genre_sets = {}

# for artis,genre in artists_genres.items():
#     if genre not in genre_sets:
#         genre_sets[genre] = set()
#         genre_sets[genre].add(artis)

# for genre, artists in genre_sets.items():
#     print(f"Genre {genre}: The artis {','.join(artists)}")

'''
Task 3: Playlist Duplication Check
Create a Python script that takes multiple playlist sets and checks if any playlist is a 
duplicate of another (i.e., contains the same set of songs).
'''


def check_duplicates(playlists):
    duplicate_indices = []
    for i in range(len(playlists)):
        for j in range(i + 1, len(playlists)):
            if playlists[i] == playlists[j]:
                duplicate_indices.append((i, j))
    return duplicate_indices

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}
playlists = [playlist1, playlist2, playlist3]

duplicate_indices = check_duplicates(playlists)

if duplicate_indices:
    print("Duplicate playlists found:")
    for dup in duplicate_indices:
        print(f"Playlist {dup[0]+1} and Playlist {dup[1]+1}")
else:
    print("No duplicate playlists found.")
