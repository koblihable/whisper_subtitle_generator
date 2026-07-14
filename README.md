# Whisper Audio Tools

Python utilities built with OpenAI Whisper for converting speech into text.

The repository contains two command-line scripts:

Audio transcription – generates a plain text transcript.
Subtitle generation – creates timestamped subtitles in SRT format.

These scripts are useful for quickly transcribing lectures, interviews, podcasts, meetings, or videos.

---

## Features

- Speech-to-text transcription
- Plain text transcript generation
- Automatic subtitle creation (SRT)
- Simple command-line interface
- Using OpenAI Whisper
- By default using the base model, this can be manually updated in the script
`model = whisper.load_model('base')`
    - Other available models include:
      - tiny
      - base
      - small
      - medium
      - large
  
---

## Requirements

Install the required packages:
`pip install openai-whisper`

Whisper also requires FFmpeg to process audio files
`sudo apt install ffmpeg`

---

## Example Workflow

### Audio Transcription

Generate a plain text transcript from an audio file.
`python transcribe_audio.py audio.m4a`

Creates a file in the base folder called transcript.txt

### Subtitle Generation

Generate subtitles in SRT format.
`python subtitle_audio.py audio.m4a`

Creates a file in the base folder called subtitles.srt

Example:

1
00:00:00,000 --> 00:00:04,000
Welcome to today's lecture.

2
00:00:04,000 --> 00:00:08,000
Let's begin.

---

## Future Improvements

Some ideas for future development include:

- Batch processing of multiple files
- Language selection
- Automatic translation
- Progress indicator
- Configurable Whisper model

---

## Author

Lenka Klementová

AI Engineer | Python Developer | NLP & LLM Engineer

GitHub: https://github.com/koblihable
LinkedIn: https://linkedin.com/in/lenka-klementova-70a78561
