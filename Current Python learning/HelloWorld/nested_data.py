# This is an example of lists in tuples in lists.
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# for name, artists, year, songs in albums:
#     print("Album: {}, Artist: {}, Year: {}, Songs: {}."
#           .format(name, artists, year, songs))
#
# print()
# print()
#
# album = albums[2]
# print(album)
#
# song = album[3]
# print(song)
# song1 = song[1]
# print(song1)
# song2 = song1[1]
# print(song2)
#
# mayhem = albums[3][3][2][1]
# print(mayhem)
#
# print(albums[0][3][4][1])