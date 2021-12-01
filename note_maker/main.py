
if __name__ == '__main__':
    from _util import *
    from ga import *
    
    key_in_major = user_chose_major()
    


    sg = Song_Generator(key_in_major)
    cg = Chunk_Generator()

    song_obj = cg.make_chunk(root=random_root(),type='verse',verbose=False)
    # print(song_obj.song)
    # print(song_obj.bass)
    # print(song_obj.appregio)

    # print(len(bass)/int(metadata["DEFAULT_TEMPO"]/4))

    sg.create_MIDI(song_obj, 'test1.mid')