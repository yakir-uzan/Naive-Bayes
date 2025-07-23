import pandas as pd

class DataCleaner:
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        # הסרת עמודת ID אם קיימת
        if 'id' in df.columns:
            df = df.drop(columns=['id'])

        # מחיקת עמודות ריקות
        df = df.dropna(axis=1, how='all')

        # מחיקת שורות ריקות
        df = df.dropna(how='all')

        # הוספת 1 לכל ערך שהוא 0
        for col in df.select_dtypes(include=['number']).columns:
            if (df[col] == 0).any() or df[col].isnull().any():
                df[col] = df[col].apply(lambda x: x + 1 if pd.notnull(x) and x == 0 else x)

        # איפוס האינדקס
        df = df.reset_index(drop=True)

        return df
