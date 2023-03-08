
# %%
for num in (101,102,103,104,105,106,107,108,109,110,111,201,202,203,204,205,206,207,301,302,303,401,402,403,404,):
    print('[{num}001,10],'.format(num=num),end='')
# for num in range(2020,2024):
#     print('[{num},9000],'.format(num=num),end='')
# %%
gifts = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\API_tools\\gift.txt",'r',encoding='utf-8-sig')
for i in gifts:
    i = i.replace("\n","")
    print('[{num},1],'.format(num=i),end='')
gifts.close()
