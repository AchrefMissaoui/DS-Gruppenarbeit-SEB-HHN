import pandas as pd


dict_from_csv = pd.read_csv('data.csv', sep=";",index_col=None).to_dict("index")

dict={}
for i in dict_from_csv:
    dict[dict_from_csv[i]["Customer"]] = dict_from_csv[i]["Revenue"]


for customer in dict:
    print("Umsatz", customer, ":", dict[customer])




