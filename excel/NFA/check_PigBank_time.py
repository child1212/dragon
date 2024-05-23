#%%
import pandas as pd
import time

def time_to_unix_time(str_time):
    b=time.strptime(str_time,'%Y-%m-%d %H:%M:%S')
    c=time.mktime(b)
    return int(c)

activity = pd.read_excel("E:\\FA\\nfa-config\\excel\\DataFile\\PiggyBankTemplate.xlsx")

data_activity = activity.values

#key:activity type
#value:activity time
activity_keep_time = {}

for i in range(3, len(data_activity)):
    if not data_activity[i][3] in activity_keep_time.keys():
        activity_keep_time[data_activity[i][3]] = []
    if pd.isna(data_activity[i][5]):
        continue
    elif not pd.isna(data_activity[i][5]):
        starttime = time_to_unix_time(data_activity[i][5])
    endtime = time_to_unix_time(data_activity[i][6])
    activity_keep_time[data_activity[i][3]].append((starttime, endtime,data_activity[i][2]))


for key in activity_keep_time:
    if key not in (3,8):
        temp = activity_keep_time.get(key)
        for i in range(len(temp)-1):
            for j in range(len(temp)-i-1):
                if temp[j][0] > temp[j+1][0]:
                    temp[j],temp[j+1] = temp[j+1],temp[j]

        for i in range(len(temp)-1):
            if temp.count(temp[i]) != 4:
                print("时间错误:\nactivity_type:","\nid:",temp[i][2],end="\n\n")
            pass
            if temp[i][1] > temp[i+1][0] and temp[i][2] != temp[i+1][2]:
                print("时间冲突:\nactivity_type:",key,"\ntime:",temp[i+1][0],"\nid:",temp[i][2],temp[i+1][2])



# %%
