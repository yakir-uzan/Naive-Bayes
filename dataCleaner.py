import pandas as pd

class DataCleaner:
    def clean(self, df: pd.DataFrame):
        if 'id' in df.columns:
            df = df.drop(columns=['id'])

        # מחיקת עמודות ריקות
        df = df.dropna(axis=1, how='all')

        for col in df.select_dtypes(include=['number']).columns:
            has_missing = df[col].isnull().any()
            has_zero = (df[col] == 0).any()

            if has_missing or has_zero:
                df[col] = df[col].apply(lambda x: x + 1 if pd.notnull(x) and x != 0 else x)

        df = df.dropna(how='all')
        df = df.reset_index(drop=True)
        return df
