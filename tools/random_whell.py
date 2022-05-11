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
import random
times = 1000
data = {1:25,0:65}
value_list = []
for key,value in data.items():
    value_list += value*[key]

ans = 0
x = 0
q = 0
for i in range(times):
    reward = 0
    if q == 3:
        reward = 1
        q = 0
        x += 1
    else:
        reward = random.choice(value_list)
        if reward == 1:
            q = 0
        else:
            q += 1
        
    ans += reward
print(ans)



# %%
