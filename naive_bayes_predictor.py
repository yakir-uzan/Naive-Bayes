import pandas as pd
from pprint import pprint

#קורא את הקובץ, מוחק את עמודת הID, שומר את השורה האחרונה כמשתנה מטרה
table = pd.read_csv("DB.csv")
table = table.drop(columns=['id'])
target = table.columns[-1]

# סופרת כמה מופעים יש מכל מחלקה בעמודת המטרה, מחשבת את השכיחות היחסית באחוזים, מעגלת ל־2 ספרות והופכת את זה למילון
target_counts = table[target].value_counts(normalize=True).round(2).to_dict()

# הדפסת הסתברויות הבסיס
print(f"\n=== הסתברויות בסיס ===")
for cls, prob in target_counts.items():
    print(f"P({cls}) = {prob}")

#==================================================================================

# יצירת מילון ריק לכל מחלקת יעד לשמירת הסתברויות מותנות
cond_probs = {}
for cls in target_counts.keys():
    cond_probs[cls] = {}

# עבור כל תכונה וכל מחלקה – יוצרים מילון פנימי וסופרים כמה מופעים יש למחלקה
for col in table.columns[:-1]:
    for cls in target_counts:
        cond_probs[cls][col] = {}
        cls_count = table[table[target] == cls].shape[0]

        # סופר כמה פעמים כל ערך מופיע במחלקה וחושב את ההסתברות המותנית שלו
        for val in table[col].unique():
            count = table[(table[col] == val) & (table[target] == cls)].shape[0]
            cond_probs[cls][col][val] = round(count / cls_count, 2) if cls_count > 0 else 0.0

# מדפיס את כל ההסתברויות המותנות עבור כל ערך בעמודת המטרה
for cls in cond_probs:
    print(f"\n=== הסתברויות כאשר הערך ב־{target} הוא '{cls}' ===")
    pprint(cond_probs[cls])