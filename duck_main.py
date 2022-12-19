import duckdb
from datetime import datetime

t1 = datetime.now()
conn = duckdb.connect()
conn.execute("SET experimental_parallel_csv=TRUE")
conn.execute("""SELECT date, SUM(failure) as failures
                FROM read_csv_auto('data/*/*.csv', delim=',', header=True,  IGNORE_ERRORS=1)
             GROUP BY date;""")
print(conn.fetchall())
t2 = datetime.now()
print("duckdb took {x}".format(x=t2-t1))
