#!/usr/bin/env python3

import os
import time
import openai
import psutil
import argparse
from subprocess import Popen, DEVNULL, STDOUT

COMMAND_WORD = "beep"
RECORDING_LIMIT = 60
LANGUAGE = "es"
MODEL = "whisper-1"

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--abort', help='Do not process the recording.', action='store_true', default=False)
args = parser.parse_args()

#Get API key from file in .config
with open(os.path.expanduser("~/.config/hear/api_key"), "r") as f:
    openai_key = f.read().strip()

# Initialize OpenAI API
openai.api_key = (openai_key)

def message(text):
    os.system('notify-send "Hear" "{}"'.format(text))
    print(text)

def write_to_os(text):
    # Split text into individual words
    text = text.lower().split(COMMAND_WORD)
    writeable_text = text[0]
    commands = text[1:]

    # Write actual text
    for word in writeable_text:
        word = word

        os.system('xdotool type "{}"'.format(word))
        time.sleep(0.01)
    
    # Write commands
    for word in commands:
        #remove puctuation and spaces around word
        word = word.strip('.,;:!? ')

        os.system('xdotool key "{}"'.format(word))
        time.sleep(0.01)

def is_process_running():
    pid = 0
    for proc in psutil.process_iter():
        if proc.name() == "arecord":
            pid = proc.pid
            break

    if pid == 0:
        return False
    else:
        return True

# Starts audio capture using arecord indefinitely
def start_audio_capture():
    message('Capturing audio...') #notifies console, but useless
    Popen(['arecord', '-f', 'cd', '-t', 'wav', '-d', str(RECORDING_LIMIT), '/tmp/whisper_tmp.wav'], stdout=DEVNULL, stderr=STDOUT)

def stop_audio_capture():
    print('Stopping audio capture...') #intentionally just stdout

    #kill arecord process silently, otherwise outputs to console
    Popen(['pkill', '-f', 'arecord'], stdout=DEVNULL, stderr=STDOUT)

def main():
    if args.abort:
        stop_audio_capture()
        message('Aborted.')
        return
    
    # Check if process is already running
    if is_process_running():
        stop_audio_capture()

        #notification
        message("Processing audio...")
        response = openai.Audio.transcribe(MODEL, open("/tmp/whisper_tmp.wav", "rb"), language=LANGUAGE)
        write_to_os(response['text'])
    else:
        start_audio_capture()

if __name__ == '__main__':
    main()