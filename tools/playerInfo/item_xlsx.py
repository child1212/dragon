#%%
import pandas as pd
import Config

class item_table():
    def __init__(self):
        self.result = {}
        item = pd.read_excel("{f}\\ItemTemplate.xlsx".format(f=Config.FILE_PATH))
        items = item.values
        for x in items:
            self.result[x[0]] = x[14]
      


