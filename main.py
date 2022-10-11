import pandas
import pandas as pd
from functions.edit import Tables


#Imports tables and converts them to dict.
#Nan values are changed to 0
table_1_list = pd.read_html("program1.xls")
table_1 = table_1_list[0].fillna(0).to_dict(orient="list")
table_2_list = pd.read_html("program2.xls")
table_2 = table_2_list[0].fillna(0).to_dict(orient="list")


#Creates Tables object
tb = Tables(table_1, table_2)

#Merges two tables into one
tb.merge()

#Formats Poznámka and Číslo in table
tb.format(type="korepetice")



#Merging Poznámka cells to Předmět cells and editing numbering system
for i in range(len(table_2["Poznámka"])):
    if table_2["Poznámka"][i] != 0.0:
        table_2["Předmět"][i] = table_2["Předmět"][i] + " \n" + table_2["Poznámka"][i]
    table_2["Číslo"][i] = f'{table_2["Číslo"][i]}.'





#Exports data to final table
table_dataframe = pandas.DataFrame(tb.sort())


#Exports to excel table and opens a writer
writer = pd.ExcelWriter('program_result.xlsx', engine='xlsxwriter')
table_dataframe.to_excel(writer, index=False)
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

#Cusomizes columns width and warps text \n
text_wrap_format = workbook.add_format({'text_wrap': True})
worksheet.set_column(0, 0, 5, text_wrap_format)
worksheet.set_column(1, 1, 30, text_wrap_format)
worksheet.set_column(2, 3, 45, text_wrap_format)
worksheet.set_column(4, 4, 7, text_wrap_format)
worksheet.set_column(5, 5, 30, text_wrap_format)
writer.close()

#Printing variables
print(tb.table_2)
print(table_2)
print(table_1)

