import sqlite3
import pandas as pd

conn = sqlite3.connect('test.db')

df = pd.read_sql("SELECT * FROM RECIPE_TABLE", conn)

def createDataSet(file, key, start, end):
    with open (file, 'a', encoding='utf8') as f:
        for idx, value in enumerate(df[key].values):
            if (idx >= start and idx < end):
                f.write(value + '\n')

# delete before creating new one's

# creating test data
createDataSet("test.from", 'INGREDIENTS', 0, 1999)
createDataSet("test.to", 'STEPS', 0, 1999)

# creating training data
# createDataSet("train.from", 'INGREDIENTS', 10, 20)
# createDataSet("train.to", 'STEPS', 10, 20)
