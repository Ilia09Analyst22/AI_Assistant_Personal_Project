"""Test module for AI speech function"""

# Required Libraries
import pyttsx3
from logging import Logger

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


