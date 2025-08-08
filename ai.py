"""Interactive audio and text AI assistant"""

# Required Libraries
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import webbrowser
import datetime
import wikipedia
import regex
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, RegexpParser
import random
import selenium.webdriver as driver

class AIProcessor:
    """Abstract class for processing natural language.
    
    Attributes:
        open_ai: Determines wether to use chat GPT.
        ml: Machine learning method to use for deep learning.
        assist: If True, use AI assistant.
    """
    def __init__(self, chat: bool = True, ml: str|None = None, assist: bool = True):
        """Initial instance of AI processor."""
        self.open_ai = chat
        self.model = ml
        self.assist = assist
    
    def nl_processor(self, text: str) -> list[list[str]]:
        """ Method for natural language processing.
        
        Args:
            text: The message to tokenize.
        
        Returns:
            A fully processed list of tokens. For example:
            [["Hello", "assistant", ".",], ["What", "time", "is", "it", "?"]]
        """
        sentences = []
        processed = []

        sentences = sent_tokenize(text)
        for line in sentences:
            line = word_tokenize(line)
            processed.append(line)
        return processed
    
    def part_of_speech(self, sentence: str):
        """Assign part of speech to each word in a sentence.
        
        Args:
            sentence: The sentence to assign POS tagging to.
        
        Returns:
            A list of tuples tagging the part of speech for each word.
        """
        return pos_tag(sentence)
    
    def chunk(self, words_tagged: list[tuple[str,str]], pattern: str):
        """Method for identifying phrases in a sentence.
        
        Args:
            words_tagged: A tokenized list of words tagged with POS.
            pattern: Regex pattern to search for phrase.
        
        Returns:
            A tree object displaying the chunked output.
        """
        chunk_parser = RegexpParser(pattern)
        word_tree = chunk_parser.parse(words_tagged)
        return word_tree
    
    def count_occur(self, words: list[str]) -> list[tuple[str,str]]:
        """Method to count number of occurences of different words.
        
        :param words: The words to count.
        :returns A list of tuples for word and number of occurrences.
        """
        word_counter = []
        for word in words:
            word_counter.append((word, words.count(word)))
        return word_counter
    
    def sentiment(self, words_tagged: list[tuple[str,str]], structure: str = "dt,adj-1,noun") -> list[str]:
        """Sentiment analysis based on a given sentence structure.
        
        Args:
            worrds_tagged: A tokenized list of words tagged with POS.
            structure: Sentence structure to follow for sentiment check. By
              default, sentence starts with an article followed by adjectives and
              finishing with a noun.
        
        Returns:
            A list of two elements:
                - The noun being described
                - The most popular sentiment for that noun
        """
        pos_ref = {"adj": "ADJECTIVE", "dt": "ARTICLE", "noun": "NOUN", "adv": "ADVERB", 
                   "pn": "PRONOUN", "vb": "VERB"}
        
        refs = structure.split(",")
        words = []
        noun = ""
        for ref in refs:
            assert ref.replace(r"-%d", "") in pos_ref
        for word in words_tagged:
            if word[1] == "DT":
                words_tagged.remove(word)
            elif word[1] == "NN":
                noun = word[0]
                words_tagged.remove(word)
            else:
                words.append(word[0])

        sent_list = self.count_occur(words)
        
        current_max = 0
        sentiment = ""
        for adj in sent_list:
            reported_max = adj[1]
            if reported_max > current_max:
                current_max = reported_max
                sentiment = adj[0]
            else:
                continue
        
        return [noun, sentiment]

class AIAssistant(AIProcessor):
    """Simple AI Assistant.
    
    Attributes:
        lang: The language for the voice assistant. For example,
          if you want American english, set to 'en-us' or if you want
          British english, set to 'en-gb'.
        gender: The gender for the voice assistant. If you want a
          male voice, set to 'male' or if you want a female voice, set
          to 'female'.
    """

    def __init__(self, lang: str, gender: str):
        """Set the language and gender of the AI voice assistant."""
        self.language = lang
        self.gender = gender
        self.voices = {("en-us","male"):
        "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
        ("en-us","female"): "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
        ("en-gb","female"): "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0",
        ("es-es","female"): "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0",
        ("es-mx","female"): "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0",
        }
    
    def get_voices(self) -> None:
        """Prints all available voices for AI assistant."""
        engine = pyttsx3.init()
        for voice in engine.getProperty('voices'):
            print(voice)
    
    def select_voice(self) -> str:
        """This method returns a voice id given language and gender."""
        voice_id = ""
        if (self.language, self.gender) in self.voices:
            voice_id = self.voices[(self.language, self.gender)]
        return voice_id
    
    def language_mapper(self) -> dict[str:[str,str]]:
        """Method to store language data.
        
        Returns:
            A dictionary mapping a language with the voice
              gender and id. Example: {'en-us':['male','id1'],
              'en-gb':['female','id2']}.
        """
        pass

    def transform_audio_to_text(self) -> str:
        """Method for AI to turn audio into text.
        
        Returns:
            A string representing the text version of audio
              input or a message informing user that the
              assistant is still waiting to receive valid input.
        """
        # Store voice recognizer for AI assistant
        r = sr.Recognizer()

        # Set microphone and start listening
        with sr.Microphone() as mp:
            
            # wait
            r.pause_threshold(0.8)

            # message telling user that recording starts
            print("Start speaking")

            # AI listens to the user speak
            audio = r.listen(mp)

            # Test speach recognition functionality
            try:
                response = r.recognize_bing(audio)
                print(response)
            except sr.UnknownValueError:
                print("Sorry, I did not recognize the audio.")
                response = "I am still waiting"
            except sr.RequestError:
                print("Sorry, an error has occurred.")
                response = "I am still waiting"
        
        return response
    
    def speak(self, message) -> None:
        """A method to allow AI assistant to speak.
        
        Args:
            message: What the AI assistant will say.
        """
        engine = pyttsx3.init()
        engine.setProperty('voice', self.select_voice())

        # Deliver speach
        engine.say(message)
        engine.runAndWait()

    def transform_text_to_audio(self) -> None:
        """Method for AI to turn text into audio."""
        # Prompt for user to input text to be transformed
        text = input("Please enter some text: ")

        # Transform text to audio
        self.speak(text)

    
    def assistant(self, voice: bool = True, set_basic: bool = False) -> None:
        """Main method to activate AI assistant.
        
        Args:
            voice: Boolean value indicating wether or not to
              activate audio mode. If set to False, the assistant will
              only interact with the user through text and the user can
              not give audio input. Set to True by default.
            set_basic: Boolean value which determines the processing
              capabilities of the AI assistant. If set to True, the 
              assistant will only be able to perform basic tasks such as
              opening a web browser or transforming audio into text. Set to
              False by default.
        """
        request = ""
        if not voice and (self.language == "en-us" or self.language == "en-gb"):
            print("Welcome to the AI assistant! Please enter input in all lowercase.")
            print("How can I help you today?")
            request = input("Tell me what's on your mind: ")

            if "search the internet for " in request.lower():
                print("Of course! Right away")
                user_request = request.replace("search the internet for ", "")
                reply = pywhatkit.search(user_request)
                print(f"This is what I found: {reply}")
            if "do a wikipedia search for " in request.lower():
                print("Searching wikipedia..")
                user_request = request.replace("do a wikipedia search for ", "")
                reply = wikipedia.summary(user_request, sentences=1)
                print(f"According to wikipedia: {reply}")
            if "open youtube" in request.lower():
                print("Sure, I'm on it")
                webbrowser.open_new_tab("https://www.youtube.com/")
            if "open google" in request.lower():
                print("Sure, I'm on it")
                webbrowser.open_new_tab("https://www.google.com/")
            if not set_basic:
                tokens = self.nl_processor(request)
                toks_with_tags = []
                for sent in tokens:
                    if "?" in sent:
                        quest_remarks = ["Great question", "Interesting question", "Facinating!", "Glad you asked!"]
                        remark = random.choice(quest_remarks)
                        print(remark)
                        pywhatkit.search(request)
                    elif "ChatGPT".lower() in sent and self.open_ai:
                        from selenium.webdriver.common.by import By
                        from selenium.webdriver.common.keys import Keys
                        from selenium.webdriver.support.ui import WebDriverWait
                        from selenium.webdriver.support import expected_conditions as EC

                        browser = driver.Chrome()
                        browser.get("https://chatgpt.com/")
                        request = request.strip().split("and")
                        user_request = request[1:]

                        browser.find_element(By.XPATH, "//*[@id='prompt-textarea']/p").send_keys(user_request + Keys.ENTER)

                    tagged_token = self.part_of_speech(sent)
                    toks_with_tags.append(tagged_token)
                    regex_rule = "NP: {<DT>?<JJ>*<NN>}"
                    expression = regex.match(regex_rule, " ".join(sent))

                    print(self.chunk(tagged_token, expression))

                    noun_sentiment = self.sentiment(tagged_token)
                    print(f"Filtering results for {noun_sentiment[0]} {noun_sentiment[1]}")
                    
                    for word in request:
                        if word == noun_sentiment[0]:
                            request.replace(word, f"{word}")
                        if word == noun_sentiment[1]:
                            request.replace(word, f"{word}")
                    
                    reply = pywhatkit.search(request)
                    print(f"This is what I found: {reply}")
        
        elif voice and (self.language == "en-us" or self.language == "en-gb"):
            self.speak("How can I help you today?")
            request = self.transform_audio_to_text()
            
            if "search the internet for" in request:
                user_request = request.replace("search the internet for", "")
                reply = pywhatkit.search(user_request)
                self.speak("This is what I found: ")
                self.speak(reply)
            if "do a wikipedia search for" in request:
                user_request = request.replace("do a wikipedia search for", "")
                reply = wikipedia.summary(user_request, sentences=1)
                self.speak("According to wikipedia: ")
                self.speak(reply)
            if "open youtube" in request:
                self.speak("sure, I'm on it")
                webbrowser.open_new_tab("https://www.youtube.com/")
            if "open google" in request:
                self.speak("sure, I'm on it")
                webbrowser.open_new_tab("https://www.google.com/")
            if not set_basic:
                tokens = self.nl_processor(request)
                toks_with_tags = []
                for sent in tokens:
                    if "?" in sent:
                        quest_remarks = ["Great question", "Interesting question", "Facinating!", "Glad you asked!"]
                        remark = random.choice(quest_remarks)
                        self.speak(remark)
                        pywhatkit.search(request)
                    elif "ChatGPT".lower() in sent and self.open_ai:
                        from selenium.webdriver.common.by import By
                        from selenium.webdriver.common.keys import Keys
                        from selenium.webdriver.support.ui import WebDriverWait
                        from selenium.webdriver.support import expected_conditions as EC

                        browser = driver.Chrome()
                        browser.get("https://chatgpt.com/")
                        request = request.strip().split("and")
                        user_request = request[1:]

                        browser.find_element(By.XPATH, "//*[@id='prompt-textarea']/p").send_keys(user_request + Keys.ENTER)

                    tagged_token = self.part_of_speech(sent)
                    toks_with_tags.append(tagged_token)
                    regex_rule = "NP: {<DT>?<JJ>*<NN>}"
                    expression = regex.match(regex_rule, " ".join(sent))

                    print(self.chunk(tagged_token, expression))

                    noun_sentiment = self.sentiment(tagged_token)
                    print(f"Filtering results for {noun_sentiment[0]} {noun_sentiment[1]}")
                    
                    for word in request:
                        if word == noun_sentiment[0]:
                            request.replace(word, f"{word}")
                        if word == noun_sentiment[1]:
                            request.replace(word, f"{word}")
                    
                    reply = pywhatkit.search(request)
                    self.speak(f"This is what I found: {reply}")

my_assistant = AIAssistant("en-us","male")
my_assistant.get_voices()