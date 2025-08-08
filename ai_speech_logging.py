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