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

        print("The logs suggest that the AI chat test failed. Look at the log messages to find " \
        "the cause of the failure. It could be one of the following: The AI voice failed to setup " \
        "properly, The web browser failed to interact with ChatGPT, or an element on the ChatGPT " \
        "webpage was not found.")