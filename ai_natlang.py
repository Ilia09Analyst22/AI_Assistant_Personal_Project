"""Module for testing AI Natural Language Features."""

# Libraries Needed
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag, RegexpParser
from nltk.help import upenn_tagset as see_postags
from nltk import download as load

load("punkt")
load("averaged_perceptron_tagger")
load("tagsets")

def sentences(text: str) -> list[str]:
    """Takes some text and breaks it into a list of sentences."""
    return sent_tokenize(text)

def words(text: str) -> list[str]:
    """Takes some text and breaks it into a list of words."""
    return word_tokenize(text)

def check_with_greeting(method: str) -> bool:
    """Uses generic greeting message to test words and sentences.
        Specify method as words or sentences for the test.
    """
    tokenize = []
    greet = "Hello. How can I help you?"

    if method.lower() == "sentences":
        if sentences(greet) == ["Hello.", "How can I help you?"]:
            return True
        else:
            return False
    if method.lower() == "words":
        if words(greet) == ["Hello",".","How","can","I","help","you","?"]:
            return True
        else:
            return False
    return False

def pos(text: str) -> list[tuple[str,str]]:
    """Returns a list of tuples indicating the POS for each word in a text."""
    return pos_tag(words(text))

def chunk(words_tagged: list[tuple[str,str]], pattern: str):
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

def nl_processor(text: str) -> list[list[str]]:
    """ Method for natural language processing.
        
    Args:
        text: The message to tokenize.
        
    Returns:
        A fully processed list of tokens. For example:
          [["Hello", "assistant", "."], ["What", "time", "is", "it", "?"]]
    """
    processed = []

    sent_list = sentences(text)
    for line in sent_list:
        line = words(line)
        processed.append(line)
    return processed

def get_pos_tags():
    """See all of the available tags for POS."""
    return see_postags()

#print(pos("Hello. How can I help you?"))
print(get_pos_tags())