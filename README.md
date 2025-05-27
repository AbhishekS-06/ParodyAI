# ParodyAI

A parody song generator that creates and mixes AI-generated lyrics with instrumentals.

## Prerequisites

- Python 3.9 or higher
- FFmpeg (required for audio processing)

### Installing FFmpeg

#### On macOS:
```bash
brew install ffmpeg
```

#### On Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

#### On Windows:
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Add FFmpeg to your system PATH

## Quick Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/RecordHacks.git
cd RecordHacks
```

2. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

3. Run the installation script:
```bash
./install.sh  # On macOS/Linux
# OR
bash install.sh  # On Windows
```

## Manual Installation (if the script doesn't work)

1. Create a virtual environment:
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
```bash
# On macOS/Linux:
source venv/bin/activate

# On Windows:
.\venv\Scripts\activate
```

3. Install the package:
```bash
pip3 install -e .
```

## Running the Application

1. Make sure your virtual environment is activated
2. Start the server:
```bash
python3 server.py
```
3. Open http://localhost:5000 in your web browser

## Features

1. **Generate Parody Lyrics**  
   - AI generates clever and funny parody lyrics while maintaining the rhythm and rhyme of the original song.
2. **Text-to-Singing AI**  
   - Converts parody lyrics into realistic vocals using AI-powered voice synthesis.
3. **Instrumental and Vocal Mixing**  
   - Overlays generated vocals on the instrumental track to produce a complete parody song.

## Troubleshooting

If you encounter installation issues:

1. Try using specific versions of packages:
```bash
pip3 uninstall openai spleeter httpx
pip3 install openai==0.27.8 spleeter==2.3.2 httpx==0.19.0
```

2. If you get SSL errors:
```bash
pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org -e .
```

3. For torch/torchaudio issues:
```bash
pip3 install torch torchaudio
```

4. For demucs installation problems:
```bash
pip3 install torch torchaudio
pip3 install demucs
```

5. Verify FFmpeg installation:
```bash
ffmpeg -version
```

## File Structure

```
RecordHacks/
├── parody_generator.py     # Generates parody lyrics
├── server.py              # Flask server for web interface
├── main.py               # Handles audio separation and mixing
├── edge.py              # Text-to-speech synthesis
├── download_song_as_mp3.py # Downloads songs from YouTube
├── templates/           # HTML templates
├── static/             # CSS and JS files
├── requirements.txt    # Python dependencies
├── setup.py           # Package configuration
├── install.sh         # Installation script
└── README.md         # Documentation
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.