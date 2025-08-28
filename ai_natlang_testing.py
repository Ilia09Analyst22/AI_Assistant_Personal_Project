"""Module for testing ai_natlang functions."""

# Libraries needed
from unittest.case import TestCase
from ai_natlang import check_with_greeting, pos, chunk, nl_processor, words, sentences
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
    
    def regex(self):
        """Test Regex and sentence tokenization."""
        import random

        greeting = random.choice(["Hello. How can I help you?", self.generic_greet])
        sent_list = sentences(greeting)

        # Set four check conditions for passing test
        check1 = False
        check2 = False
        check3 = False
        check4 = False

        def re_search(lookup: str, text: str) -> bool:
            """A method to lookup a phrase/pattern in text.
            
            Args:
                lookup: Phrase/pattern to search for in text.
                text: The text to search in.
            
            Returns:
                True if the lookup is found inside text, False otherwise.
            """
            find_match = re.search(lookup, text)
            if not find_match:
                return False
            else:
                return True
            
        for sent in sent_list:
            if not check1:
                check1 = re_search(lookup="Hello.", text=sent)
            
            if not check2 and re.search("How", sent, re.IGNORECASE):
                pos = pos_tag("How")
                tag = pos[1]
                if tag == "WRB":
                    check2 = True
        
            if not check3:
                check3 = re_search(lookup="I help", text=sent)
            
            if not check4 and "?" in sent:
                check4 = re_search(lookup="you", text=sent)
        
        assert (check1 and check2 and check3 and check4)
    
        return True