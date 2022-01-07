import pandas as pd

df = pd.read_parquet("ParquetSample.parquet", engine= 'auto')
print(df)

#install pyarrow
#pip install pytz