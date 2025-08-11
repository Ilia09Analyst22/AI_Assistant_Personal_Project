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
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

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
        Logger.info("Successful setup of AI speech engine")

        try:
            r = sr.Recognizer()
            with sr.Microphone() as mp:
                r.pause_threshold(0.8)
                print("Start speaking")
                audio = r.listen(mp)
        except Exception as err:
            Logger.error(f"Failed to recognize speech: {err}")
            return False
        Logger.info("Successful AI speech recognition")

        try:
            import time
            browser = driver.Edge()
            browser.get("https://chatgpt.com")
            time.sleep(2)
            browser.find_element(By.CLASS_NAME,"placeholder").send_keys(audio + Keys.ENTER)
        except Exception as err:
            Logger.error(f"Failed to enter data into ChatGPT: {err}")
            return False
        Logger.info("User request entered into CHATGPT successfully")

        try:
            time.sleep(10)
            response = browser.find_element(By.XPATH, "//*[@id='thread']/div/div[1]/div/div/div[2]/article[2]/div/div/div[2]/div/div/div/p[1]").text()
            pyttsx3.speak(response)
        except Exception:
            Logger.error("An error occurred. Likely the browser failed to locate ChatGPT reply!")
            response = WebDriverWait(browser, 20).until(EC.presence_of_element_located(response))
            pyttsx3.speak(response)
        Logger.info("Selenium web browsing operation successful")

    elif audio_text.lower() == "text":
        try:
            import time

            print("Hello, how can I help you?")
            text = input("Please enter some text: ")

            browser = driver.Edge()
            browser.get("https://chatgpt.com")
            time.sleep(2)
            browser.find_element(By.CLASS_NAME,"placeholder").send_keys(text + Keys.ENTER)
        except Exception:
            Logger.error(f"Failed to enter data into ChatGPT: {err}")
            return False
        Logger.info("Entered user request into CHATGPT")

        try:
            time.sleep(10)
            response = browser.find_element(By.XPATH, "//*[@id='thread']/div/div[1]/div/div/div[2]/article[2]/div/div/div[2]/div/div/div/p[1]").text()
            print(response)
        except (NoSuchElementException, ElementNotVisibleException):
            Logger.fatal("Failed to locate ChatGPT generated response")
            Logger.info("Retrying...")

            response = WebDriverWait(browser, 20).until(EC.presence_of_element_located(response))
            print(response)
        except Exception as err:
            Logger.error(f"An exception has occurred: {err}")
            return False
        Logger.info("Successfully retrieved response from ChatGPT")

    else:
        Logger.error("Invalid input")
        return False
    Logger.info("All operations were successfull!")
    return True

def voice_interact(voice_id: str | float, requests: int) -> bool:
    """Interactive AI voice agent.

    Args:
        voice_id: Voice ID for AI speech.
        requests: Number of requests before stopping the agent.
    """
    for request in range(requests):
        try:
            chatbox("audio")
        except Exception as err:
            Logger.error(f"Something went wrong: {err}")
            return False

