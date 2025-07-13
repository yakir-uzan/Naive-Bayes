import pandas as pd

#קלאס שמקבל נתיב לקובץ csv ןקורא אותו על ידי ספריית pandas
# ובמקרה שיש בקובץ עמודת ID הוא מוחק אותה ומחזיר רשימה חדשה בלי עמודת הID

class DatasetLoader:
    def load(self, path):
        df = pd.read_csv(path)
        if 'id' in df.columns:
            df = df.drop(columns = ['id'])
        return df
