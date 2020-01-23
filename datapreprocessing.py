import numpy as np
import pandas as pd
import matplotlib as plot
from sklearn.preprocessing import Imputer
import graphviz
'''
class PreProcessing:
    data_x: int

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.data_x = 0
        self.data_y = 0

    def get_data(self, rows="default", columns=0):
        self.data = pd.read_csv(self.file_path)
        if rows is "default":
            self.data_x = self.data.iloc[:, :columns]
            self.data_y = self.data.iloc[:, columns]
            print(self.data_x, self.data_y)
        else:
            self.data_x = self.data.iloc[:rows, :columns]
            self.data_y = self.data.iloc[:rows, :columns]
            print(self.data_x, self.data_y)

    def missing_data(self, rows="default", columnStart=0, columnEnd=0):

        imputer = Imputer(missing_values="NaN", strategy="mean")
        if rows == "default":
            self.data[:, columnStart:columnEnd] = imputer.fit_transform(self.data[:, columnStart:columnEnd])
            print(self.data[:, columnStart:columnEnd])


if __name__ == "__main__":
    file_path = "C://Users//15659//Desktop//CS//python file//Data//Data.csv"
    processing_data = PreProcessing(file_path)
    processing_data.get_data(rows="default", columns=3)
    processing_data.missing_data(rows="default", columnStart=1, columnEnd=3)
'''
dataset = pd.read_csv("C://Users//15659//Desktop//CS//python file//Data//Data.csv")
x = dataset.iloc[:, :3].values
y = dataset.iloc[:, 3].values

# deal with missing data


imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
# Imputer is a module
x[:, 1:3] = imputer.fit_transform(x[:, 1:3])

print(x[:, 1:3])
