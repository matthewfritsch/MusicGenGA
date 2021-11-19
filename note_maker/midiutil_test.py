from midiutil import MIDIFile
import random
from _util import *
degrees  = [60, 62, 64, 65, 67, 69, 71] # MIDI note number in the 5th octave
track    = 0
channel  = 0
time     = 0   # In beats (used to control when to play the next note)
duration = 1   # In beats
tempo    = 60  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,time, tempo)

add_notes(MyMIDI, track, channel, major_triad(note("C", 5)), time, duration, volume)
time += 1
add_notes(MyMIDI, track, channel, minor_triad(note("D", 5)), time, duration, volume)
time += 1
add_notes(MyMIDI, track, channel, major_triad(note("C", 5)), time, duration, volume)
time += 1
add_notes(MyMIDI, track, channel, major_seventh_suspended(note("C", 5)), time, duration, volume)

for i in range(10):
    add_notes(MyMIDI, track, channel, random_common_chord(random_root()), time + i, duration, volume)

'''
for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    #MyMIDI.addNote(track, channel, degrees[random.randint(0,len(degrees)-1)], time, duration, volume)
    time = time + 1
'''
with open("rand-test.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

'''
Fitness stuff:
    generally only use 8 out the 12 notes
    chords are made by skipping notes
    theres 3 notes that you play almost all the time (called chords), note 1, note 3, and note 5
        Notes 2,4,6 sounds really good together (8 is an octive higher than 1, higher pitch)
        3 5 7
        4 6 8
        G B D (in note form) this would be a good closer (another would be F A C)
        basically, skipping notes sounds good
    C-C is called an octive (8 notes in total)
    2 4 6 goes really nice into G B C
    sometimes we want G chord to go to A chord (less frequently)
    chords that overlap sounds good together
    major cadency sounds good 5-1 or 4-1
    6 and 3 are substitution chords for 1 (but don't start or end with them)
    try to not use the B chord (if the chord is B D F, pick a different chord) it sounds cool, but needs lots of rules around it
    chords 4 and 5 can substitute for each other
    chord 2 can sometimes be used instead of chord 4 or 5 (rarely)
    Never want to have more than 4 notes happen at one time (snare drum is included in that 4)

    We also want to limit repititon of stuff too
'''