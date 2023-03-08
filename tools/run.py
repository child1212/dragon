#%%
from os import name
import os
pack_pos = os.path.dirname(os.path.dirname(__file__))
import sys
sys.path.append('{pack_pos}\\function'.format(pack_pos=pack_pos))
sys.path.append('{pack_pos}\\package'.format(pack_pos=pack_pos))
from xieyi import *

account = 1061
server = "https://dtest.gameyici.com"
version = "3.1.0"

def create(account, server,version):
    log = login(account, server, version)
    data = enterGame(log, server,version)
    g =Guide(log, server, version)
    s =senceData(log, server, version)
    m =magicalcreature(log, server, version)


    playerid = log.playerId
    sessionid = log.sessionId
    guide = ''
    scene = ''
    task = ''
    obstacle = ''
    sequenceId='0'
    fil = open("D:\\pyprogram\\PyTestTools\\dragon\\tools\\orderclick.csv","r")
    x = 2
    for line in fil:
        if x == 0:
            line = line.replace("\n",'')
            D = line.split(",")
            requestId = D[1]
            guide = D[2]
            scene = D[3]
            task = D[4]
            obstacle = D[5]
            position=D[6]
            farm = D[7]
            build = D[8]
            item = D[9]
            count = D[10]
            print(requestId)
            protocol_post(requestId, playerid, version, server,sessionid, guide=guide,scene=scene,task=task,obstacle=obstacle,position=position,farm=farm,building=build,itemid=item,itemcount=count)
        else:
            x -= 1
    fil.close()

if __name__ == "__main__":
    create(account, server,version)

# %%
