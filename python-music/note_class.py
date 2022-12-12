import time
import numpy as np
import pyaudio
#DISCLAIMER: give reasonable frequency and sampling rate values or you may run into some problems with larger values
class Note: 
    def __init__(self, frequency: float, sampling_rate: int, volume: float, duration: float) -> None:
        '''
        Creates a note. Volume value must lie between [0, 1]. Sampling rate must be an integer.
        Sampling rate and duration are measured in seconds. Frequency is in Hertz.
        '''
        self.__frequency = frequency
        self.__sampling_rate = sampling_rate
        self.__volume = volume
        self.__duration = duration
        if self.__duration < 0:
            self.__duration = self.__duration*(-1)
        if self.__volume > 1:
            self.__volume = 1
        if self.__volume < 0:
            self.__volume = 0    
        self.__sampling_rate = int(self.__sampling_rate)
        if self.__frequency >= (self.__sampling_rate)//2:
            self.__sampling_rate = int(self.__frequency*4)
            
    def get_frequency(self) -> float:
        '''
        Returns note frequency value
        '''
        return self.__frequency
    
    def get_sampling_rate(self) -> int:
        '''
        Returns note sampling rate value
        '''
        return self.__sampling_rate
    
    def get_volume(self) -> float:
        '''
        Returns note volume value
        '''
        return self.__volume
    
    def get_duration(self) -> float:
        '''
        Returns note duration value
        '''
        return self.__duration
    
    def change_frequency(self, freq: float) -> None: # Also adjusts sampling rate
        self.__frequency = freq
        if self.__frequency >= (self.__sampling_rate)//2:
            self.__sampling_rate = int(self.__frequency*4)
    
    def change_volume(self, vol: float) -> None:
        '''
        Changes note volume
        '''
        if vol < 0:
            self.__volume = 0
        if vol > 1:
            self.volume = 1
        if (vol > 0) and (vol < 1):
            self.__volume = vol
    
    def change_duration(self, dur: float) -> None:
        '''
        Changes note duration
        '''
        if dur >= 0:
            self.__duration = dur
    
    def note_info(self) -> str:
        '''
        Prints note information
        '''
        print(f'Frequency: {self.get_frequency()}, Sampling rate: {self.get_sampling_rate()}, Volume: {self.get_volume()}, Duration: {self.get_duration()}')    

    def play(self) -> None:
        '''
        Plays a sine wave using note information
        '''
        soundwave = (np.sin(2 * np.pi * np.arange(self.get_sampling_rate()*self.get_duration())*self.get_frequency() / self.get_sampling_rate())).astype(np.float32)
        sound_convert = (soundwave*self.get_volume()).tobytes()    
        audio_clip = pyaudio.PyAudio()
        stream = audio_clip.open(format=pyaudio.paFloat32, channels=1, rate=self.get_sampling_rate(), output=True)    
        stream.write(sound_convert)
        audio_clip.terminate()