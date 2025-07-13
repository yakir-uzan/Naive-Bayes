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
        self.model.print_model()
        self.classifier = NaiveBayesClassifier(self.model)

        print("\nטוען קובץ בדיקה...")
        test_df = self.loader.load("DB.csv")
        accuracy = self.classifier.evaluate(test_df)
        print(f"\nדיוק המודל: {accuracy}%")

        while True:
            print("\nהכנס רשומה חדשה (בפורמט: key1=value1,key2=value2,...) או 'exit':")
            user_input = input().strip()
            if user_input.lower() == 'exit':
                break
            try:
                record = dict(item.split('=') for item in user_input.split(','))
                prediction = self.classifier.predict(record)
                print(f"תחזית: {prediction}")
            except:
                print("קלט שגוי, נסה שוב.")