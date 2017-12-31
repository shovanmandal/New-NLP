####  Reading from Excel  ######

# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'tags.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
#print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')

print(df1)


#####  Writing to excel  ###########

# Install `XlsxWriter` 
pip install XlsxWriter

# Specify a writer
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

# Write your DataFrame to a file     
yourData.to_excel(writer, 'Sheet1')

# Save the result 
writer.save()
