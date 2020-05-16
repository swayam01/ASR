#!/usr/bin/env python3

import os
import sys
from speech_to_text import SpeechToText
import speech_recognition as sr

print('loading model...')
STT = SpeechToText(os.getcwd()+'/model_v1')
audio_file = sys.argv[1]
txt = STT(audio_file)
op = txt.get('text')
    
#with open(os.getcwd() + "/{}".format(audio_file.split('.')[0] + '.txt'), "w") as file:
#    file.write("{}: {}".format(audio_file.split('.')[0],op))
    
print(op)
    
    
    
    

    
