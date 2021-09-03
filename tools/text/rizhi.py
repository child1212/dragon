#%%
rizhi = open("rizhi.txt", "r")
rizhi1 = open("rizhi1-1.txt", "w")
rizhi2 = open("rizhi1-2.txt", "w")
for line in rizhi:
    if '生产' in line:
        if '添加' in line:
            rizhi1.write(line)
        else:
            rizhi2.write(line)

rizhi.close()
rizhi1.close()
rizhi2.close()

# %%
