import pandas as pd
from pprint import pprint

table = pd.read_csv("Demo.csv")
table = table.drop(columns=['id'])
target = table.columns[-1]

target_counts = table[target].value_counts(normalize=True).round(2).to_dict()

print(f"\n=== הסתברויות בסיס ===")
for cls, prob in target_counts.items():
    print(f"P({cls}) = {prob}")

#==================================================================================

cond_probs = {cls: {} for cls in target_counts.keys()}

for col in table.columns[:-1]:
    for cls in target_counts:
        cond_probs[cls][col] = {}
        cls_count = table[table[target] == cls].shape[0]

        for val in table[col].unique():
            count = table[(table[col] == val) & (table[target] == cls)].shape[0]
            cond_probs[cls][col][val] = round(count / cls_count, 2) if cls_count > 0 else 0.0

for cls in cond_probs:
    print(f"\n=== הסתברויות כאשר הערך ב־{target} הוא '{cls}' ===")
    pprint(cond_probs[cls])