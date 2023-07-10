import pandas as pd

table = pd.read_excel("E:\\dragon\\dragon-config\\excel\\DataFile\\ItemTemplate.xlsx")

v = table.values
table_dict = {}

for line in v:
    table_dict[line[0]] = line[1]

def get_item_name(item_id):
    print("\t\t\t",table_dict[item_id])

while True:
    item_id = int(input("\n请输入物品id:\n"))
    if item_id in table_dict:
        get_item_name(item_id)
    else:
        print("物品不存在")
