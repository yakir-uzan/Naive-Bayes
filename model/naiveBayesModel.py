#מחשב הסתברויות בסיסיות: כמה דוגמאות שייכות לכל מחלקה
# מחשב הסתברויות מותנות: מה הסיכוי של כל ערך בתכונה מסוימת, בתוך כל מחלקה
# שומר את כל ההסתברויות בתוך משתנים פנימיים שישמשו בהמשך לחיזוי

#==============================================================================

import pandas as pd
from pprint import pprint

# יצירת משתנה מטרה ומילונים בשביל ההסתברות הבסיסית והמותנית
class NaiveBayesModel:
    def __init__(self):
        self.target = None
        self.prior_probs = {}
        self.cond_probs = {}

    # הזנת העמודה הרלוונטית במשתנה המטרה
    # חישוב ההסתברות הבסיסית
    def fit(self, df: pd.DataFrame):
        self.target = df.columns[-1]
        self.prior_probs = df[self.target].value_counts(normalize = True).round(2).to_dict()

        # יוצר מילונים נפרדים עבור כל אחד מהערכים בעמודה
        for cls in self.prior_probs:
            self.cond_probs[cls] = {}

        # 
        for col in df.columns[:-1]:
            for cls in self.prior_probs:
                self.cond_probs[cls][col] = {}
                cls_count = df[df[self.target] == cls].shape[0]

                for val in df[col].unique():
                    count = df[(df[col] == val) & (df[self.target] == cls)].shape[0]

                    unique_vals = df[col].nunique()
                    smoothed_prob = (count + 1) / (cls_count + unique_vals)
                    self.cond_probs[cls][col][val] = round(smoothed_prob, 4)

    # פונקציה שמדפיסה את המילונים של ההסתברויות הבסיסית ןהמותנת
    def print_model(self):
        print("\n=== הסתברויות בסיס ===")
        for cls, prob in self.prior_probs.items():
            print(f"P({cls}) = {prob}")

        for cls in self.cond_probs:
            print(f"\n=== הסתברויות כאשר הערך ב־{self.target} הוא '{cls}' ===")
            pprint(self.cond_probs[cls])