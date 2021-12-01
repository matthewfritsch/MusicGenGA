import random
from midiutil import MIDIFile

class Units:
    i   = 0
    ii  = 2
    iii = 4
    iv  = 5
    v   = 7
    vi  = 9
    vii = 11
    
    notes = {
        'C': 0,
        'C#': 1,
        'D': 2,
        'D#': 3,
        'E': 4,
        'F': 5,
        'F#': 6,
        'G': 7,
        'G#': 8,
        'A': 9,
        'A#': 10,
        'B': 11,
    }


# Returns the MIDI note number for the given note name and octave
# Letter options are C, C#, D, D#, E, F, F#, G, G#, A, A#, B
# Octaves range from 0 to 10

# possible notes given the root for any major
def major_notes(root):
    return [root, root + 2, root + 4, root + 5, root + 7, root + 9, root + 11]

def minor_harmonic_notes(root):
    return [root, root + 2, root + 3, root + 5, root + 7, root + 8, root + 11]

def minor_notes(root):
    return [root, root + 2, root + 3, root + 5, root + 7, root + 8, root + 10]

def note(Letter, Octave):
    return Units.notes.get(Letter) + (Octave * 12)

def random_root():
    return random.randint(36, 79)

def note_names():
    return Units.notes.keys()

#we don't need this function tho
def random_note():
    return (random_root())

def random_common_chord(root):
    return random.choice(common_chords)(root)

def random_major_chord(root):
    return random.choice(major_chords)(root)

def random_minor_chord(root):
    return random.choice(minor_chords)(root)

def major_triad(root):
    return [root, root + 4, root + 7, root + 12]

def modified_major_triad1(root):
    return [root-3, root, root + 4, root + 7]

def modified_major_triad2(root):
    return [root-3, root, root + 4, root + 7, root+10]
    
def minor_triad(root):
    return [root, root + 3, root + 7, root + 12]

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

def diminished_seventh(root):
    return [root, root + 3, root + 6, root + 10]

def augmented_seventh(root):
    return [root, root + 4, root + 8, root + 10]

def suspended_fourth(root):
    return [root, root + 5, root + 7, root + 12]

def suspended_second(root):
    return [root, root + 1, root + 7, root + 12]

common_chords = [major_triad, minor_triad, major_seventh, minor_seventh, major_sixth, minor_sixth, dominant_seventh, diminished_seventh, augmented_seventh, suspended_fourth, suspended_second]
major_chords = [major_triad, major_sixth, major_seventh, dominant_seventh, augmented_seventh, suspended_fourth, suspended_second]
minor_chords = [minor_triad, minor_sixth, minor_seventh, diminished_seventh]

def major_seventh_suspended(root):
    return [root, root + 7, root + 11, root + 12]

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

#returns true if there is overlap, false if there isn't OR there are 2 notes in a row
#n1 and n2 represent lists of notes (can be only 1 note)
def checkingOverlap(n1, n2):
    first = n1
    second = n2
    if len(n1) == 1 and len(n2) == 1:
        return False
    if len(n2) == 1:
        first = n2
        second = n1
    for n in first:
        for i in range(0,2):
            if n >= second[i] and n <= second[i+1]:
                return True
    return False

def random_major_prog(root):
    return random.choice(major_prog)(root)

def random_minor_prog(root):
    return random.choice(minor_prog)(root)

# progression pattern
# TODO: Add more patterns
def i_vi_iii_v(root):
    return [[root], [root+Units.vi], [root+Units.iii], [root+Units.v]]

def i_vi_iv_v(root):
    return [[root], [root+Units.vi], [root+Units.iv], [root+Units.v]]

def i_v_vi_iv(root):
    return[[root], [root+Units.v], [root+Units.vi], [root+Units.iv]]

def i_v_vi_iii_iv_i_iv_v(root):
    return[[root], [root+Units.v], [root+Units.vi], [root+Units.iii], [root+Units.iv], [root], [root+Units.iv], [root+Units.v]]

def vi_iii_iv_i_vi_ii_iv_v(root):
    return[[root+Units.vi], [root+Units.iii], [root+Units.iv], [root], [root+Units.vi], [root+Units.ii], [root+Units.iv], [root+Units.v]]

def vi_ii_vi_ii_iv_i_iv_v(root):
    return [[root + Units.vi], [root + Units.ii], [root + Units.vi], [root+Units.ii], [root + Units.iv], [root], [root + Units.iv], [root + Units.v]]

minor_prog = [i_vi_iii_v, i_vi_iv_v]
major_prog = [i_v_vi_iv, i_v_vi_iii_iv_i_iv_v]

# TODO: bridge_prog
major_bridge= [vi_iii_iv_i_vi_ii_iv_v, vi_ii_vi_ii_iv_i_iv_v]

def get_random_letter():
    return random.choice(list(note_names()))

def note_in_octs_l(Letter, min_oct, max_oct):
    return Units.notes.get(Letter) + (random.randint(min_oct, max_oct) * 12)

def note_in_octs_n(num, min_oct, max_oct):
    # print(num)
    num %= 12
    return num + (random.randint(min_oct, max_oct) * 12)

def replace_item_with_list(listlist):
    for idx in range(len(listlist)):
        lst = listlist[idx]
        for jdx in range(len(lst)):
            lst[jdx] = [lst[jdx]]
    return listlist

def user_chose_major():
    key = ''
    while key not in ['major', 'minor']:
        key = input('Please select a key for your song.\nEnter \'major\' or \'minor\': ').lower()
    return key == 'major'