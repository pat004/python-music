import keyboard
from note_class import Note

A4 = Note(440,44100,0.20,0.20) # reference point for equal tone tuning

C4 = Note(A4.get_frequency()*(2**(-9/12)),44100,0.50,0.20)
C4_SHARP = Note(C4.get_frequency()*(2**(1/12)),44100,0.50,0.20)
D4 = Note(C4_SHARP.get_frequency()*(2**(1/12)),44100,0.50,0.20)
D4_SHARP = Note(D4.get_frequency()*(2**(1/12)),44100,0.50,0.20)
E4 = Note(D4_SHARP.get_frequency()*(2**(1/12)),44100,0.50,0.20)
F4 = Note(E4.get_frequency()*(2**(1/12)),44100,0.50,0.20)
F4_SHARP = Note(F4.get_frequency()*(2**(1/12)),44100,0.50,0.20)
G4 = Note(F4_SHARP.get_frequency()*(2**(1/12)),44100,0.50,0.20)
G4_SHARP = Note(G4.get_frequency()*(2**(1/12)),44100,0.50,0.20)
# A4 goes here
A4_SHARP = Note(A4.get_frequency()*(2**(1/12)),44100,0.50,0.20)
B4 = Note(A4_SHARP.get_frequency()*(2**(1/12)),44100,0.50,0.20)
C5 = Note(C4.get_frequency()*2,44100,0.50,0.20)

C3 = Note(A4.get_frequency()*(2**(-21/12)),44100,1,0.20)
C3_SHARP = Note(C3.get_frequency()*(2**(1/12)),44100,1,0.20)
D3 = Note(C3_SHARP.get_frequency()*(2**(1/12)),44100,1,0.20)
D3_SHARP = Note(D3.get_frequency()*(2**(1/12)),44100,1,0.20)
E3 = Note(D3_SHARP.get_frequency()*(2**(1/12)),44100,1,0.20)
F3 = Note(E3.get_frequency()*(2**(1/12)),44100,1,0.20)
F3_SHARP = Note(F3.get_frequency()*(2**(1/12)),44100,1,0.20)
G3 = Note(F3_SHARP.get_frequency()*(2**(1/12)),44100,1,0.20)
G3_SHARP = Note(G3.get_frequency()*(2**(1/12)),44100,1,0.20)
A3 = Note(A4.get_frequency()/2,44100,1,0.20)
A3_SHARP = Note(A3.get_frequency()*(2**(1/12)),44100,1,0.20)
B3 = Note(A3_SHARP.get_frequency()*(2**(1/12)),44100,1,0.20)
# C4 goes here

# C5 goes here
C5_SHARP = Note(C5.get_frequency()*(2**(1/12)),44100,0.25,0.20)
D5 = Note(C5_SHARP.get_frequency()*(2**(1/12)),44100,0.25,0.20)
D5_SHARP = Note(D5.get_frequency()*(2**(1/12)),44100,0.25,0.20)
E5 = Note(D5_SHARP.get_frequency()*(2**(1/12)),44100,0.25,0.20)
F5 = Note(E5.get_frequency()*(2**(1/12)),44100,0.20,0.25)
F5_SHARP = Note(F5.get_frequency()*(2**(1/12)),44100,0.25,0.20)
G5 = Note(F5_SHARP.get_frequency()*(2**(1/12)),44100,0.25,0.20)
G5_SHARP = Note(G5.get_frequency()*(2**(1/12)),44100,0.25,0.20)
A5 = Note(A4.get_frequency()*2,44100,0.20,0.20)
A5_SHARP = Note(A5.get_frequency()*(2**(1/12)),44100,0.25,0.20)
B5 = Note(A5_SHARP.get_frequency()*(2**(1/12)),44100,0.25,0.20)
C6 = Note(C5.get_frequency()*2,44100,0.25,0.20)

def pyano_test() -> None:
    '''
    Uses keyboard inputs to play notes... Simulates a piano
    '''
    print('Press 0 on keyboard to close pyano')
    while not keyboard.is_pressed('0'):
        if keyboard.is_pressed('z'): 
            C4.play()
        if keyboard.is_pressed('s'): 
            C4_SHARP.play()
        if keyboard.is_pressed('x'): 
            D4.play()
        if keyboard.is_pressed('d'): 
            D4_SHARP.play()
        if keyboard.is_pressed('c'):
            E4.play()
        if keyboard.is_pressed('v'):
            F4.play()
        if keyboard.is_pressed('g'): 
            F4_SHARP.play()
        if keyboard.is_pressed('b'):
            G4.play()
        if keyboard.is_pressed('h'): 
            G4_SHARP.play()
        if keyboard.is_pressed('n'): 
            A4.play()
        if keyboard.is_pressed('j'): 
            A4_SHARP.play()
        if keyboard.is_pressed('m'): 
            B4.play()
        if keyboard.is_pressed(','): 
            C5.play()
    print('Pyano closed')

def middle_octave(n) -> None:
    '''
    middle octave of the pyano (4th octave of piano)
    '''
    print('middle octave')
    while n == 1:
        if not keyboard.is_pressed('2') or not keyboard.is_pressed('3') or not keyboard.is_pressed('0'):
            if keyboard.is_pressed('z'): 
                C4.play()
            if keyboard.is_pressed('s'): 
                C4_SHARP.play()
            if keyboard.is_pressed('x'): 
                D4.play()
            if keyboard.is_pressed('d'): 
                D4_SHARP.play()
            if keyboard.is_pressed('c'):
                E4.play()
            if keyboard.is_pressed('v'):
                F4.play()
            if keyboard.is_pressed('g'): 
                F4_SHARP.play()
            if keyboard.is_pressed('b'):
                G4.play()
            if keyboard.is_pressed('h'): 
                G4_SHARP.play()
            if keyboard.is_pressed('n'): 
                A4.play()
            if keyboard.is_pressed('j'): 
                A4_SHARP.play()
            if keyboard.is_pressed('m'): 
                B4.play()
            if keyboard.is_pressed(','): 
                C5.play()  
        if keyboard.is_pressed('2'):
            n = 2
        if keyboard.is_pressed('3'):
            n = 3
        if keyboard.is_pressed('0'):
            n = 0        
    
def lower_octave(n) -> None:
    '''
    lower octave of the pyano (3rd octave of piano)
    '''
    print('lower octave')
    while n == 2:
        if not keyboard.is_pressed('1') or not keyboard.is_pressed('3') or not keyboard.is_pressed('0'):
            if keyboard.is_pressed('z'): 
                C3.play()
            if keyboard.is_pressed('s'): 
                C3_SHARP.play()
            if keyboard.is_pressed('x'): 
                D3.play()
            if keyboard.is_pressed('d'): 
                D3_SHARP.play()
            if keyboard.is_pressed('c'):
                E3.play()
            if keyboard.is_pressed('v'):
                F3.play()
            if keyboard.is_pressed('g'): 
                F3_SHARP.play()
            if keyboard.is_pressed('b'):
                G3.play()
            if keyboard.is_pressed('h'): 
                G3_SHARP.play()
            if keyboard.is_pressed('n'): 
                A3.play()
            if keyboard.is_pressed('j'): 
                A3_SHARP.play()
            if keyboard.is_pressed('m'): 
                B3.play()
            if keyboard.is_pressed(','): 
                C4.play()
        if keyboard.is_pressed('1'):
            n = 1
        if keyboard.is_pressed('3'):
            n = 3
        if keyboard.is_pressed('0'):
            n = 0        

def upper_octave(n) -> None:
    '''
    upper octave of the pyano (5th octave of piano)
    '''
    print('upper octave')
    while n == 3:
        if not keyboard.is_pressed('1') or not keyboard.is_pressed('2') or not keyboard.is_pressed('0'):
            if keyboard.is_pressed('z'): 
                C5.play()
            if keyboard.is_pressed('s'): 
                C5_SHARP.play()
            if keyboard.is_pressed('x'): 
                D5.play()
            if keyboard.is_pressed('d'): 
                D5_SHARP.play()
            if keyboard.is_pressed('c'):
                E5.play()
            if keyboard.is_pressed('v'):
                F5.play()
            if keyboard.is_pressed('g'): 
                F5_SHARP.play()
            if keyboard.is_pressed('b'):
                G5.play()
            if keyboard.is_pressed('h'): 
                G5_SHARP.play()
            if keyboard.is_pressed('n'): 
                A5.play()
            if keyboard.is_pressed('j'): 
                A5_SHARP.play()
            if keyboard.is_pressed('m'): 
                B5.play()
            if keyboard.is_pressed(','): 
                C6.play()
        if keyboard.is_pressed('1'):
            n = 1
        if keyboard.is_pressed('2'):
            n = 2
        if keyboard.is_pressed('0'):
            n = 0        

def pyano() -> None:
    '''
    pyano but with 3 octaves
    '''
    print('Press 1 on keyboard for middle octave\nPress 2 on keyboard for lower octave\nPress 3 on keyboard for upper octave\nPress 0 on keyboard to close pyano')
    n = True
    while not keyboard.is_pressed('0') or n == 0:
        if keyboard.is_pressed('1'):
            n = 1
            middle_octave(n)
        if keyboard.is_pressed('2'):
            n = 2
            lower_octave(n)
        if keyboard.is_pressed('3'):
            n = 3
            upper_octave(n)
    print('pyano closed')