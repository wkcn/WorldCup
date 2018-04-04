# coding=utf-8
import datetime
from seeding import *

class Arrangement:
    def __init__(self,A,B,group,place,time):
        self.A = A
        self.B = B
        self.group = group
        self.place = place
        self.time = time
    def GetTime(self,number=False):
        st = datetime.datetime(2014,6,11)
        nt = st + datetime.timedelta(days = self.time)
        months = ['','January','February','March','April','May','June',\
                    'July','August','September','October','November','December']
        if number:
            return [nt.month,nt.day]
        return months[nt.month] + ' ' + str(nt.day)
    def __str__(self):
        output = self.A + ' vs ' + self.B + ', '
        output += self.place + ', '
        output += self.GetTime()
        return output


def GetPlaces():
    places = []
    file = open('places.txt','r')
    for line in file:
        places.append(line.replace('\n',''))
    file.close()
    return places

def GetArrangement(groups,startDay = 0):
    #return a List, the all arrangement
    arrange = []
    places = GetPlaces()
    day  = startDay
    for (i,j) in {(0,1),(1,2),(2,3),(3,0),(0,2),(1,3)}:
        for k in range(2):
            pl = random.sample(places,4)
            for u in range(4):
                g = k * 4 + u
                A = groups[g][i]
                B = groups[g][j]
                arrange.append(Arrangement(A,B,chr(ord('A') + g),pl[u],day))
            day += 1
    return arrange,day

def GetArrangement16to8(groups,startDay = 0):
    #return a List, the all arrangement
    arrange = []
    places = GetPlaces()
    day  = startDay
    combine = [] #比赛组合
    
    for i in range(4):
        combine.append((groups[i*2][0],groups[i*2+1][1]))
    for i in range(4):
        combine.append((groups[i*2][1],groups[i*2+1][0]))

    oldcombine = combine

    random.shuffle(combine)
    for i in range(4):
        pl = random.sample(places,2)
        A = combine[i*2][0]
        B = combine[i*2][1]
        arrange.append(Arrangement(A,B,chr(ord('A') + i),pl[0],day))
        A = combine[i*2+1][0]
        B = combine[i*2+1][1]
        arrange.append(Arrangement(A,B,chr(ord('A') + i),pl[1],day))
        day += 1
    return arrange,day,oldcombine

def GetArrangementFromCombination(combination,startDay = 0):
    arrange = []
    places = GetPlaces()
    day = startDay
    for (a,b) in combination:
        arrange.append(Arrangement(a,b,'Z',random.choice(places),day))
        day += 1
    return arrange,day

def GetArrangementInfo(arrange):
    output = ''
    ti = -1
    for a in arrange:
        if ti != a.time:
            output += a.GetTime() + '\n'
            ti = a.time
        output += ' ' + a.A + ' vs ' + a.B + ', '
        output += a.place + '\n'
    return output
    
def PrintArrangement(arrange):
    #arrange is a List
    #sort arrange by time
    arrange = sorted(arrange, key = lambda Arrangement : Arrangement.time)

    output = 'Matches by squads\n'
    #print arrangement by group
    arr = [[] for i in range(16)]
    for a in arrange:
        arr[ord(a.group) - ord('A')].append(a)

    for g in range(8):
        output += 'Group ' + chr(ord('A') + g) + '\n'
        for a in arr[g]:
            output += ' ' + a.A + ' vs ' + a.B + ', '
            output += a.place + ', '
            output += a.GetTime() + '\n'

    output += '\n'
    output += 'Matches by date\n'
    ti = -1
    for a in arrange:
        if ti != a.time:
            output += a.GetTime() + '\n'
            ti = a.time
        output += ' ' + a.A + ' vs ' + a.B + ', '
        output += a.place + '\n'

    print output
    file = open('schedule16.txt','w')
    file.writelines(output)
    file.close()

if __name__ == '__main__':
    teams = GetTeamsInfo()
    PrintTeamsInfo(teams)
    groups = Seeding(teams)
    arrange = GetArrangement(groups,0)
