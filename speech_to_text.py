"""
Speech-to-text pipeline
"""

from media import Media
from model import Model
from segment import Segment
from transcriber import Transcriber


class SpeechToText():
    """
    Speech-to-text
    """

    def __init__(self, model_name):
        self._model = self._load_model(model_name)

    @staticmethod
    def _load_model(model_name):
        model = Model(model_name)
        return model

    def __call__(self, file_path):
        model = self._model
        media = Media(file_path)
        segment = Segment(waveform=media.waveform,
                          boundaries=(0.0, media.duration),
                          sample_rate=media.sample_rate,
                          channel=0)
        transcriber = Transcriber(model)
        text, score = transcriber(segment)
        result = {
            'file': file_path,
            'sample_rate': media.sample_rate,
            'begin': segment.boundaries[0],
            'end': segment.boundaries[1],
            'channel': segment.channel,
            'text': text,
            'score': score
        }
        return result
