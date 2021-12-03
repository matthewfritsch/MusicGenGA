
if __name__ == '__main__':
    from _util import *
    from ga import *
    
    tempos = {
        'fast': metadata['TEMPO_FAST'], 
        'medium': metadata['TEMPO_MED'], 
        'slow': metadata['TEMPO_SLOW'], 
        }

    key_in_major = user_chose_major()
    tempo = user_choose_tempo()
    if tempo in tempos.keys():
        tempo = tempos[tempo]

    sg = Song_Generator(key_in_major, tempo)
    cg = Chunk_Generator()

    song_obj_v = cg.make_chunk(type='verse',verbose=False)
    song_obj_b = cg.make_chunk(type='bridge',verbose=False)

    sg.create_MIDI(verse_list=[song_obj_v])