#!/usr/bin/env python3

from speech_to_text import SpeechToText
import numpy as np
import speech_recognition as sr


sample_rate = 16000
STT = SpeechToText('/home/swayam/tensor2tensor/model_v1') #en_16k
audio_file = "/home/swayam/Desktop/test.wav"

if __name__ == '__main__':
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=sample_rate) as source:
        print("Say Something")
        audio = r.listen(source)
        with open("/home/swayam/Desktop/test.wav", "wb") as file:
            file.write(audio.get_wav_data())
    txt = STT('/home/swayam/Desktop/test.wav')
    print(txt.get('text'))
    
    
    
    
    

    
