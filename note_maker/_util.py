notes = {
    "C": 0,
    "C#": 1,
    "D": 2,
    "D#": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "G": 7,
    "G#": 8,
    "A": 9,
    "A#": 10,
    "B": 11
}

# Returns the MIDI note number for the given note name and octave
# Letter options are C, C#, D, D#, E, F, F#, G, G#, A, A#, B
# Octaves range from 0 to 10
def note(Letter, Octave):
    return notes.get(Letter) + (Octave * 12)

def note_names():
    return notes.keys()