"""Module for testing ai_natlang functions."""

# Libraries needed
from unittest.case import TestCase
from ai_natlang import check_with_greeting, pos, chunk, nl_processor, words, sentences
from nltk import pos_tag
import re
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as pl

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
    
    def linear_model(self, model: str):
        """Linear Model Based On a Chosen Machine Learning Method.
        
        Trains a set of data from ai_text.txt and returns True if the model
        succeeds with a probabilty greater than 95%.

        Args:
            model: The machine learning model to train the data.
        """
        import pandas as pd
        import csv

        data = open("ai_text.txt", "r")
        self.model = model

        def create_csv():
            """Transform the text file into a csv file."""
            with open("ai_text.csv", "w") as csv_file:
                for line in data:
                    line = line.strip().split()
                    csv_file.write(line)
            return csv_file
        
        data_csv = create_csv()
        csv_file = csv.reader(data_csv)

        processed_data = pd.read_csv(csv_file)


        def model_sentiment():
            from random import randint

            word_dict = {}
            for line in processed_data:
                for word in line:
                    if word not in word_dict.keys():
                        word_dict[word] = randint(0, 1000000)
            
            with open("ai_text_enum.csv", "w") as text_enum:
                text_words = []
                for line in processed_data:
                    for i in range(len(line)):
                        text_words.append(word_dict[processed_data[i]])
                    text_enum.write(text_words)
                    text_words = []
            
            # Train/test data using enumerated text csv
            train_data_x = text_enum[0:8][0:15]
            test_data_x = text_enum[0:8][16:19]

            train_data_y = text_enum[9][0:15]
            test_data_y = text_enum[9][16:19]

            if self.model == "log_regr":
                model = linear_model.LogisticRegression()

                sample_nouns = ["Python", "Islam", "Xbox", "Men", "Paris", "Biology"]
                sample_sentiments = ["BAD", "BAD", "GOOD", "GOOD", "BAD", "GOOD"]

                noun_dict = {"Python": 2, "Islam": 7, "Xbox": 5, "Men": 6, "Paris": 1, "Biology": 8}
                sent_dict = {"GOOD": 1, "BAD": -1}

                x_data = []
                y_data = []

                for noun in sample_nouns:
                    x_data.append(noun_dict[noun])
                for sent in sample_sentiments:
                    y_data.append(sent_dict[sent])

                x = np.array(x_data).reshape(-1, 1)
                y = np.array(y_data)

                model.fit(X=x, y=y)
                sent_predict = model.predict(np.array([6]).reshape(-1, 1))
                print(f"The model predicted that women are {sent_predict}")

            if self.model == "stoch_grad_desc":
                model = linear_model.SGDClassifier()
                model.fit(X=train_data_x, y=train_data_y)
                sent_predict = model.predict(X=test_data_x)

            if self.model == "PassiveAggressive":
                model = linear_model.PassiveAggressiveClassifier()
                model.fit(X=train_data_x, y=train_data_y)
                sent_predict = model.predict(X=test_data_x)

            if self.model == "Poisson_Model":
                model = linear_model.PoissonRegressor()
                model.fit(X=train_data_x, y=train_data_y)
                sent_predict = model.predict(X=test_data_x)

            return [sent_predict, test_data_y]
        
        pl.scatter(x=processed_data[0], y=processed_data[9])
        pl.show()

        prediction = model_sentiment()[0]

        if prediction == model_sentiment()[1]:
            print("Exact match ('100%' accuracy)!")
        else:
            print(f"The model returned these predictions: {prediction}")
            print(f"These are the actual values from the dataset: {model_sentiment()[1]}")
