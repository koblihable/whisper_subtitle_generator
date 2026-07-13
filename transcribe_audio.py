#!/usr/bin/env python3

import whisper


def transcribe_audio(file):

    model = whisper.load_model('base')
    transcribe = model.transcribe(audio=file)
    segments = transcribe['segments']

    with open('transcript.txt', 'w', encoding='utf-8') as f:
        for segment in segments:
            text = segment['text']
            f.write(text)


if __name__ == "__main__":
    import sys
    transcribe_audio(sys.argv[1])
