import pandas as pd

#קלאס שמקבל נתיב לקובץ csv ןקורא אותו על ידי ספריית pandas
class DatasetLoader:
    def load(self, path):
        df = pd.read_csv(path)
        return df

