def user_choose_key():
    key = ''
    while key not in ['major', 'minor']:
        key = input('Please select a key for your song.\nEnter \'major\' or \'minor\': ').lower()
    return key

if __name__ == '__main__':
    from _util import *
    from ga import *
    
    key_in_major = user_choose_key() == 'major'
    
    sg = Song_Generator(key_in_major)
    cg = Chunk_Generator()

    song,bass,appreg = cg.make_chunk(type='verse',verbose=False)
    
    
    sg.generate_MIDI([song, bass, appreg], steps=[8, 1, 'appreg'])
    sg.write_song_to_file("test2.mid")