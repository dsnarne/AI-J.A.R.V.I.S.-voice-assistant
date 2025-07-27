#!/usr/bin/env python3
"""
Configuration file for AI Voice Assistant
Centralized settings and API configuration
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Centralized configuration for the AI Voice Assistant"""
    
    #API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")
    
    #OpenAI Configuration
    OPENAI_MODEL = "gpt-4o"
    OPENAI_MAX_TOKENS = 200
    OPENAI_TEMPERATURE = 0.7
    
    #ElevenLabs Configuration
    ELEVENLABS_MODEL = "eleven_monolingual_v1"
    
    #Audio Recording Configuration
    SAMPLE_RATE = 16000
    CHANNELS = 1
    CHUNK_SIZE = 1024
    
    #Whisper Configuration
    WHISPER_MODEL = "base"
    
   
    @classmethod
    def validate(cls):
        """Validate that all required environment variables are set"""
        missing_keys = []
        
        if not cls.OPENAI_API_KEY:
            missing_keys.append("OPENAI_API_KEY")
        if not cls.ELEVENLABS_API_KEY:
            missing_keys.append("ELEVENLABS_API_KEY")
        if not cls.ELEVENLABS_VOICE_ID:
            missing_keys.append("ELEVENLABS_VOICE_ID")
            
        if missing_keys:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_keys)}")
        
        return True
