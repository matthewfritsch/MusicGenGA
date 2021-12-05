def make_bridge():
    return [cg.make_chunk(type='bridge',verbose=False)]

def make_verse():
    return [cg.make_chunk(type='verse',verbose=False)]

if __name__ == '__main__':
    from _util import *
    from ga import *

    key_in_major = user_chose_major()
    tempo = user_choose_tempo()
    if tempo in tempos.keys():
        tempo = tempos[tempo]

    sg = Song_Generator(key_in_major, tempo)
    cg = Chunk_Generator(tempo)

    use_this_song = False
    verse_count = 4
    bridge_count = 4
    filename = 'my_song.mid'
    verse = []
    bridge = []

    while not use_this_song:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Now generating a new song...')

        bridge = make_bridge()
        verse = make_verse()
        sg.create_MIDI(verse_list=verse, bridge_list=bridge, filename=filename)
       
        print('Done!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        use_this_song = user_likes_song(filename)

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    filename_format = filename.split('.mid')

    for i in range(bridge_count):
        new_filename = filename_format[0] + str(i+1) + '.mid'
        print('Creating', new_filename)
        new_verse = make_verse()
        new_bridge = bridge
        sg.create_MIDI(verse_list=new_verse, bridge_list=new_bridge, filename=new_filename)
    
    for j in range(verse_count):
        new_filename = filename_format[0] + str(i+j+2) + '.mid'
        print('Creating', new_filename)
        new_verse = verse
        new_bridge = make_bridge()
        sg.create_MIDI(verse_list=new_verse, bridge_list=new_bridge, filename=new_filename)

    print('Done!')