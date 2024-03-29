#%%
import pandas as pd
import copy
import time 
import numpy as np


class actInfo():
    def __init__(self,a_type,old_start_time,name,local,prewarm,old_rank_end_time,old_end_time) -> None:
        self.a_type = a_type
        self.old_start_time = old_start_time
        self.name = name
        self.local = local
        self.prewarm = prewarm
        self.old_rank_end_time = old_rank_end_time
        self.old_end_time = old_end_time

    def keep_rank_end_time(self):
        s = time.strptime(self.old_start_time,"%Y-%m-%d %H:%M:%S")
        s = time.mktime(s)
        e = time.strptime(self.old_rank_end_time,"%Y-%m-%d %H:%M:%S")
        e = time.mktime(e)
        return(e-s)

    def keep_end_time(self):
        s = time.strptime(self.old_start_time,"%Y-%m-%d %H:%M:%S")
        s = time.mktime(s)
        e = time.strptime(self.old_end_time,"%Y-%m-%d %H:%M:%S")
        e = time.mktime(e)
        return(e-s)

    def set_new_activity_time(self,res):
        print(self.name)
        while True:
            new_start_time = input("输入开始时间：")
            if new_start_time == "":
                return 0
            try:
                start_time = time.strptime(new_start_time,"%Y-%m-%d %H:%M:%S")
                start_time = time.mktime(start_time)
                break
            except:
                print("输入数据格式错误，请重新输入！")
        end_time = start_time + self.keep_end_time()
        new_end_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(end_time)))
        res.iloc[self.local,9] = new_start_time
        res.iloc[self.local,11] = new_end_time
        if not pd.isnull(self.old_rank_end_time):
            rank_end_time = start_time + self.keep_rank_end_time()
            new_rank_end_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(rank_end_time)))
            res.iloc[self.local,10] = new_rank_end_time
        if not pd.isnull(self.prewarm):
            prewarm = start_time - 48*3600
            prewarm = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(prewarm)))
            res.iloc[self.local,8] = prewarm


# if __name__ == "__main__":
act = pd.read_excel("E:\\dragon\\dragon-config\\excel\\DataFile\\ActivityTemplate.xlsx")
res = copy.deepcopy(act)

next_one = {}
last_one = {}
i = 0
for index in range(10,len(act.values)):
    if act.values[index][5] != act.values[index-1][5]:
        next_one[act.values[index][5]] = index
        if not last_one.get(act.values[index-1][5]):
            last_one[act.values[index-1][5]] = index-1
    if act.values[index][5] == act.values[index-1][5]:
        act1 = time.strptime(act.values[index][9],"%Y-%m-%d %H:%M:%S")
        acttime1 = time.mktime(act1)
        act0 = time.strptime(act.values[index-1][9],"%Y-%m-%d %H:%M:%S")
        acttime0 = time.mktime(act0)
        if acttime1 < acttime0:
            next_one[act.values[index][5]] = index

            last_one[act.values[index][5]] = index-1
a_types = [1,4,5,7,9,12,10,11,15,23,24,26]
for a_type in a_types:
    index = next_one[a_type]
    index_old = last_one[a_type]
    command = actInfo(a_type,act.iat[index_old,9],act.iat[index_old,1],index,act.iat[index_old,8],act.iat[index_old,10],act.iat[index_old,11])
    command.set_new_activity_time(res)
res.to_excel("ActivityTemplate.xlsx")




        


# %%
