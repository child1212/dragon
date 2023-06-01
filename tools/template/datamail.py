#%%
import pandas as pd


data = pd.read_excel("D:\\pyprogram\\PyTestTools\\dragon\\tools\\template\\data_mail.xlsx")

time = {}


data_1 = data.values

for data_info in data_1:
