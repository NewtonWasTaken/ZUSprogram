import pandas
import pandas as pd

table_1_list = pd.read_html("program1.xls")
table_1 = table_1_list[0].fillna(0).to_dict(orient="list")
table_2_list = pd.read_html("program2.xls")
table_2 = table_2_list[0].fillna(0).to_dict(orient="list")


for i in range(len(table_1["Autor"])):
    if table_1["Autor"][i] == 0:
        del table_1["Autor"][i]

for i in range(len(table_1["Skladba"])):
    if table_1["Skladba"][i] == 0:
        del table_1["Skladba"][i]
del table_2["Skladby"]
table_2.update({"Skladba":[]})
table_2.update({"Autor":[]})
table_2["Skladba"] += table_1["Skladba"]
table_2["Autor"] += table_1["Autor"]

for i in range(len(table_2["Poznámka"])):
    if table_2["Poznámka"][i] != 0.0:
        table_2["Předmět"][i] = table_2["Předmět"][i] + " \n" + table_2["Poznámka"][i]


for i in range(len(table_2["Číslo"])):
    table_2["Číslo"][i] = f'{table_2["Číslo"][i]}.'


del table_2["Poznámka"]
del table_2["Učitel"]
del table_2["Délka"]

order = ("Číslo", "Autor", "Skladba", "Žák (žáci)", "Ročník", "Předmět")
final_table = {}
for i in order:
    final_table[i] = table_2[i]
table_dataframe = pandas.DataFrame(final_table)
table_dataframe.to_excel("program_result.xlsx", index=False)
print(table_1)
print(table_2)
print(table_dataframe)

