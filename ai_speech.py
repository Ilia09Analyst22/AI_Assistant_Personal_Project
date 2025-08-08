"""Test module for AI speech function"""

# Required Libraries
import pyttsx3
import speech_recognition as sr

def speak() -> bool:
    """Allows AI assistant to speak.
    
    Returns:
        Boolean value indicating wether speach was successful.
    """
    try:
        # Initialize voice engine
        engine = pyttsx3.init()
    except Exception as err:
        pass

    try:
        # Set the voice of the AI assistant
        engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    except Exception as err:
        pass

    try:
        # Tell the assistant to speak
        engine.say("Hello, how can I help you?")

        # Run the interactive assistant
        engine.runAndWait()
    except Exception:
        pass


