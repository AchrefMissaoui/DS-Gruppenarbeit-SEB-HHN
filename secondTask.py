import pandas as pd
class ExcelHandler:
    dict = {}
    def __init__(self):
        dict_from_csv = pd.read_csv('data.csv', sep=";").to_dict()
        for i in dict_from_csv["Customer"]:
            self.dict[dict_from_csv["Customer"][i]] = dict_from_csv["Revenue"][i]

    def printDictionary(self):
        print(self.dict)
    def getValue(self,customer):
        print("Wert für",customer,"ist",self.dict[customer])


#### Dritte Aufgabe

    def writeDictionnary(self,fileName):
        df = pd.DataFrame(self.dict.items())
        df.to_csv(fileName+".csv",header=None,sep=";",index=None)


handler = ExcelHandler()
handler.writeDictionnary("g")

