import time
import numpy as np
import pyaudio

audio_clip = pyaudio.PyAudio()

volume = 0.25  # range [0.0, 1.0]
SR = 44100  # sampling rate, Hz, must be integer
whole_beat = 1.0 # in seconds, may be float
half_beat = 0.5 
quarter_beat = 0.25
sixteenth = 0.125 
f = 440.0  # sine frequency, Hz, may be float

A4 = f//1
A3 = A4//2
A2 = A3//2
A1 = A2//2
A0 = A1//2
A5 = A4*2
A6 = A5*2
A7 = A6*2


C4 = A4*(2**(-9/12)) # equal tone tuning for C4
C4_SHARP = C4*(2**(1/12))
D4 = C4_SHARP*(2**(1/12))
D4_SHARP = D4*(2**(1/12))
E4 = D4_SHARP*(2**(1/12))
F4 = E4*(2**(1/12))
F4_SHARP = F4*(2**(1/12))
G4 = F4_SHARP*(2**(1/12))
G4_SHARP = G4*(2**(1/12))
A4 = 440
A4_SHARP = A4*(2**(1/12))
B4 = A4_SHARP*(2**(1/12))
C5 = C4*2 # Octave

# generate samples, note conversion to float32 array

sample0 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * C4 / SR)).astype(np.float32)
sample1 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * C4_SHARP / SR)).astype(np.float32)
sample2 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * D4 / SR)).astype(np.float32)
sample3 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * D4_SHARP / SR)).astype(np.float32)
sample4 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * E4 / SR)).astype(np.float32)
sample5 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * F4 / SR)).astype(np.float32)
sample6 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * F4_SHARP / SR)).astype(np.float32)
sample7 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * G4 / SR)).astype(np.float32)
sample8 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * G4_SHARP / SR)).astype(np.float32)
sample9 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * A4 / SR)).astype(np.float32)
sample10 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * A4_SHARP / SR)).astype(np.float32)
sample11 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * B4 / SR)).astype(np.float32)
sample12 = (np.sin(2 * np.pi * np.arange(SR * quarter_beat) * C5 / SR)).astype(np.float32)

# per @yahweh comment explicitly convert to bytes sequence
output0 = (volume * sample0).tobytes()
output1 = (volume*sample1).tobytes()
output2 = (volume*sample2).tobytes()
output3 = (volume*sample3).tobytes()
output4 = (volume*sample4).tobytes()
output5 = (volume*sample5).tobytes()
output6 = (volume*sample6).tobytes()
output7 = (volume*sample7).tobytes()
output8 = (volume*sample8).tobytes()
output9 = (volume*sample9).tobytes()
output10 = (volume*sample10).tobytes()
output11 = (volume*sample11).tobytes()
output12 = (volume*sample12).tobytes()

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = audio_clip.open(format=pyaudio.paFloat32,
                channels=1,
                rate=SR,
                output=True)

# play. May repeat with different volume values (if done interactively)
start_time = time.time()
stream.write(output0)
stream.write(output1)
stream.write(output2)
stream.write(output3)
stream.write(output4)
stream.write(output5)
stream.write(output6)
stream.write(output7)
stream.write(output8)
stream.write(output9)
stream.write(output10)
stream.write(output11)
stream.write(output12)

print(f"Duration: {(time.time() - start_time):.2f} seconds")

stream.stop_stream()
stream.close()

audio_clip.terminate()