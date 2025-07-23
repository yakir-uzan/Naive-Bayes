from controller.appController import AppController
from model.naiveBayesClassifier import NaiveBayesClassifier

def train_and_test(dataBase):
    db = dataBase
    app = AppController()
    df = app.loader.load(db)
    df = app.cleaner.clean(df)

    # ערבוב הדאטה
    df = df.sample(frac = 1, random_state = 42).reset_index(drop = True)

    # חלוקה ל-70% אימון ו-30% בדיקה
    split_index = int(len(df) * 0.7)
    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]

    # אימון המודל
    app.model.fit(train_df)
    app.classifier = NaiveBayesClassifier(app.model)

    # בדיקה
    accuracy = app.classifier.evaluate(test_df)
    print(f"The accuracy of the model on the database {db} is: {accuracy}%")

if __name__ == "__main__":
    train_and_test("data/DB.csv")
