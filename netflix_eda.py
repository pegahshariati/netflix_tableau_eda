import pandas as pd

# Preprocessing
# in each sheet of the xlsx file:
# 1. find the number of duplicate rows
# 1.1. find the primary key (show_id) and check if it is unique
# 2. fix data types for columns
# 2.1. incorrect data type (str in 'time duration') write a function to return the rows with misplaced values TODO: check chatgpt for similar solutions
# 2.2. out of range data (1000 min movie duration)
# 3. visualize missing values for some columns using heatmap
# 4. merge TV show and Movies in 'Listed in' column so when asked about top 10 genre, we will not have separated genres named 'international TV shows' and 'international movies'





#load the xlsx data to a pandas df
xl = pd.ExcelFile('netflix_titles.xlsx')
sheet_names = xl.sheet_names  # see all sheet names






a = 1