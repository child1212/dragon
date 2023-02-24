#%%
err = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\template\\player_error.txt","r")
e = set()
for line in err:
    line = line.replace("\n",'')
    e.add(line)
err.close()

get_r = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\API_tools\\pid_list.txt",'r')
for line in get_r:
    line = line.replace("\n",'')
    e.discard(line)
get_r.close()

for i in e:
    print(i)
# %%
