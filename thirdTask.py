import queue

import pandas as pd
class ExcelHandler:
    dict = {}
    def __init__(self):
        dict_from_csv = pd.read_csv('data.csv', sep=";").to_dict()
        for i in dict_from_csv["Customer"]:
            self.dict[dict_from_csv["Customer"][i]] = {
                "Country": dict_from_csv["Country"][i],
                "Revenue": dict_from_csv["Revenue"][i],
                "Currency": dict_from_csv["Currency"][i]
            }

    def printDictionary(self):
        new_dict={}
        for customer in self.dict:
            new_dict[customer]=self.dict[customer]['Revenue']
        print(new_dict)
    def getValue(self,customer):
        print("Wert für",customer,"ist",self.dict[customer]['Revenue'])

    def writeDictionnary(self,fileName):
        df = pd.DataFrame(self.dict.items())
        df.to_csv(fileName+".csv",header=None,sep=";",index=None)

    def countCurrency(self,currency):
        counter = 0
        for customer in self.dict:
            if self.dict[customer]["Currency"] == currency:
                counter = counter + 1
        print("Die Währung",currency,"kommt insgesamt",counter,"vor.")


    def printCurrencies(self):
        currencyDict = {}
        currencyQueue = queue.PriorityQueue()
        for customer in self.dict:
            if self.dict[customer]["Currency"] not in currencyDict:
                currencyDict[self.dict[customer]["Currency"]] = 1
            else :
                currencyDict[self.dict[customer]["Currency"]] +=1

        for item in currencyDict:
            currencyQueue.put((item,currencyDict[item]))


        while not currencyQueue.empty():
            print(currencyQueue.get())


handler = ExcelHandler()
handler.printCurrencies()
