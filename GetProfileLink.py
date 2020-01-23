from urllib import request
import pandas as pd


Main_url = "https://www.google.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

Data = pd.read_excel("C://Users//15659//Desktop//syllabus category.xlsx")
Name = Data.iloc[1:32, 13].values
# print(Name)
