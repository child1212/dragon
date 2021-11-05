#%%
import random

times = int(input("样本数量："))

data = {20:100,30:300,40:250,50:200,70:100,100:50}
value_list = []

for key,value in data.items():
    value_list += value*[key]


ans = []
for i in range(times):
    all = 0
    j = 0
    while True:
        all += random.choice(value_list)
        j += 1
        if all > 199:
            ans.append(j)
            break
# print(ans)
print(sum(ans)/times)
    
    

# %%
