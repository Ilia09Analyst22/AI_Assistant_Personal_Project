"""Module for testing AI speech related functions."""

# Required Libraries
from unittest.case import TestCase
from ai_speech import speak, chatbox, voice_interact, text_interact
import random

class TestAISpeech(TestCase):
    """Testbase for testing AI speech functions."""

    def test_speak(self) -> bool:
        """Testing the speak functionality of AI assistant.
        
        Returns:
            True if AI voice can be heard, False otherwise.
        """
        self.assertTrue(speak())
    
    def test_chatbox(self) -> bool:
        """Testing the chatbox function of AI assistant.
        
        Returns:
            Boolean value indicating successful execution of chatbox function.
        """
        audio_or_text = random.choice(["audio", "text"])
        self.assertTrue(chatbox(audio_or_text))

    def test_voice_interact(self) -> bool:
        """Testing the interactive voice function of AI assistant.
        
        Returns:
            True if voice interactive function runs successfully, False otherwise.
        """
        num_reqs = random.choice(range(10))
        voices = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
                  "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
                  "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0",
                  "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0",
                  "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"]
        voice_id = random.choice(voices)
        self.assertTrue(voice_interact(voice_id, num_reqs))

    def test_text_interact(self) -> bool:
        """Testing the interactive test function of AI assistant.
        
        Returns:
            Boolean value indicating success of interactive text functionality.
        """
        num_reqs = random.choice(range(10))
        self.assertTrue(text_interact(num_reqs))

if __name__ == "__main__":
    import unittest
    unittest.main()
