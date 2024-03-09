import asyncio
from shazamio import Shazam
import os

async def recognize_and_rename(audio_file):
    try:
        shazam = Shazam()
        out = await shazam.recognize(audio_file)  # Provide full path with file extension
        if out['track']['title']:
            song_name = out['track']['title']
            if out['track']['subtitle']:
                creator_name = out['track']['subtitle']
            else:
                creator_name = ""

            # Remove forbidden characters from the file name
            forbidden_chars = '/\\?%*:|"<>'
            new_song_name = ''.join(c for c in song_name if c not in forbidden_chars)
            new_creator_name = ''.join(c for c in creator_name if c not in forbidden_chars)

            # Rename the file to the artist's name
            renamed_file = os.path.join(os.path.dirname(audio_file), f"{new_creator_name} - {new_song_name}{os.path.splitext(audio_file)[1]}")
            os.rename(audio_file, renamed_file)
            print("File renamed to:", f"{new_creator_name} - {new_song_name}")
        else:
            print("Song recognition failed for file:", audio_file)
    except Exception as e:
        print(f"An error occurred while processing file {audio_file}: {e}")

async def main():
    current_directory = os.getcwd()
    song_directory = os.path.join(current_directory, "song")  # Create 'songs' directory in the current directory

    for filename in os.listdir(song_directory):
        if filename.endswith((".mp3", ".wav", ".ogg")):  # Adjust this line for supported file extensions
            audio_file = os.path.join(song_directory, filename)
            await recognize_and_rename(audio_file)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
