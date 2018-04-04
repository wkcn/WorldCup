#coding=utf-8
import random
from arrange import *
from event import *

def GetPlayers(team):
    #return a List, the all player in this team, ordered by id
    players = []
    #FW,MF,DF,GK
    p = ['FW','MF','DF','GK']
    t = [(1,5,4,1),(2,4,4,1),(3,3,4,1)]
    random.shuffle(t)
    for z in t:
        try:
            for i in range(-1,-5,-1):
                players += sorted(random.sample(team.players[p[i]].values(),z[i]), key = lambda Player : Player.id)
            break
        except ValueError:
            players = []

    return players


def GetPlayersInfo(players):
    output = ''
    for p in players:
        output += '#%d, %s, %s\n' % (p.id,p.name,p.position)
    return output

def CreatEvent():
    # not done yet
    f = open("events.txt")
    for x in f.readlines():
        print x
    f.close()


if __name__ == '__main__':
    teams = GetTeamsInfo()
    groups = Seeding(teams)
    arrange = GetArrangement(groups)
    eventLib = EventLib()
    output = ''
    output += 'Group state:\n'
    for a in arrange:
        output += str(a) + '\n'
        (op,ev) = Emulate(teams,a,eventLib,True)
        output += op + '\n'
    file = open('GroupMatch.txt','w')
    file.writelines(output)
    file.close()
