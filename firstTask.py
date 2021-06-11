import pandas as pd


dict_from_csv = pd.read_csv('data.csv',sep=";").to_dict()

dict = {}

for i in dict_from_csv["Customer"]:

    dict[dict_from_csv["Customer"][i]] = {
        "Country" : dict_from_csv["Country"][i],
        "Revenue" : dict_from_csv["Revenue"][i],
        "Currency": dict_from_csv["Currency"][i]
    }

for customer in dict:
    print("Umsatz",customer,":", dict[customer]["Revenue"])


