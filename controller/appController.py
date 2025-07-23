from model.naiveBayesModel import NaiveBayesModel
from model.loader import DatasetLoader
from model.naiveBayesClassifier import NaiveBayesClassifier
from model.dataCleaner import DataCleaner

class AppController:
    def __init__(self, data_path):
        self.data_path = data_path
        self.loader = DatasetLoader()
        self.cleaner = DataCleaner()
        self.model = NaiveBayesModel()
        self.classifier = None

    def run(self):
        df = self.loader.load(str(self.data_path))
        df = self.cleaner.clean(df)
        self.model.fit(df)
        self.classifier = NaiveBayesClassifier(self.model)
