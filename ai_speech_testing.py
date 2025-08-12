"""Module for testing AI speech related functions."""

# Required Libraries
from unittest.case import TestCase
from ai_speech import speak, chatbox, voice_interact, text_interact

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
        self.assertTrue(chatbox())

