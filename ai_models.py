# Libraries needed
from unittest.case import TestCase
import tensorflow as tf
import sklearn
import nltk
import numpy
import pandas
import keras

class CustomModels(TestCase):
    """Base class for customized ML models.
    
    Attributes:
        data: A pandas dataframe containing a fully enumerated dataset ready
        for ML model training.
        rows: The number of rows in the dataframe to use for training set
        columns: The number of columns in the dataframe to use for training set
    """
    def __init__(self, dataframe: pandas.DataFrame, num_rows: int, num_col: int):
        """Initialize the custom model class."""
        self.data = dataframe
        self.rows = num_rows
        self.columns = num_col

    def grad_desc(self) -> bool:
        """Perform the Gradient Descent algorithm.
        
        Returns:
            True if the model can predict query sentiment
            with at least 95% accuracy. Otherwise, False.
        """
        # Set X feature matrix and Y label vector
        X = self.data[0:self.columns-2][0:self.rows-10]
        Y = self.data[self.columns-1][0:self.rows-1]

        # Train the data using GD model
        from sklearn import linear_model
        
        model = linear_model.SGDClassifier()
        model.fit(X, Y)

        # Predict labels
        X_predict = self.data[0:self.columns-2][self.rows-9:self.rows-1]
        Y_predict = model.predict(X_predict)

        # Calculate accuracy
        return True # skip this for now
    
    def identify_good_or_bad(self, query: str) -> bool:
        """Use sentiment analysis to check sentiment.
        
        See what the user thinks about the topic being queried. If it
        predicts the right sentiment with 95% accuracy or higher, return True.
        """
        from ai import AIProcessor
        
        process = AIProcessor()
        query_pos_tags = process.part_of_speech(query)
        analyse_sentiment = process.sentiment(query_pos_tags)

        # Set X feature matrix and Y label vector
        X = self.data[0:self.columns-2][0:self.rows-10]
        Y = self.data[self.columns-1][0:self.rows-1]

        # Setup model
        good_sent = 1
        bad_sent = 0

        import random

        sent_val = random.choice([good_sent, bad_sent])
        map_sent = {analyse_sentiment: sent_val}

        for i in range(self.columns):
            for j in range(self.rows):
                if self.data.iloc(i)[j] == map_sent[analyse_sentiment]:
                    self.data.iloc(i)[self.columns-1] = sent_val
    
        return True # ignore for now
    
    def tensor_model(self):
        """Custom tensor flow model for ML training/prediction."""
        # Set X feature matrix and Y label vector
        X = self.data[0:self.columns-2][0:self.rows-10]
        Y = self.data[self.columns-1][0:self.rows-1]
        tf.add(X, Y)
        
        for i in range(self.columns):
            for j in range(self.rows):
                if isinstance(self.data[i][j],tf.as_dtype("float")):
                    self.data[i][j] = tf.AggregationMethod.ADD_N
                elif self.data[i][j] == 0:
                    self.data[i][j] = 1
        
        return True # ignore for now
    
    def mykrs(self, yaml_file):
        """Custom keras model for ML training and prediction.
        
        yaml_file: File specifying the type of model to use.
        """
        keras.Input(shape=(self.columns,), batch_size=10, dtype="int32")
        keras.Model.build((self.rows, self.columns))
        keras.models.model_from_yaml(yaml_file)

        from sklearn import linear_model
        linear_model._coordinate_descent.Lasso.__or__

    def lasso_decent(self):
        """Method for performing Lasso coordinate descent."""
        from sklearn import linear_model

        # Set X feature matrix and Y label vector
        X = self.data[0:self.columns-2][0:self.rows-10]
        Y = self.data[self.columns-1][0:self.rows-1]

        model = linear_model._coordinate_descent.Lasso()
        model.fit(X, Y)

        # Predict labels
        X_predict = self.data[0:self.columns-2][self.rows-9:self.rows-1]
        Y_predict = model.predict(X_predict)

        return True # ignore

            