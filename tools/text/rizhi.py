#%%
rizhi = open("k6gr84.log", "r",encoding="utf-8")
rizhi1 = open("rizhi1.log", "w",encoding="utf-8")
rizhi2 = open("rizhi2.log", "w",encoding="utf-8")
for line in rizhi:
    if '生产' in line:
        if '：1' in line or ": 1 " in line:
            rizhi1.write(line)
        # else:
        rizhi2.write(line)

rizhi.close()
rizhi1.close()
rizhi2.close()

# %%
