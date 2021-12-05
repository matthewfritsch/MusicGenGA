from midiutil import MIDIFile
import random
from _util import *

# metadata that holds basic info about the song
metadata = {
    'MELODY_NOTES_PB' : 2 ** random.randint(1,3),
    'MUTATE_CHANCE': 0.5,
    'ROOT': random_root(),
    'TEMPO_SLOW' : random.randint(40,120),
    'TEMPO_MED' : random.randint(120,160),
    'TEMPO_FAST' : random.randint(160, 240),
    'TEMPO': -1,
    'USER_KEY_MAJOR': True,
}

# current tempo options
tempos = {
    'fast': metadata['TEMPO_FAST'], 
    'medium': metadata['TEMPO_MED'], 
    'slow': metadata['TEMPO_SLOW'],
}

class Track:
    def __init__(self, notes, note_type):
        self.notes = notes
        self.note_type = note_type
        if note_type == 'bass':
            self.steps = 1
        elif note_type == 'melody':
            self.steps = 'melody'
        else:
            self.steps = 4

class BassTrack(Track):
    def __init__(self, notes):
        super().__init__(notes, 'bass')

class MelodyTrack(Track):
    def __init__(self, notes):
        super().__init__(notes, 'bass')

class AppregioTrack(Track):
    def __init__(self, notes):
        super().__init__(notes, 'bass')


#Song is an object that contains features of a MIDI song
class Song:
    def __init__(self, track_type, **track_info):
        self.track_type = track_type
        self.vars = []
        for key,value in track_info.items():
            self.vars.append(key)
            setattr(self, key, value)

    def to_list(self):
        return [getattr(self, item) for item in self.vars]

#Song_Generator is an object that generates a MIDI object and writes song features to a MIDI file.
class Song_Generator:

    # on creation of Song_Generator, set the user key from their input
    def __init__(self, user_key_major, tempo=metadata['TEMPO']):
        metadata['USER_KEY_MAJOR'] = user_key_major
        metadata['TEMPO'] = tempo
        metadata['MELODY_NOTES_PB'] = 2 * random.randint(8, 16)

    def create_MIDI(self, verse_list, bridge_list=[], filename='my_song.mid'):
        print(metadata['TEMPO'])
        final_song = self._create_song_structure(verse_list, bridge_list)
        final_MIDI = self.generate_MIDI(final_song)
        self.write_song_to_file(final_MIDI, filename)

    def _create_song_structure(self, verse_list, bridge_list):
        # e.g verse1*4, bridge
        structure = [
            verse_list[0],
            verse_list[0],
            verse_list[0],
            verse_list[0],
            # bridge_list[0]
            ]

        final_melody = []
        final_bass = []
        final_appregio = []

        for song in structure:
            final_melody += song.melody.notes
            final_bass += song.bass.notes
            final_appregio += song.appregio.notes

        final_melody_track = Track(final_melody, note_type='melody')
        final_bass_track = Track(final_bass, note_type='bass')
        final_appregio_track = Track(final_appregio, note_type='appregio')
        

        return Song(track_type='final', melody=final_melody_track, bass=final_bass_track, appregio=final_appregio_track)

    # local function for adding notes
    def _add_notes(self, midi, track, channel, notes_t, time, duration, volume):
        for note in notes_t:
            midi.addNote(track, channel, note, time, duration, volume)

    # self._add_song_to_MIDI does the legwork of adding a list of notes/chords to the MIDIFile object.
    def _add_song_to_MIDI(self, MyMIDI, song, track, channel, time, duration, volume):
        if MyMIDI == None:
            return MyMIDI
        i = 0
        for note_list in song.notes:
            steps = song.steps
            if song.steps == 'melody':
                steps = len(note_list)
            for val in note_list:    #so we don't forget to add the very first val in song
                self._add_notes(MyMIDI, track, channel, val, time + i, duration/steps, volume)
                i += 1/steps
        return MyMIDI

    # write_song_to_file, provided a MIDIFile and file name, will write a MIDIFile to a file
    def write_song_to_file(self, myMIDI, filename):
        if '.mid' not in filename:
            filename += '.mid'
        with open(filename, 'wb') as output_file:
            myMIDI.writeFile(output_file) 
    
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
    def generate_MIDI(self, final_song, volume=100):

        channel=0
        duration=1
        tempo=metadata['TEMPO']

        note_tracks = final_song.to_list()

        tracks = len(note_tracks)
        MyMIDI = MIDIFile(tracks)


        for i in range(0,len(note_tracks)):
            
            track_idx=i # 0,1,2 for melody,bass,appreg respectively
            track = note_tracks[track_idx]
            MyMIDI.addTempo(track_idx, 0, tempo)

            self._add_song_to_MIDI(MyMIDI, track, track_idx, channel, 0, duration, volume)

        return MyMIDI


class Chunk_Generator:

    # The function for generating an individual chunk of song
    def make_chunk(self, root=metadata['ROOT'], type='verse',verbose=False):
        if type == 'verse':
            bass = [self._get_random_prog(major=metadata['USER_KEY_MAJOR'])]
            track_type = 'verse'
        else:
            bass = [self._get_random_bridge(major=metadata['USER_KEY_MAJOR'])]
            track_type = 'bridge'

        if (len(bass[0]) == 4) and random.random() > 0.5:
            metadata['MELODY_NOTES_PB'] /= 2
            metadata['MELODY_NOTES_PB'] += metadata['MELODY_NOTES_PB'] % 2

        melody = self._make_melody(len(bass[0]), metadata['USER_KEY_MAJOR'], verbose=verbose)
        appregio = self._get_random_chord(bass[0], major=metadata['USER_KEY_MAJOR'])
        if verbose:
            print('melody: ', melody)
            print('bass: ', bass)
            print('appregio:', appregio)

        bass_track = BassTrack(bass)
        melody_track = MelodyTrack(melody)
        appregio_track = AppregioTrack(appregio)

        return Song(track_type=track_type, melody=melody_track,bass=bass_track,appregio=appregio_track) 

    # returns a random progression, dependent on 'major' value
    def _get_random_prog(self, major=True):
        if major:
            return random_major_prog(note_in_octs_l(get_random_letter(), 2, 3))
        return random_minor_prog(note_in_octs_l(get_random_letter(), 2, 3))

    def _get_random_bridge(self, major=True):
        if major:
            return random_major_bridge(note_in_octs_l(get_random_letter(), 2, 3))
        return random_minor_bridge(note_in_octs_l(get_random_letter(), 2, 3))


    def _get_random_chord(self, bass, major=True, reverse_chance=0.5):
        if major:
            to_ret = [random_major_chord(note_in_octs_n(n[0], 4, 5)) for n in bass]
        else: 
            to_ret = [random_minor_chord(note_in_octs_n(n[0], 4, 5)) for n in bass]
        # check if we want to reverse the appregio
        if random.random() < reverse_chance:
            to_ret.reverse()
        return replace_item_with_list(to_ret)

    def _get_random_drums(self):
        return [[random.choice(1,1,1,1,1,1,1,3)], [random.choice(1,1,3)], [random.choice(1,1,1,1,1,1,1,3)], [random.choice(1,1,3)]]

    def _make_melody(self, bass_count, major, verbose=False):
        song = []
        next_note = random.randint(4, 9)
        if verbose:
            print(next_note)
            # print(note_count)
            print(major)

        for b_note in range(bass_count):
            song.append([])
            note_count = 2 ** random.randint(1, 3)
            i = 1
            while i <= note_count:
                rand_note = random_root()
                if verbose:
                    print(str(i) + ':',str(rand_note % 12), major_notes(metadata['ROOT'] % 12))
                # if abs(song[-1][0] - rand_note) < next_note:
                if major and rand_note % 12 in major_notes(metadata['ROOT'] % 12):
                    song[b_note].append([rand_note])
                elif not major and rand_note % 12 in minor_notes(metadata['ROOT'] % 12):
                    song[b_note].append([rand_note])
                else:
                    i -= 1
                i += 1
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