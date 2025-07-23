import pandas as pd
from model.naiveBayesModel import NaiveBayesModel

class NaiveBayesClassifier:
    def __init__(self, model: NaiveBayesModel):
        self.model = model

    def predict(self, record: dict):
        results = {}
        for cls in self.model.prior_probs:
            prob = self.model.prior_probs[cls]
            for feature, value in record.items():
                cond_prob = self.model.cond_probs[cls].get(feature, {}).get(value, 1e-6)
                prob *= cond_prob
            results[cls] = prob
        return max(results, key = results.get)

    def evaluate(self, df: pd.DataFrame):
        correct = 0
        total = df.shape[0]
        for _, row in df.iterrows():
            record = row.to_dict()
            actual = record.pop(self.model.target)
            predicted = self.predict(record)
            if predicted == actual:
                correct += 1
        accuracy = round((correct / total) * 100, 2)
        return accuracy