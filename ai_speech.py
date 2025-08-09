"""Test module for AI speech function"""

# Required Libraries
import pyttsx3
from logging import Logger
import speech_recognition as sr
from selenium import webdriver as driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def speak() -> bool:
    """Allows AI assistant to speak.
    
    Returns:
        Boolean value indicating wether speach was successful.
    """
    try:
        # Initialize voice engine
        engine = pyttsx3.init()
    except Exception as err:
        Logger.error(f"Failed to setup AI speech engine: {err}")
        return False
    Logger.info("AI speech setup successful")

    try:
        # Set the voice of the AI assistant
        engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    except Exception as err:
        Logger.error(f"Failed to set the voice for the AI assistant: {err}")
        return False
    Logger.info("AI voice was set successfully")

    try:
        # Tell the assistant to speak
        engine.say("Hello, how can I help you?")

        # Run the interactive assistant
        engine.runAndWait()
    except Exception:
        Logger.error("AI speak function failed during runtime")
        return False
    
    Logger.info("Successfully ran AI speech")
    return True

def chatbox(audio_text: str) -> bool:
    """Interacts with ChatGPT for user requests.
    
    User gives audio of text input to the AI assistant and the assistant 
      will search ChatGPT and reply to the user. The assistant begins by saying
      "Hello, how can I help you?". The user then provides an audio or text response
      for the assistant to enter into ChatGPT.

    Args:
        audio_text: A string value indicating either 'audio' or 'text'.
    
    Returns:
        A boolean value indicating wether the chatbox function was
          implemented successfully.
    """
    if audio_text.lower() == "audio":
        try:
            engine = pyttsx3.init()
            engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
            engine.say("Hello, how can I help you?")
            engine.runAndWait()
        except Exception:
            Logger.fatal("Failed to set up speech engine for AI assistant")
            return False
        
        try:
            r = sr.Recognizer()
            with sr.Microphone() as mp:
                r.pause_threshold(0.8)
                print("Start speaking")
                audio = r.listen(mp)
        except Exception as err:
            Logger.error(f"Failed to recognize speech: {err}")
            return False
        
    elif audio_text.lower() == "text":
        try:
            print("Hello, how can I help you")
            pass
        except Exception:
            return False
