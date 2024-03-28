#%%
import pygsheets

client = pygsheets.authorize(service_file="test-pyg-sheet-288052707273.json")

sh = client.open("很随便的表")

#%%
wks = sh.sheet1

wks.update_value((1,5),"hello world")

get = wks.get_value("A5")


# %%
