#%%
rizhi = open("m1jk2z.log", "r",encoding="utf-8")
rizhi1 = open("rizhi1-1.txt", "w",encoding="utf-8")
rizhi2 = open("rizhi1-2.txt", "w",encoding="utf-8")
for line in rizhi:
    if '执行方法：video_ads' in line:
        if 'front' in line:
            rizhi1.write(line)
        else:
            rizhi2.write(line)

rizhi.close()
rizhi1.close()
rizhi2.close()

# %%
