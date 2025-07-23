from model.naiveBayesModel import NaiveBayesModel
from model.loader import DatasetLoader
from model.naiveBayesClassifier import NaiveBayesClassifier
from model.dataCleaner import DataCleaner

class AppController:
    def __init__(self):
        self.loader = DatasetLoader()
        self.cleaner = DataCleaner()
        self.model = NaiveBayesModel()
        self.classifier = None

    def run(self):
        train_df = self.loader.load("DB.csv")
        train_df = self.cleaner.clean(train_df)
        self.model.fit(train_df)
        self.classifier = NaiveBayesClassifier(self.model)
