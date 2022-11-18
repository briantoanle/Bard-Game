"""
A BARD DAY'S NIGHT
a.k.a. BARD ROCK CAFE
a.k.a. THE SCHOOL OF BARD KNOCKS
a.k.a. A BARD RAIN'S A-GONNA FALL
"""

# Imports

from typing import Optional, TextIO  # Specific annotations

from math import ceil  # For stats

# Constants

# Minimum number of songs for a villager to be promoted to a bard
BARD_THRESHOLD = 10

# Number of songs for the billboard_top statistic
BILLBOARD_N = 10


# DO NOT use these as variables in your code;
# they are only for type contracts.

# Maps from {name: songs that this villager knows}
villagers_type = dict[str, set[str]]

bards_type = set[str]

# Maps from {song name: names of people, including bards, that know this song}
songs_type = dict[str, set[str]]

# A list of parties; each party is a set of the attendee names
parties_type = list[set[str]]


def read_input(
    f: TextIO,
) -> tuple[villagers_type, bards_type, songs_type, parties_type]:
    """
    Read the given file and return the villagers, bards, songs, and parties.

    f is an open file containing VILLAGERS and bards, SONGS, and PARTIES,
    in that order. One villager or bard per line;
    one song per line; one party per line, consisting of attendees
    separated by commas. The parties are given in the order they're held.

    """
    # TODO
    names = []
    bard = []
    f.readline()
    for line in f:
        if 'SONGS' in line:
            break
        if line == '\n':
            pass
        else:
            if '*' in line:
                bard.append(line.strip('\n'))
            else:
                names.append(line.strip('\n'))
    bards_type = set(bard)

    villa = {}
    for i in names:
        villa[i] = {}
    villagers_type = villa

    songs_type = {}
    songs = []
    for line in f:
        if 'PARTIES' in line:
            break
        if line == '\n':
            pass
        else:
            songs.append(line.strip('\n'))
    #print(songs)
    for j in songs:
        songs_type[j] = {}
    #print(songs_type)

    # parties_type = list[set[str]]
    parties_type = []
    counter=0
    for line in f:

        #print(line)
        partiers = line.strip('\n').split(",")
        tempSet = set(partiers)
        parties_type.append(tempSet)

    return [villagers_type,bards_type,songs_type,parties_type]

    #print(temp_party)

    pass


# Party functions
# We highly recommend adding helper functions here!

def sing_at_party(
    villagers: villagers_type, bards: bards_type, songs: songs_type, party: set[str]
) -> None:
    """
    A bard sings if present, otherwise the villagers sing.
    """
    # TODO
    pass

def update_bards_after_party(
    villagers: villagers_type, bards: bards_type, songs: songs_type, party: set[str]
) -> None:
    """
    Promote attendees who have learned enough songs to bards,
    iff there is another bard present at the party.
    """
    # TODO
    pass


# Stats functions

def unheard_songs(
    villagers: villagers_type,
    bards: bards_type,
    songs: songs_type,
    parties: parties_type,
) -> set[str]:
    """
    Return a set of songs that have never been heard by non-bards.
    (This means that only the bards know it.)
    """
    # TODO
    pass

def billboard_top(
    villagers: villagers_type,
    bards: bards_type,
    songs: songs_type,
    parties: parties_type,
) -> list[str]:
    """
    Return a list of the BILLBOARD_N most popular songs by number of people
    who know them, in descending order. Break ties alphabetically.
    """
    # TODO
    pass

def all_bards(
    villagers: villagers_type,
    bards: bards_type,
    songs: songs_type,
    parties: parties_type,
) -> set[str]:
    """Return the set of the village's bards."""
    # TODO
    pass

def average_attendees(
    villagers: villagers_type,
    bards: bards_type,
    songs: songs_type,
    parties: parties_type,
) -> int:
    """
    Return the average number of attendees at parties in the village.
    Round up to the nearest integer.
    """
    # TODO
    pass


# Main process

def run(filename: str) -> dict[str, object]:
    """
    Run the program: read the input, host the parties,
    and return a dictionary of resulting statistics keyed by name:
    unheard_songs, billboard_top, all_bards, average_attendees

    filename is the name of an input file.
    """
    # TODO
    pass


# Run program

if __name__ == "__main__":
    #print("hello world")
    inputfile= open("handout_example.txt", "r")
    print(read_input(inputfile))


    '''
    # Sample input from the handout -- you can tweak this if you like
    stats_handout = run("handout_example.txt")
    print("Results of handout sample input")
    for key, value in stats_handout.items():
        print(f"{key}: {value}")

    print()

    # Sample bigger input -- you can tweak this if you like
    stats_bigger = run("bigger_example.txt")
    print("Results of bigger sample input")
    for key, value in stats_bigger.items():
        print(f"{key}: {value}")
    '''