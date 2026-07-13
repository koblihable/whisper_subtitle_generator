#!/usr/bin/env python3

import whisper
from datetime import timedelta

def subtitle_audio(file):

    model = whisper.load_model('base')
    transcribe = model.transcribe(audio=file)
    segments = transcribe['segments']

    with open('subtitles.txt', 'w', encoding='utf-8') as f:
        for segment in segments:
            startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
            endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
            text = segment['text']
            segmentId = segment['id']+1
            segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"
            f.write(segment)


if __name__ == "__main__":
    import sys
    subtitle_audio(sys.argv[1])
