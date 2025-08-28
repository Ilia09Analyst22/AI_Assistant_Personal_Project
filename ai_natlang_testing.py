"""Module for testing ai_natlang functions."""

# Libraries needed
from unittest.case import TestCase
from ai_natlang import check_with_greeting, pos, chunk, nl_processor
from nltk import pos_tag
import re
import sklearn as sl

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
        """Test POS feature of AI NatLang."""
        return self.assertAlmostEqual(pos(self.generic_greet),[('Hello', 'NNP'), ('.', '.'), ('How', 'WRB'), ('can', 'MD'), ('I', 'PRP'), ('help', 'VB'), ('you', 'PRP'), ('?', '?')])
    
    def test_basic_chunk(self):
        """Test chunking with generic text."""
        some_text = "A great successful man"
        return self.assertRegex(some_text, "NP: {<DT>?<JJ>*<NN>}")
    
    def test_natlang_chunk(self):
        """Test chunk feature of AI NatLang."""
        import nltk.tree.tree as tr
        pattern = "NP: {<DT>?<JJ>*<NN>}"
        return self.assertIsInstance(chunk(pos("A great successful man"),pattern), tr.Tree)
    
    def test_nl_process(self):
        """Test Natural Language Processing."""
        gg = self.generic_greet
        return self.assertEqual(nl_processor(gg), ["Hello",",","how","may","I","help","you","?"])
    

        