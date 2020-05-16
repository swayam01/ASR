# ASR
## Install via pip
- Python >= 3.6
- Tensorflow = 1.14
- Scipy (for reading wav files)

RUN `mic.py`

# Limitations

- The max duration of your audio file should be less than **15 seconds** else an error will not be thrown if the duration exceeds and your transcript may contain errors and missing text.
- Trained on english audio with Indian Accent recorded at 16 KHz
