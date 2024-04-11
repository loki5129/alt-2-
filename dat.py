 
# import pandas with shortcut 'pd' 
import pandas as pd 

# read_csv function which is used to read the required CSV file 
data = pd.read_csv('games.csv') 

# display 

# drop function which is used in removing or deleting rows or columns from the CSV files 
data.drop("Genres", inplace=True, axis=1 )
data.drop("Publisher",inplace=True, axis=1)
# display 
file=open("game1.csv","w+")
file.write(data)
file.close()