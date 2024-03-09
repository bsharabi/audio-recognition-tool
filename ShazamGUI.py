import asyncio
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from shazamio import Shazam

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
            print("File renamed to:", renamed_file)
            messagebox.showinfo("Success", f"File renamed to: {renamed_file}")
        else:
            print("Song recognition failed for file:", audio_file)
            messagebox.showerror("Error", "Song recognition failed.")
    except Exception as e:
        print(f"An error occurred while processing file {audio_file}: {e}")
        messagebox.showerror("Error", f"An error occurred while processing file {audio_file}: {e}")

async def main(files):
    for audio_file in files:
        await recognize_and_rename(audio_file)

def select_files():
    files = filedialog.askopenfilenames(title="Select Audio Files", filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
    if files:
        asyncio.run(main(files))

# GUI
root = tk.Tk()
root.title("Audio Recognition and Renaming Tool")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

select_button = tk.Button(frame, text="Select Audio Files", command=select_files)
select_button.pack()

root.mainloop()
