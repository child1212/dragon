import random
count = 33
lenth = count*3 
result = []
randow_seed = range(30)
ans = []
run = lenth
while len(result) < lenth:
    if len(ans) < 5 and run > 0:
        x = random.choice(randow_seed)
        ans += [x,x,x]
        run = run-3
    result.append(ans.pop(random.choice(range(len(ans)))))
