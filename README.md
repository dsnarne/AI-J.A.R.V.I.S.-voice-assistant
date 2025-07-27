# AI Voice Assistant: D.E.E.R (Digital Enhanced Electronic Responder)

**Your personal JARVIS-like voice assistant for natural conversations 🎙️🤖**

A streamlined, terminal-based AI voice assistant that lets you have natural conversations with AI. Speak to it, and it responds with your own cloned voice using advanced AI technology.

## Features

- **🎤 Speech-to-Text**: Uses OpenAI Whisper for accurate speech recognition
- **🤖 AI Intelligence**: Powered by OpenAI GPT-4o for intelligent responses
- **🔊 Text-to-Speech**: ElevenLabs TTS with your cloned voice for natural responses
- **⌨️ Simple Controls**: Press Enter to start/stop recording, Ctrl+C to exit
- **🎯 Voice Cloning**: Uses your own voice ID for personalized responses
- **⚡ Real-time**: Instant voice interaction without web interfaces

## Quick Start

### Prerequisites

- Python 3.9+
- OpenAI API key
- ElevenLabs API key and voice ID
- macOS/Linux/Windows

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/AI-Voice-assistant.git
cd AI-Voice-assistant
```

2. **Create and activate virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
ELEVENLABS_VOICE_ID=your_cloned_voice_id_here
```

### Running the Assistant

```bash
python ai_voice_assistant.py
```

## Usage

1. **Start the assistant** - Run the script
2. **Press Enter** - Start recording your voice
3. **Speak naturally** - Ask questions, have conversations
4. **Press Enter again** - Stop recording and get AI response
5. **Listen** - AI responds with your cloned voice
6. **Repeat** - Continue the conversation
7. **Exit** - Press Ctrl+C to quit

## Configuration

All settings are centralized in `config.py`:

- **OpenAI Model**: `gpt-4o` (latest GPT-4)
- **Response Length**: 200 tokens max
- **Creativity**: Temperature 0.7 (balanced)
- **Audio Quality**: 16kHz, mono
- **Whisper Model**: Base model for transcription

## Project Structure

```
AI-Voice-assistant/
├── ai_voice_assistant.py    # Main application
├── config.py                # Configuration settings
├── requirements.txt         # Python dependencies
├── .env                    # API keys (not in repo)
├── README.md              # This file
└── .gitignore             # Git ignore rules
```

## API Setup

### OpenAI
1. Get API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Add to `.env` as `OPENAI_API_KEY`

### ElevenLabs
1. Get API key from [ElevenLabs](https://elevenlabs.io/)
2. Create or clone a voice and get the voice ID
3. Add to `.env` as `ELEVENLABS_API_KEY` and `ELEVENLABS_VOICE_ID`

## Troubleshooting

### Common Issues

**"No module named 'whisper'"**
```bash
pip install openai-whisper
```

**"ffmpeg not found"**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

**"PortAudio not found"**
```bash
# macOS
brew install portaudio

# Ubuntu/Debian
sudo apt install portaudio19-dev
```

**SSL Certificate Issues (macOS)**
```bash
/Applications/Python\ 3.*/Install\ Certificates.command
```

### Audio Issues
- Ensure microphone permissions are granted
- Check system audio settings
- Try different audio devices if available

## Dependencies

- **openai**: GPT-4o API access
- **elevenlabs**: Text-to-speech with voice cloning
- **openai-whisper**: Speech-to-text transcription
- **sounddevice**: Audio recording
- **pygame**: Audio playback
- **scipy/numpy**: Audio processing
- **python-dotenv**: Environment variable management

## Security Notes

- `.env` file is excluded from version control
- API keys are never committed to the repository
- Use environment variables for all sensitive data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

---

**Enjoy your personal AI voice assistant! 🎤🤖**


