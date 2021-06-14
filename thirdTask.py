from queue import PriorityQueue

import pandas as pd


class ExcelHandler:
    dict = {}

    def __init__(self):
        self.dict = pd.read_csv('data.csv', sep=";", index_col="Customer").to_dict("index")

    def printDictionary(self):
        new_dict = {}
        for customer in self.dict:
            new_dict[customer] = self.dict[customer]['Revenue']
        print(new_dict)

    def getValue(self, customer):
        print("Wert für", customer, "ist", self.dict[customer]['Revenue'])

    def writeDictionnary(self, fileName):
        df = pd.DataFrame(self.dict.items())
        df.to_csv(fileName + ".csv", header=None, sep=";", index=None)

    def countCurrency(self, currency):
        counter = 0
        for customer in self.dict:
            if self.dict[customer]["Currency"] == currency:
                counter = counter + 1
        print("Die Währung", currency, "kommt insgesamt", counter, "vor.")
        return counter

    def printCurrencies(self):
        currencies = set()
        for customer in self.dict:
            currencies.add(self.dict[customer]["Currency"])
        currencyQueue = PriorityQueue()
        for currency in currencies:
            currencyQueue.put((self.countCurrency(currency), currency))
        while not currencyQueue.empty():
            print(currencyQueue.get())


handler = ExcelHandler()
handler.printCurrencies()
