import pandas as pd


# read_csv

file = ''


!type file



df =  pd.read_csv(file, sep=',', header=None)
df =  pd.read_csv(file, sep='s+')

df =  pd.read_csv(file, names['a', 'b', 'c', 'd', 'message'])



df =  pd.read_csv(file, index_col='message')

df =  pd.read_csv(file, index_col=['key1, 'key2'])


other options:
parse_dates
skiprows
usecols