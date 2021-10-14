#%%
import random

data = {20:100,30:300,40:250,50:200,70:100,100:50}
value_list = []

for key,value in data.items():
    value_list += value*[key]


ans = []
for i in range(100):
    all = 0
    for j in range(10):
        all += random.choice(value_list)
        if all > 199:
            ans.append(j+1)
            break
# print(ans)
print(sum(ans)/100)
    
    

# %%
