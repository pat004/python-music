from note_class import Note

A4 = Note(440, 44100, 0.25, 0.25) # Reference point
C4 = Note(440*(2**(-9/12)), 44100, 0.25, 0.25)

MAJOR_SCALE = (0,2,2,1,2,2,2,1,-1,-2,-2,-2,-1,-2,-2) # Following tuples are scales
MINOR_SCALE = (0,2,1,2,2,1,2,2,-2,-2,-1,-2,-2,-1,-2) # Integers represent equal tone halfsteps
PENTATONIC_SCALE = (0,2,2,3,2,3,-3,-2,-3,-2,-2) # Halfsteps are from current position and not from tonic note
MAJOR_BLUES_SCALE = (0,2,1,1,3,2,3,-3,-2,-3,-1,-1,-2)
MINOR_BLUES_SCALE = (0,3,2,1,1,3,2,-2,-3,-1,-1,-2,-3)
CHROMATIC_SCALE = (0,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1)

# Pieces of the twelve bar blues below, assumes quarter notes and is based on a tonic note
BLUES_I = (0,4,7,9,10,9,7,4) # BARS 1-2, 3-4, 7-8
BLUES_IV = (5,9,12,14,15,14,12,9) # BARS 5-6
BLUES_V_IV = (7,11,14,16,5,9,12,14) # BARS 9-10
BLUES_I_END = (0,4,7,9,7,4,-2,0) # BARS 11-12

def chromatic_test(note: 'Note', halfsteps: int) -> None: # Based on equal tone tuning... rough function
    '''
    Plays a chromatic scale ascending or descending. Starts on a tonic note and 
    does not change direction.
    '''
    halfsteps = int(halfsteps)
    tonic = Note(note.get_frequency(), note.get_sampling_rate(), note.get_volume(), note.get_duration())
    if halfsteps > 0:
        for scale_note in range(0, halfsteps+1):
            tonic.change_frequency(note.get_frequency()*(2**(scale_note/12)))
            tonic.note_info()
            tonic.play() 
    elif halfsteps == 0:
        tonic.note_info()
        tonic.play()
    else:
        for scale_note in range(0, halfsteps-1, -1):
            tonic.change_frequency(note.get_frequency()*(2**(scale_note/12)))
            tonic.note_info()
            tonic.play() 

def major_scale(note: 'Note', octaves: int) -> None:
    '''
    Plays a major scale ascending then descending
    '''
    octaves = int(octaves)
    tonic = Note(note.get_frequency(), note.get_sampling_rate(), note.get_volume(), note.get_duration())
    if (octaves == 0) or (octaves == 1):
        for step in MAJOR_SCALE:
                tonic.change_frequency(tonic.get_frequency()*(2**(step/12)))
                tonic.note_info()
                tonic.play()
    else:
        for octave in range(octaves):
            for step in MAJOR_SCALE:
                if step >= 0:
                    if step == 0 and octave != 0:
                        step = 2
                    else:
                        tonic.change_frequency(tonic.get_frequency()*(2**(step/12)))
                        tonic.note_info()
                        tonic.play()
        for octave in range(octaves):
            for step in MAJOR_SCALE:
                if step < 0:
                    tonic.change_frequency(tonic.get_frequency()*(2**(step/12)))
                    tonic.note_info()
                    tonic.play()                         

def minor_scale(note: 'Note', octaves: int) -> None: # same function model as above
    '''
    Plays a minor scale ascending then descending
    '''
    octaves = int(octaves)
    tonic = Note(note.get_frequency(), note.get_sampling_rate(), note.get_volume(), note.get_duration())
    if (octaves == 0) or (octaves == 1):
        for step in MINOR_SCALE:
                tonic.change_frequency(tonic.get_frequency()*(2**(step/12)))
                tonic.note_info()
                tonic.play()
    else:
        for octave in range(octaves):
            for step in MINOR_SCALE:
                if step >= 0:
                    if step == 0 and octave != 0:
                        step = 2
                    else:
                        tonic.change_frequency(tonic.get_frequency()*(2**(step/12)))
                        tonic.note_info()
                        tonic.play()
        for octave in range(octaves):
            for step in MINOR_SCALE:
                if step < 0:
                    tonic.change_frequency(tonic.get_frequency()*(2**(step/12)))
                    tonic.note_info()
                    tonic.play()

def play_scale(note: 'Note', SCALE: tuple[int], octaves: int) -> None:
    '''
    Plays a scale ascending then descending
    '''
    octaves = int(octaves)
    tonic = Note(note.get_frequency(), note.get_sampling_rate(), note.get_volume(), note.get_duration())
    if (octaves == 0) or (octaves == 1):
        for step in SCALE:
                tonic.change_frequency(tonic.get_frequency()*(2**(step/12)))
                tonic.note_info()
                tonic.play()
    else:
        for octave in range(octaves):
            for step in SCALE:
                if step >= 0:
                    if step == 0 and octave != 0:
                        step = 2
                    else:
                        tonic.change_frequency(tonic.get_frequency()*(2**(step/12)))
                        tonic.note_info()
                        tonic.play()
        for octave in range(octaves):
            for step in SCALE:
                if step < 0:
                    tonic.change_frequency(tonic.get_frequency()*(2**(step/12)))
                    tonic.note_info()
                    tonic.play()

def twelve_bar_blues(note: 'Note', repeats: int) -> None:
    '''
    Plays a twelve bar blues bass line
    '''
    repeats = int(repeats)
    tonic = Note(note.get_frequency(), note.get_sampling_rate(), note.get_volume(), note.get_duration())
    for repeat in range(repeats):
        print(f'\nSection {repeat+1}:\n')
        for step in BLUES_I:
            tonic.change_frequency(note.get_frequency()*(2**(step/12)))
            tonic.note_info()
            tonic.play()
        for step in BLUES_I:
            tonic.change_frequency(note.get_frequency()*(2**(step/12)))
            tonic.note_info()
            tonic.play()
        for step in BLUES_IV:
            tonic.change_frequency(note.get_frequency()*(2**(step/12)))
            tonic.note_info()
            tonic.play()
        for step in BLUES_I:
            tonic.change_frequency(note.get_frequency()*(2**(step/12)))
            tonic.note_info()
            tonic.play()
        for step in BLUES_V_IV:
            tonic.change_frequency(note.get_frequency()*(2**(step/12)))
            tonic.note_info()
            tonic.play()
        for step in BLUES_I_END:
            tonic.change_frequency(note.get_frequency()*(2**(step/12)))
            tonic.note_info()
            tonic.play()