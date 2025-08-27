"""Module for testing ai_natlang functions."""

# Libraries needed
from unittest.case import TestCase
from ai_natlang import check_with_greeting, pos, chunk, nl_processor

class TestAINatLang(TestCase):
    """Method for testing AI NatLang features."""

    generic_greet = "Hello, how may I help you?"
    def test_words_or_sentences(self, word_sent: str) -> bool:
        """Test word or sentence tokenization on generic greeting.
        
        Args:
            word_sent: User's choice of word or sentence tokenization.
              Specify words or sentences.
        
        Returns:
            True if word or sentence tokenization was successful, False otherwise.
        """
        return self.assertTrue(check_with_greeting(word_sent))
    
    def test_pos(self):
        return
    
    def test_chunk(self):
        return
    
    def test_nl_process(self):
        gg = self.generic_greet
        return self.assertEqual(nl_processor(gg), ["Hello",",","how","may","I","help","you","?"])