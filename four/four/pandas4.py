import pandas as pd

def best(df):
    conditions = (df[['maths', 'physics', 'computer science']] >= 4).all(axis=1)
    return df[conditions]

data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data)

filtered = best(journal)
print(journal)
print(filtered)
