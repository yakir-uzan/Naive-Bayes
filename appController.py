from naiveBayesModel import NaiveBayesModel
from loader import DatasetLoader
from naiveBayesClassifier import NaiveBayesClassifier

class AppController:
    def __init__(self):
        self.loader = DatasetLoader()
        self.model = NaiveBayesModel()
        self.classifier = None

    def run(self):
        train_df = self.loader.load("DB.csv")
        self.model.fit(train_df)
        self.classifier = NaiveBayesClassifier(self.model)
