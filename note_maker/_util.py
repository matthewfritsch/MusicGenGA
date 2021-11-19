import random

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

def random_chord(root):
    return random.choice(chords)(root)

def major_triad(root):
    return [root, root + 4, root + 7]

def minor_triad(root):
    return [root, root + 3, root + 7]

def major_seventh(root):
    return [root, root + 4, root + 7, root + 11]

def minor_seventh(root):
    return [root, root + 3, root + 7, root + 10]

def major_sixth(root):
    return [root, root + 4, root + 7, root + 9]

def minor_sixth(root):
    return [root, root + 3, root + 7, root + 9]

def dominant_seventh(root):
    return [root, root + 4, root + 7, root + 10]

def minor_major_seventh(root):
    return [root, root + 3, root + 7, root + 11]

def diminished_seventh(root):
    return [root, root + 3, root + 6, root + 10]

def augmented_seventh(root):
    return [root, root + 4, root + 8, root + 10]

def suspended_fourth(root):
    return [root, root + 5, root + 7]

def suspended_second(root):
    return [root, root + 1, root + 7]

def suspended_fourth_seventh(root):
    return [root, root + 5, root + 7, root + 10]

def suspended_second_seventh(root):
    return [root, root + 1, root + 7, root + 10]

def dominant_seventh_flat_five(root):
    return [root, root + 4, root + 6, root + 10]

def dominant_seventh_sharp_five(root):
    return [root, root + 4, root + 8, root + 10]

def dominant_seventh_flat_nine(root):
    return [root, root + 4, root + 6, root + 10, root + 2]

def dominant_seventh_sharp_nine(root):
    return [root, root + 4, root + 8, root + 10, root + 2]

def major_triad_flat_nine(root):
    return [root, root + 4, root + 6, root + 10]

def major_triad_sharp_nine(root):
    return [root, root + 4, root + 8, root + 10]

def minor_triad_flat_nine(root):
    return [root, root + 3, root + 6, root + 10]

def minor_triad_sharp_nine(root):
    return [root, root + 3, root + 8, root + 10]

def dominant_seventh_flat_two(root):
    return [root, root + 4, root + 6, root + 9]

def dominant_seventh_sharp_two(root):
    return [root, root + 4, root + 8, root + 9]

def minor_major_seventh_flat_two(root):
    return [root, root + 3, root + 6, root + 9]

def minor_major_seventh_sharp_two(root):
    return [root, root + 3, root + 8, root + 9]

def diminished_seventh_flat_two(root):
    return [root, root + 3, root + 6, root + 9]

def diminished_seventh_sharp_two(root):
    return [root, root + 3, root + 8, root + 9]

def augmented_seventh_flat_two(root):
    return [root, root + 4, root + 6, root + 9]

def augmented_seventh_sharp_two(root):
    return [root, root + 4, root + 8, root + 9]

def suspended_fourth_flat_two(root):
    return [root, root + 5, root + 6]

def suspended_fourth_sharp_two(root):
    return [root, root + 5, root + 8]

def suspended_second_flat_two(root):
    return [root, root + 1, root + 6]

def suspended_second_sharp_two(root):
    return [root, root + 1, root + 8]

def dominant_seventh_flat_three(root):
    return [root, root + 4, root + 6, root + 9, root + 1]

def dominant_seventh_sharp_three(root):
    return [root, root + 4, root + 8, root + 9, root + 1]

def diminished_seventh_flat_three(root):
    return [root, root + 3, root + 6, root + 9, root + 1]

def diminished_seventh_sharp_three(root):
    return [root, root + 3, root + 8, root + 9, root + 1]

def augmented_seventh_flat_three(root):
    return [root, root + 4, root + 6, root + 9, root + 1]

def augmented_seventh_sharp_three(root):
    return [root, root + 4, root + 8, root + 9, root + 1]

def suspended_fourth_flat_three(root):
    return [root, root + 5, root + 6, root + 1]

def suspended_fourth_sharp_three(root):
    return [root, root + 5, root + 8, root + 1]

chords = [major_triad, minor_triad, major_seventh, minor_seventh, major_sixth, minor_sixth, dominant_seventh, minor_major_seventh, diminished_seventh, augmented_seventh, suspended_fourth, suspended_second, suspended_fourth_seventh, suspended_second_seventh, dominant_seventh_flat_five, dominant_seventh_sharp_five, dominant_seventh_flat_nine, dominant_seventh_sharp_nine, major_triad_flat_nine, major_triad_sharp_nine, minor_triad_flat_nine, minor_triad_sharp_nine, dominant_seventh_flat_two, dominant_seventh_sharp_two, minor_major_seventh_flat_two, minor_major_seventh_sharp_two, diminished_seventh_flat_two, diminished_seventh_sharp_two, augmented_seventh_flat_two, augmented_seventh_sharp_two, suspended_fourth_flat_two, suspended_fourth_sharp_two, suspended_second_flat_two, suspended_second_sharp_two, dominant_seventh_flat_three, dominant_seventh_sharp_three, diminished_seventh_flat_three, diminished_seventh_sharp_three, augmented_seventh_flat_three, augmented_seventh_sharp_three, suspended_fourth_flat_three, suspended_fourth_sharp_three]