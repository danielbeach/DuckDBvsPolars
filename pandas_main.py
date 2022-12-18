import pandas as pd
import glob
from datetime import datetime

t1 = datetime.now()


all_files = glob.glob("data/*/*.csv")
files = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    files.append(df)

df = pd.concat(all_files, axis=0, ignore_index=True)
df = df.groupby([df['date'].dt.date]).sum()
print(df)
t2 = datetime.now()
print("duckdb took {x}".format(x=t2-t1))
