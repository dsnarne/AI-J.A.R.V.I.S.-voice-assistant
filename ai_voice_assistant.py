#!/usr/bin/env python3
"""
AI Voice Assistant
A clean, organized voice assistant with speech-to-text and text-to-speech
"""
import os
import time
import tempfile
import numpy as np
import pygame
import sounddevice as sd
import scipy.io.wavfile
import whisper
from openai import OpenAI
from elevenlabs import ElevenLabs, save
from config import Config

class AIVoiceAssistant:
    """Main AI Voice Assistant class"""
    
    def __init__(self):
        """Initialize the voice assistant"""
        # Validate configuration
        Config.validate()
        
        # Initialize clients
        self.openai_client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.elevenlabs_client = ElevenLabs(api_key=Config.ELEVENLABS_API_KEY)
        
        # Initialize audio components
        pygame.mixer.init()
        self.whisper_model = whisper.load_model(Config.WHISPER_MODEL)
        
        print("🎤 AI Voice Assistant initialized successfully!")
    
    def ask_openai(self, prompt):
        """Send prompt to OpenAI and get response"""
        try:
            response = self.openai_client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=Config.OPENAI_MAX_TOKENS,
                temperature=Config.OPENAI_TEMPERATURE
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"❌ Error with OpenAI API: {e}")
            return "I'm sorry, I encountered an error processing your request."
    
    def speak(self, text):
        """Convert text to speech using ElevenLabs"""
        try:
            audio = self.elevenlabs_client.text_to_speech.convert(
                text=text,
                voice_id=Config.ELEVENLABS_VOICE_ID,
                model_id=Config.ELEVENLABS_MODEL
            )
            
            # Create temporary file and play audio
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
                save(audio, temp_file.name)
                pygame.mixer.music.load(temp_file.name)
                pygame.mixer.music.play()
                
                # Wait for audio to finish
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                
                # Clean up temporary file
                os.unlink(temp_file.name)
                
        except Exception as e:
            print(f"❌ Error with ElevenLabs TTS: {e}")
    
    def record_audio(self):
        """Record audio using Enter to start/stop"""
        print("🎤 Press Enter to start recording...")
        input()
        
        print("🎙️  Recording... Press Enter again to stop.")
        
        # Start recording
        recording = []
        stream = sd.InputStream(
            samplerate=Config.SAMPLE_RATE, 
            channels=Config.CHANNELS, 
            dtype='int16'
        )
        stream.start()
        
        # Recording loop
        try:
            while True:
                data, _ = stream.read(Config.CHUNK_SIZE)
                recording.append(data)
                
                # Check if Enter was pressed (every ~6 seconds)
                if len(recording) % 100 == 0:
                    print("   Still recording... Press Enter to stop")
                    input()
                    break
        except KeyboardInterrupt:
            pass
        
        stream.stop()
        stream.close()
        
        # Convert to numpy array
        audio = np.concatenate(recording, axis=0)
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            scipy.io.wavfile.write(f.name, Config.SAMPLE_RATE, audio)
            audio_path = f.name
        
        print("⏹️  Recording stopped, transcribing...")
        
        # Transcribe with Whisper
        result = self.whisper_model.transcribe(audio_path)
        os.unlink(audio_path)  # Clean up temp file
        
        text = result["text"].strip()
        print(f"🎯 You said: {text}")
        return text if text else None
    
    def run(self):
        """Main assistant loop"""
        print("🎤 Welcome to your AI Voice Assistant!")
        print("💬 Press Enter to start talking, Enter again to stop.")
        print("🔊 AI responses will be spoken using your cloned voice.")
        print("❌ Press Ctrl+C to exit.\n")
        
        while True:
            try:
                # Record user input
                user_input = self.record_audio()
                
                if not user_input:
                    print("❌ No speech detected. Try again.")
                    continue
                
                # Check for exit commands
                if any(word in user_input.lower() for word in ["goodbye", "exit", "quit", "bye"]):
                    print("👋 Goodbye!")
                    self.speak("Goodbye!")
                    break
                
                # Get AI response
                print("🤔 Thinking...")
                ai_response = self.ask_openai(user_input)
                print(f"🤖 AI: {ai_response}")
                self.speak(ai_response)
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                continue

def main():
    """Main entry point"""
    try:
        assistant = AIVoiceAssistant()
        assistant.run()
    except Exception as e:
        print(f"❌ Failed to initialize assistant: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
