import pandas as pd
import sqlite3

con = sqlite3.connect('./database.sqlite')

name_list = ['Country', 'League', 'Match', 'Player',
'Player_Attributes', 'Team', 'Team_Attributes']

for name in name_list:
	df = pd.read_sql_query(f"SELECT * from {name}", con)
	df.to_csv(f'./{name}.csv', index_col= None)
print('Finished..!')

