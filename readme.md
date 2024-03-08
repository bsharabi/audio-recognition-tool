# Audio Recognition and Renaming Tool
This tool is designed to recognize audio files and rename them based on the recognized song's metadata.

## Description
The tool utilizes the Shazam API to recognize audio files and extract metadata such as the song name and artist. It then renames the audio files using this metadata.

## Features
* Recognize audio files using the Shazam API
* Extract song metadata (song name, artist)
* Rename audio files based on the recognized metadata

## Installation
1. Clone this repository:

```bash
git clone https://github.com/bsharabi/audio-recognition-tool.git
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```
## Usage
1. Place your audio files in the same directory as the script.

2. Run the script:
```bash
python recognize_and_rename.py
```
3. The script will recognize each audio file in the directory and rename it based on the recognized song's metadata.

## Requirements
* Python 3.x
* shazamio library
* Internet connection (for using the Shazam API)

License
This project is licensed under the MIT License - see the LICENSE file for details.