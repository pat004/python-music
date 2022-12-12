from note_class import Note

A4 = Note(440,44100,0.025,0.20)

BAR2 = (-120000,-120000,-120000,-120000,7,6,7,6,7,2,5,3) # each element in tuple represents a sixteenth in 3/8
BAR4 = (0,-120000,-120000,-9,-5,0,2,-12000,-12000,-5,-1,2) # large negative values act as rests
BAR6 = (3,-120000,-120000,-5,7,6,7,6,7,2,5,3)
BAR8 = (0,-120000,-120000,-9,-5,0,2,-120000,-12000,-7,3,2)
BAR9_REPEAT = (0,-120000,-120000,-120000,7,6)
BAR9_END = (0,-120000,-120000,2,3,5)
BAR12 = (7,-120000,-120000,-2,8,7,5,-120000,-120000,-4,7,5,3,-120000,-120000,-5,5,3)
BAR14 = (2,-17,-5,-5,7,-5,-5,7,19,-6,-5,6)
BAR16 = (7,-120000,-120000,6,7,6,7,6,7,2,5,3)
BAR18 = BAR4
BAR20 = BAR6
BAR22 = BAR8
BAR23_REPEAT = BAR9_END
BAR23_END = (0,)

def fur_elise(note: 'Note') -> None:
    tonic = Note(note.get_frequency(), note.get_sampling_rate(), note.get_volume(), note.get_duration())
    print('\nSecion 1:\n')
    for repeat in range(2):
        if repeat != 1:
            for degree in BAR2:
                tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
                tonic.note_info()
                tonic.play()
        else:
            for degree in BAR2[6:]:
                tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
                tonic.note_info()
                tonic.play()            
        for degree in BAR4:
            tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
            tonic.note_info()
            tonic.play()
        for degree in BAR6:
            tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
            tonic.note_info()
            tonic.play() 
        for degree in BAR8:
            tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
            tonic.note_info()
            tonic.play()
        if repeat != 1:
            for degree in BAR9_REPEAT:
                tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
                tonic.note_info()
                tonic.play()
        else:
            for degree in BAR9_END:
                tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
                tonic.note_info()
                tonic.play()
    print('\nSecion 2:\n')
    for repeat in range(2):
        for degree in BAR12:
            tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
            tonic.note_info()
            tonic.play()
        for degree in BAR14:
            tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
            tonic.note_info()
            tonic.play()
        for degree in BAR16:
            tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
            tonic.note_info()
            tonic.play()
        for degree in BAR18:
            tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
            tonic.note_info()
            tonic.play()
        for degree in BAR20:
            tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
            tonic.note_info()
            tonic.play()
        for degree in BAR22:
            tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
            tonic.note_info()
            tonic.play()
        if repeat != 1:
            for degree in BAR23_REPEAT:
                tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
                tonic.note_info()
                tonic.play()
        else:
            for degree in BAR23_END:
                tonic.change_frequency(note.get_frequency()*(2**(degree/12)))
                tonic.note_info()
                tonic.play()        

fur_elise(A4)