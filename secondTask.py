import pandas as pd


class ExcelHandler:
    dict = {}
    dict_from_csv={}

    def __init__(self):
        dict_from_csv = pd.read_csv('data.csv', sep=";").to_dict("index")
        for i in dict_from_csv:
            self.dict[dict_from_csv[i]["Customer"]] = dict_from_csv[i]["Revenue"]

        self.dict_from_csv=dict_from_csv

    def printDictionary(self):
        print(self.dict)

    def getValue(self, customer):
        print("Wert für", customer, "ist", self.dict[customer])

    #### Dritte Aufgabe

    def writeDictionnary(self, fileName):
        df = pd.DataFrame(self.dict.items())
        df.to_csv(fileName + ".csv", header=None, sep=";", index=None)


handler = ExcelHandler()
handler.writeDictionnary("h")
