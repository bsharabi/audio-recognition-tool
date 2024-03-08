import asyncio
from shazamio import Shazam
import os

async def recognize_and_rename(audio_file):
    shazam = Shazam()
    out = await shazam.recognize(audio_file)  # Provide full path with file extension
    if out['track']['title']:
        song_name = out['track']['title']
        if out['track']['subtitle']:
            creator_name = out['track']['subtitle']
        else:
            creator_name = ""
        # Rename the file to the artist's name
        renamed_file = os.path.join(os.path.dirname(audio_file), creator_name + " - " + song_name+ os.path.splitext(audio_file)[1])
        os.rename(audio_file, renamed_file)
        print("File renamed to:", renamed_file)
    else:
        print("Song recognition failed for file:", audio_file)

async def main():
    current_directory = os.getcwd()
    song_directory = os.path.join(current_directory, "song")  # Create 'songs' directory in the current directory

    for filename in os.listdir(song_directory):
        if filename.endswith((".mp3", ".wav", ".ogg")):  # Adjust this line for supported file extensions
            audio_file = os.path.join(song_directory, filename)
            await recognize_and_rename(audio_file)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
