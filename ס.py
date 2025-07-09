import pandas as pd
from pprint import pprint

table = pd.read_csv("Demo.csv")
table = table.drop(columns=['id'])
target = table.columns[-1]

count_yes = table[target].value_counts()['yes']
count_no = table[target].value_counts()['no']

percent_yes = float(round(count_yes / len(table), 2))
percent_no = float(round(count_no / len(table), 2))

print(f"\n=== הסתברויות בסיס ===")
print(f"P(yes) = {percent_yes}")
print(f"P(no) = {percent_no}")

yes_dict = {}
no_dict = {}

for col in table.columns[:-1]:
    yes_dict[col] = {}
    no_dict[col] = {}

    for val in table[col].unique():
        yes_count = table[(table[col] == val) & (table[target] == 'yes')].shape[0]
        no_count = table[(table[col] == val) & (table[target] == 'no')].shape[0]

        yes_dict[col][val] = float(round(yes_count / count_yes, 2))
        no_dict[col][val] = float(round(no_count / count_no, 2))

print("\n=== הסתברויות כאשר הלקוח קנה מחשב ===")
pprint(yes_dict)

print("\n=== הסתברויות כאשר הלקוח לא קנה מחשב ===")
pprint(no_dict)
