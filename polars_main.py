import polars as pl
from datetime import datetime

d1 = datetime.now()
q = (
    pl.scan_csv("data/*/*.csv", parse_dates=True, dtypes={
                            'date': pl.Date,
                            'serial_number' : pl.Utf8,
                            'model' : pl.Utf8,
                            'capacity_bytes' : pl.Utf8,
                            'failure' : pl.Int32
                            })
)

df = q.lazy().groupby(pl.col("date")).agg(pl.col('failure').sum()).collect()
print(df)
d2 = datetime.now()
print(d2-d1)