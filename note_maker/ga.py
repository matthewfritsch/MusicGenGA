from midiutil import MIDIFile
import random
from _util import *

# metadata that holds basic info about the song
metadata = {
    'NOTES_PER_SONG': 60,
    'DEFAULT_TEMPO': 60,
    'USER_KEY_MAJOR': True,
    'TEMPOS': [30, 60, 120],
    'MUTATE_CHANCE': 0.9,
    'ROOT': random_root()
}

class Song_Generator:

    myMIDI = None

    # on creation of Song_Generator, set the user key from their input
    def __init__(self, user_key_major):
        metadata['USER_KEY_MAJOR'] = user_key_major

    # local function for adding notes
    def _add_notes(self, midi, track, channel, notes_t, time, duration, volume):
        for note in notes_t:
            midi.addNote(track, channel, note, time, duration, volume)

    # self._add_song_to_MIDI does the legwork of adding a list of notes/chords to the MIDIFile object.
    def _add_song_to_MIDI(self, MyMIDI, song, track, channel, time, duration, volume, steps):
        if MyMIDI == None:
            return MyMIDI
        i = 0
        for val in song:    #so we don't forget to add the very first val in song
            self._add_notes(MyMIDI, track, channel, val, time + i, duration/steps, volume)
            i += 1/steps
        return MyMIDI

    # write_song_to_file, provided a MIDIFile and file name, will write a MIDIFile to a file
    def write_song_to_file(self, filename):
        MyMIDI = self.myMIDI
        if '.mid' not in filename:
            filename += '.mid'
        with open(filename, 'wb') as output_file:
            MyMIDI.writeFile(output_file) 
    
    # combine_songs takes in two song lists (and optionally a point in which to split them)
    # it returns both songs with one half of song 'a' transplanted into song 'b'
    def _combine_chunks(self, song1, song2, split_pt=-1):
        split_gamut = 5
        # if we were not provided a split point, we will find our own based on the middle 1/5 of the song
        if split_pt == -1:
            split_variance = int(len(s1)/split_gamut)
            split_pt = split_variance * int(split_gamut/2)
            split_pt += random.randint(1,split_variance+1)

        song1_split = song1[:split_pt] + song2[split_pt:]
        song2_split = song2[:split_pt] + song1[split_pt:]
        return song1_split, song2_split

    # generate_MIDI must be provided a __list__ of songs. 
    # It will add each song to an additional track of a MIDIFile object, and return that MIDIFile.
    def generate_MIDI(self, note_tracks, steps=[1], channel=0, duration=1, times=[0], tempos=[metadata['DEFAULT_TEMPO']], volume=100):
        tracks = len(note_tracks)
        MyMIDI = MIDIFile(tracks)
        if len(times) == 1:
            times = [times[0] for item in note_tracks]
        if len(tempos) == 1:
            tempos = [tempos[0] for item in note_tracks]
        if len(steps) == 1:
            steps = [steps[0] for item in note_tracks]

        for i in range(0,len(note_tracks)):
            # print(i)
            track = i
            MyMIDI.addTempo(track, times[i], tempos[i])
            step = steps[i]
            if step == 'appreg':
                t = times[i]
                for cdx in range(len(note_tracks[i])):
                    chord = note_tracks[i][cdx]
                    self._add_song_to_MIDI(MyMIDI, chord, track, channel, t + cdx, duration, volume, len(chord))
            else:
                self._add_song_to_MIDI(MyMIDI, note_tracks[i], track, channel, times[i], duration, volume, steps[i])

        self.myMIDI = MyMIDI

    def generate_MIDI_with_bass(self, song, bass, channel=0, tracks=2, duration=1, times=[0], tempos=[60], volume=100):
        MyMIDI = MIDIFile(tracks)
        MyMIDI.addTempo(0, 0, 60)
        self._add_song_to_MIDI(MyMIDI, song, 0, 0, 0, duration, volume, 4)
        MyMIDI.addTempo(1, 0, 60)
        for i in range(tempos[0]):
            self._add_song_to_MIDI(MyMIDI, bass, 1, 0, i*4, duration, volume, 1)
        self.myMIDI = MyMIDI


class Chunk_Generator:

    def _get_random_prog(self, major=True):
        if major:
            return random_major_prog(note_in_octs_l(get_random_letter(), 2, 3))
        return random_minor_prog(note_in_octs_l(get_random_letter(), 2, 3))

    def _get_random_chord(self, bass, major=True, reverse_chance=0.9):
        to_ret = [[random_major_chord(note_in_octs_n(n[0], 4, 5))] for n in bass]
        if not major: 
            to_ret = [[random_minor_chord(note_in_octs_n(n[0], 4, 5))] for n in bass]
                # check if we want to reverse the appregio
        if random.random() < reverse_chance:
            to_ret.reverse()
        return to_ret

    def _make_verse(self, verbose=False, notes_for_melody=60):
        # Check key here(major or minor)
        song = self._make_song_singles(notes_for_melody, metadata['USER_KEY_MAJOR'], verbose=verbose)
        bass = self._get_random_prog(major=metadata['USER_KEY_MAJOR'])
        appreg = self._get_random_chord(bass, major=metadata['USER_KEY_MAJOR'])

        if verbose:
            print(song)
            print(bass)
            print('appreg:', appreg)
            
        # bass *= int(metadata['DEFAULT_TEMPO']/4)
        # appreg *= int(metadata['DEFAULT_TEMPO']/4)
        
        return song,bass,appreg 
        
    def _make_bridge(self, verbose=False):
        # TODO don't just make a verse out of a bridge
        return self._make_verse(verbose=verbose)

    def make_chunk(self, type='verse',verbose=False):
        if type == 'verse':
            return self._make_verse(verbose=verbose)
        return self._make_bridge(verbose=verbose)

    def _make_song_singles(self, note_count, major, verbose=False):
        song = []
        next_note = random.randint(4, 9)
        if verbose:
            print(next_note)
            print(note_count)
            print(major)
        song.append([metadata['ROOT']])
        i = 1
        while i < note_count:
            rand_note = random_root() + song[0][0]
            if verbose:
                print(str(i) + ':',str(rand_note % 12), major_notes(metadata['ROOT'] % 12))
            # if abs(song[-1][0] - rand_note) < next_note:
            if major and rand_note % 12 in major_notes(metadata['ROOT'] % 12):
                song.append([rand_note])
            elif not major and rand_note % 12 in minor_notes(metadata['ROOT'] % 12):
                song.append([rand_note])
            else:
                i -= 1
            i += 1
        return song

    def make_bass(self, note_count):
        song = []
        notes_so_far = 0
        
        root = random_root()
        bl = bassline(root)
        for i in range(15):
            song += bl
        return song

    def mutate_chunk(self, song): # has a MUTATE_CHANCE chance of giving back a randomized new song
        if random.random() <= metadata['MUTATE_CHANCE']:
            return make_song_singles(len(song))
        return song


def checkFitness(song):
    #song is a 2D array of chords
    #checking for good closer chords
    if len(song[-1])==3:
        if song[-1][0] % 12 == G and song[-1][1] % 12 == B and song[-1][2] % 12 == D:
            pass
        if song[-1][0] % 12 == F and song[-1][1] % 12 == A and song[-1][2] % 12 == C:
            pass


# all appreg should have 4 or 3 so it doesn't sound awful

'''
BASIC STRUCTURE:
Song = verse + bridge
    verse: 
        prog1
        melody1
    bridge:
        prog2
        melody2
'''

# TODO: add drums (1,1,1,3?)
# TODO: generate singular chunks and fit them together
# TODO: calculate fitness for a chunk
# TODO: calculate fitness for the connection of two chunks, or a whole song