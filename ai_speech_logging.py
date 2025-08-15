"""Logging module for AI speech function."""

# Required libraries
from logging import Logger


def speech_logging(test_result):
    """Decorator for AI speech testcase."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            log = Logger("AI speech logging")
            result = func(*args, **kwargs)
            if test_result:
                Logger.info(log, "Test successful: AI assistant spoke without any issues")
                Logger.setLevel(log, "SUCCESS")
            else:
                Logger.error(log, "Just to let you know, the AI speech failed.")
                Logger.fatal(log, "AI speak function failed!!")
                Logger.setLevel(log, "FAIL")
                print("The logs suggest a failure in the speech functionality of the "
                      "AI assistant. This suggests a possible software issue, or perhaps an error in your "
                      "code. Please make sure all required libraries are accessible.")
            return result
        return wrapper
    return decorator


def chat_logging(test_result):
    """Decorator for AI speech chatbox function."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            log = Logger("AI chat logging")
            result = func(*args, **kwargs)
            if test_result:
                Logger.info(log, "Test successful: AI assistant chat function worked without any issues")
                Logger.setLevel(log, "SUCCESS")
            else:
                Logger.error(log, "Just to let you know, the AI chatbox failed!")
                Logger.fatal(log, "AI chatbox function failed!")
                Logger.setLevel(log, "FAIL")
                print("The logs suggest that the AI chat test failed. Look at the log messages to find "
                      "the cause of the failure. It could be one of the following: The AI voice failed to setup "
                      "properly, The web browser failed to interact with ChatGPT, or an element on the ChatGPT "
                      "webpage was not found.")
            return result
        return wrapper
    return decorator


def voice_interact_logging(test_result):
    """Decorator for AI voice interaction testcase."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            log = Logger("AI voice interact logging")
            result = func(*args, **kwargs)
            if test_result:
                Logger.info(log, "Successful voice interaction with AI assistant")
                Logger.setLevel(log, "SUCCESS")
            else:
                Logger.error(log, "Just to let you know, the AI interactive voice agent failed")
                Logger.fatal(log, "Voice interaction with AI assistant failed!!")
                Logger.setLevel(log, "FAIL")
                print("The testcase failed due to an issue with ChatGPT interaction and "
                      "selenium web browsing functionality. Please check to make sure you have entered a valid "
                      "voice ID and that you have internet access.")
            return result
        return wrapper
    return decorator


def text_interact_logging(test_result):
    """Decorator for AI interactive text agent."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            log = Logger("AI text interact logging")
            result = func(*args, **kwargs)
            if test_result:
                Logger.info(log, "Successful text interaction with AI assistant")
                Logger.setLevel(log, "SUCCESS")
            else:
                Logger.error(log, "Just to let you know, the AI interactive text agent failed")
                Logger.fatal(log, "Text interaction with AI assistant failed!!")
                Logger.setLevel(log, "FAIL")
                print("The test failed due to an issue with selenium web browsing functionality. Please "
                      "make sure you have a stable internet connection, or check for any invalid locator values "
                      "or selector methods in the function.")
            return result
        return wrapper
    return decorator