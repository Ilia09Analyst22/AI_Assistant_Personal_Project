"""Logging module for AI speech function."""

# Required libraries
from logging import Logger

def speech_logging(speech_func: function) -> None:
    """A logging method for AI speech testcase.
    
    Args:
        speech_func: The speak function to be used for testing.
    """
    log = Logger("AI speech logging")
    if speech_func:
        Logger.info("Test successful: AI assistant spoke without any issues")
        Logger.setLevel(log, "SUCCESS")
    else:
        Logger.error("Just to let you know, the AI speech failed.")
        Logger.fatal("AI speak function failed!!")
        Logger.setLevel(log, "FAIL")
        print("The logs suggest a failure in the speech functionality of the " \
        "AI assistant. This suggests a possible software issue, or perhaps an error in your" \
        "code. Please make sure all required libraries are accessible.")

def chat_logging(chat_func: function) -> None:
    """A logging method for AI speech chatbox function.
    
    Args:
        chat_func: The chatbox function from ai_speech.
    """
    log = Logger("AI chat logging")
    if chat_func:
        Logger.info("Test successful: AI assistant chat function worked without any issues")
        Logger.setLevel(log, "SUCCESS")
    else:
        Logger.error("Just to let you know, the AI chatbox failed!")
        Logger.fatal("AI chatbox function failed!")
        Logger.setLevel(log, "FAIL")
        print("The logs suggest that the AI chat test failed. Look at the log messages to find " \
        "the cause of the failure. It could be one of the following: The AI voice failed to setup " \
        "properly, The web browser failed to interact with ChatGPT, or an element on the ChatGPT " \
        "webpage was not found.")

def voice_interact_logging(voice_func: function) -> None:
    """A logging method for AI voice interaction testcase.
    
    Args:
        voice_func: The voice interact function for testing.
    """
    log = Logger("AI voice interact logging")
    if voice_func:
        Logger.info("Successful voice interaction with AI assistant")
        Logger.setLevel(log, "SUCCESS")
    else:
        Logger.error("Just to let you know, the AI interactive voice agent failed")
        Logger.fatal("Voice interaction with AI assistant failed!!")
        Logger.setLevel(log, "FAIL")
        print("The testcase failed due to an issue with ChatGPT interaction and " \
        "selenium web browsing functionality. Please check to make sure you have entered a valid " \
        "voice ID and that you have internet access.")

def text_interact_logging(text_func: function) -> None:
    """A logging method for AI interactive text agent.
    
    Args:
        voice_func: The text interact function from ai_speech.
    """
    log = Logger("AI text interact logging")
    if text_func:
        Logger.info("Successful text interaction with AI assistant")
        Logger.setLevel(log, "SUCCESS")
    else:
        Logger.error("Just to let you know, the AI interactive text agent failed")
        Logger.fatal("Text interaction with AI assistant failed!!")
        Logger.setLevel(log, "FAIL")
        print("The test failed due to an issue with selenium web browsing functionality. Please " \
        "make sure you have a stable internet connection, or check for any invalid locator values " \
        "or selector methods in the function.")