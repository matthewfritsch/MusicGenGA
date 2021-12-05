def make_bridges(bridge_count):
    bridges = []
    for bridge in range(bridge_count):
        bridges.append(cg.make_chunk(type='bridge',verbose=False))
    return bridges

def make_verses(verse_count):
    verses = []
    for verse in range(verse_count):
        verses.append(cg.make_chunk(type='verse',verbose=False))
    return verses

if __name__ == '__main__':
    from _util import *
    from ga import *

    key_in_major = user_chose_major()
    tempo = user_choose_tempo()
    if tempo in tempos.keys():
        tempo = tempos[tempo]

    sg = Song_Generator(key_in_major, tempo)
    cg = Chunk_Generator()

    use_this_song = False
    verse_count = 2
    bridge_count = 2
    filename = 'my_song.mid'
    verses = []
    bridges = []

    while not use_this_song:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Now generating a new song...')

        bridges = make_bridges(bridge_count)
        verses = make_verses(verse_count)
        sg.create_MIDI(verse_list=verses, bridge_list=bridges, filename=filename)
       
        print('Done!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        use_this_song = user_likes_song(filename)

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    filename_format = filename.split('.mid')
    for i in range(verse_count-1):
        new_filename = filename_format[0] + str(i+1) + '.mid'
        print('Creating', new_filename)
        new_verses = verses
        for j in range(len(verses)):
            if i == j:
                continue
            new_verses[j] = cg.make_chunk(type='verse',verbose=False)
        new_bridges = make_bridges(bridge_count)
        sg.create_MIDI(verse_list=verses, bridge_list=bridges, filename=new_filename)

    for i in range(bridge_count-1):
        new_filename = filename_format[0] + str(i+j+1) + '.mid'
        print('Creating', new_filename)
        new_verses = make_verses(verse_count)
        new_bridges = bridges
        for j in range(len(bridges)):
            if i == j:
                continue
            new_bridges[j] = cg.make_chunk(type='bridge',verbose=False)
        sg.create_MIDI(verse_list=verses, bridge_list=bridges, filename=new_filename)

    print('Done!')