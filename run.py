#coding=utf-8
from team import *
from arrange import *
from emulate import *
from PyQt4 import QtCore, QtGui
from time import sleep


def SortTeam(a,b):
    if a.info['pts'] != b.info['pts']:
        return b.info['pts'] - a.info['pts']
    if a.info['gd'] != b.info['gd']:
        return b.info['gd'] - a.info['gd']
    if a.info['gf'] != b.info['gf']:
        return b.info['gf'] - a.info['gf']
    return a.rank - b.rank


def SortPlayer(a,b):
    if a.info['g'] != b.info['g']:
        return b.info['g'] - a.info['g']
    if a.country != b.country:
        if a.country <  b.country:
            return -1
        return 1
    if a.name == b.name:
        return 0
    if a.name < b.name:
        return -1
    return 1


def SortPlayerList(a,b):
    if a['g'] != b['g']:
        return b['g'] - a['g']
    if a["tm"] != b["tm"]:
        if a["tm"] <  b["tm"]:
            return -1
        return 1
    if a["name"] < b["name"]:
        return -1
    return 1


class MainFunc(QtGui.QWidget):
    setPicSignal = QtCore.pyqtSignal(list)
    fillTeamListSignal = QtCore.pyqtSignal(list)
    fillPersonalListSignal = QtCore.pyqtSignal(list)
    setTimeSignal = QtCore.pyqtSignal(list)
    setNowPlayingSignal = QtCore.pyqtSignal(list)
    setPointsSignal = QtCore.pyqtSignal(list)
    setLiveSignal = QtCore.pyqtSignal(str)
    endSignal = QtCore.pyqtSignal()
    setTitleSignal = QtCore.pyqtSignal(str)


    def __init__(self,parent=None):
        super(MainFunc,self).__init__(parent)
        self.eventLib = EventLib()
        self.teams = GetTeamsInfo()
        self.groups = Seeding(self.teams)
        self.flags = self.getFlags()
        self.arrange,self.day = GetArrangement(self.groups)
        #游戏进行的速度
        self.speed = 0.2
        self.matchNum = 0
        self.teamNum = {}
        self.oldwins = []
        self.first = False


    def getFlags(self):
        flags = dict()
        f = open("flags.txt")
        lines = f.readlines()
        f.close()
        lines = lines[:32]
        for line in lines:
            [a,b] = line.split('|')
            flags[a]=b.strip()
        return flags



    def CountStateResult(self,teams,arrange,w):
        output = 'Schedule for round of %d:\n' % (w*2)
        output += GetArrangementInfo(arrange).replace(', ',' at ')
        #print output
        file = open('schedule%d.txt' % w,'w')
        file.writelines(output)
        file.close()


    def TeamsRank(self,teams,combine):
        ts = []
        for (a,b) in combine:
            ts.append(teams[a])
            ts.append(teams[b])

        output = '\nTeams Rank:\n'
        output += '%-22sW    D\tL\tGF\tGA\tGD\tPts\n' % 'Team'
        for t in sorted(ts,SortTeam):
            output += '%-22s%d    %d\t%d\t%d\t%d\t%d\t%d\n' % (t.country,t.info['w'],t.info['d'],t.info['l'],
                        t.info['gf'],t.info['ga'],t.info['gd'],t.info['pts'])
        return output


    def Get8(self,output):
        for i in range(8):
            t = []
            for name in self.groups[i]:
                t.append(self.teams[name])
            t = sorted(t,cmp=SortTeam)
            print t[0].country,t[1].country,t[2].country,t[3].country,'\n'
            self.groups[i] = [t[0].country,t[1].country]

        # print GetGroupsInfo(groups)
        #16 to 8

        self.arrange,self.day,combine = GetArrangement16to8(self.groups,self.day + 1)
        # PrintArrangement(self.arrange)
        wins = []
        res = 'Final Result:\n'
        for a in self.arrange:
            output += str(a) + '\n'
            op,ev,win,score = self.Emulate(self.teams,a,self.eventLib,True)
            res += str(a) + '\n'
            res += '%d : %d '%(score[0],score[1]) + win + ' Win\n'
            wins.append(win)
            self.setPicSignal.emit([81+self.arrange.index(a),self.flags[win]])
            output += op + '\n'
        #print output
        res += self.TeamsRank(self.teams,combine)

        file = open('Result8.txt','w')
        file.writelines(res)
        file.close()

        top = 'Qualified for round of 8\n'
        for w in wins:
            top += w + '\n'
        file = open('team8.txt','w')
        file.writelines(top)
        file.close()
        return combine,wins,output


    def Taotai(self,output,combine,wins,toNum):
        newCombine = []
        if toNum==1:
            newCombine.append((self.oldwins[0],self.oldwins[1]))
        #Get toNum*2 self.Teams
        for i in range(toNum):
            (a1,b1) = combine[i*2]
            (a2,b2) = combine[i*2+1]
            if a1 in wins:
                t1 = a1
            else:
                t1 = b1
            if a2 in wins:
                t2 = a2
            else:
                t2 = b2
            newCombine.append((t1,t2))

        self.arrange,self.day = GetArrangementFromCombination(newCombine,self.day + 1)
        print GetArrangementInfo(self.arrange)

        self.oldwins = wins
        wins = []
        res = 'Final Result:\n'
        for a in self.arrange:
            output += str(a) + '\n'
            op,ev,win,score = self.Emulate(self.teams,a,self.eventLib,True)
            res += str(a) + '\n'
            res += '%d : %d '%(score[0],score[1]) + win + ' Win\n'
            wins.append(win)
            if toNum==1 and not self.first:
                self.first = True
            elif toNum==1 and self.first:
                self.setPicSignal.emit([11,self.flags[win]])
            else:
                num=toNum*10+1+self.arrange.index(a)
                self.setPicSignal.emit([num,self.flags[win]])
            output += op + '\n'

        res += self.TeamsRank(self.teams,newCombine)

        file = open('Result%d.txt' % toNum,'w')
        file.writelines(res)
        file.close()

        
        top = 'Qualified for round of %d\n' % toNum
        for w in wins:
            top += w + '\n'
        file = open('team%d.txt' % toNum,'w')
        file.writelines(top)
        file.close()
        if toNum==2:
            for winner in wins:
                del(self.oldwins[self.oldwins.index(winner)])

        return newCombine,wins,output


    def CountFirstStateResult(self,teams,groups):
        #输出小组比赛结果
        #A-H组
        output = ''
        nextState = []
        for i in range(8):
            output += 'Final result for group ' + chr(ord('A') + i) + '\n'
            output += '%-22sW    D\tL\tGF\tGA\tGD\tPts\n' % 'Team'
            t = []
            for name in groups[i]:
                t.append(teams[name])
            ts = sorted(t,SortTeam)
            for t in ts:
                output += '%-22s%d    %d\t%d\t%d\t%d\t%d\t%d\n' % (t.country,t.info['w'],t.info['d'],t.info['l'],
                        t.info['gf'],t.info['ga'],t.info['gd'],t.info['pts'])
            nextState += ts[0:2]
        
        print output + '\n'
        file = open('Result16.txt','w')
        file.writelines(output)
        file.close()

        output = ''

        output += 'Qualified for round of 16:\n'
        for t in nextState:
            output += t.country + '\n'

        print output
        file = open('team16.txt','w')
        file.writelines(output)
        file.close()



    def CountFinalResult(self,teams):
        output = ''
        ts = sorted(teams.values(),SortTeam)
        output += 'Top ten teams:\n'
        output += '    %-22sW    D\tL\tGF\tGA\tGD\tPts\n' % 'Team'
        for i in range(10):
            t = ts[i]
            output += '%-4s%-22s%d    %d\t%d\t%d\t%d\t%d\t%d\n' % ('%d.' % (i+1),t.country,t.info['w'],t.info['d'],t.info['l'],
                        t.info['gf'],t.info['ga'],t.info['gd'],t.info['pts'])
        output += '\n'
        output += 'Goalscorers\n\n'

        people = []
        for team in teams.values():
            for v in team.players.values():
                people += v.values()
        t = -1
        for p in sorted(people,SortPlayer):
            if t != p.info['g']:
                if p.info['g'] == 0:
                    break
                t = p.info['g']
                if t > 1:
                    output += str(t) + ' goals\n'
                else:
                    output += '1 goal\n'
            output += p.name + ', ' + p.position + ', ' + p.country + '\n'

        file = open('finalStastics.txt','w')
        file.writelines(output)
        file.close()


    def ChangeTitle(self,team):
        self.matchNum += 1
        if self.matchNum<=48:
            if team in self.teamNum:
                self.teamNum[team]+=1
                s = "%s组 - 第%d场" % (team,self.teamNum[team])
            else:
                self.teamNum[team]=1
                s = "%s组 - 第1场" % team
        elif self.matchNum<=48+8:
            s = "1/8决赛 - 第%d场" % (self.matchNum-48)
        elif self.matchNum<=48+8+4:
            s = "1/4决赛 - 第%d场" % (self.matchNum-48-8)
        elif self.matchNum<=48+8+4+2:
            s = "半决赛 - 第%d场" % (self.matchNum-48-8-4)
        elif self.matchNum==48+8+4+2+1:
            s = "季军赛"
        else:
            s = "决赛！"
        self.setTitleSignal.emit(s)


    def Emulate(self,teams,arrange,eventLib,timeout = False):
        self.ChangeTitle(teams[arrange.A].info["gp"])
        A = arrange.A
        B = arrange.B
        self.setNowPlayingSignal.emit([self.flags[A],self.flags[B]])
        self.setTimeSignal.emit(arrange.GetTime(True))
        msg = "%s vs %s\n地点: %s\n" % (A,B,arrange.place)
        self.setLiveSignal.emit(msg)
        pA = GetPlayers(teams[A])
        pB = GetPlayers(teams[B])
        output = ''
        output += A + '\n'
        output += GetPlayersInfo(pA)
        output += B + '\n'
        output += GetPlayersInfo(pB)

        output += 'Playing...\n'
        pl,ev,w,s = self.Play(teams,A,B,pA,pB,eventLib,timeout)
        output += pl
        self.setLiveSignal.emit("cln")
        self.freshDataLists()
        return output,pl,w,s


    def Play(self,teams,A,B,pA,pB,eventLib,timeout = False):
        #teams,teamA,teamB,the players of A,the players of B
        #当timeout为True时，允许加时赛
        output = ''
        rankA = teams[A].rank
        rankB = teams[B].rank
        #射门能力值
        abilityA = 320 / rankA
        abilityB = 320 / rankB
        # abilityA = int(1000 - rankA * rankA / 10)
        # abilityB = int(1000 - rankB * rankB / 10)

        blackHorse = 4

        if rankA < rankB:
            abilityB = int(min(abilityA*2,int(abilityB * (random.random() * blackHorse + 1))))
        else:
            abilityA = int(min(abilityB*2,int(abilityA * (random.random() * blackHorse + 1))))

        score = [0,0] #scoreA and scoreB
        attack = [pA,pB]
        menjiang = ['','']
        for i in range(2):
            for p in attack[i]:
                if p.position == 'GK':
                    menjiang[i] = p.name
                    break

        name = [A,B]
        t = 0  #time seconds
        eventP = 350.0 / 5400   #发生事件的概率
        weak = 0.2             #衰弱值
        morale = 0.1           #士气
        eventA = 0.3           #timeout add morale
        events = []
        t += random.randint(180,300)
        time = 90 * 60
        addTime = 0
        dq = 0
        oldscore = score
        while t < time:
            self.setPointsSignal.emit([0,0])
            r = random.random()
            if r < eventP:
                #发生事件
                c = random.random() <= 0.5
                d = 1 -  c
                a = random.randint(0,abilityA)
                b = random.randint(0,abilityB)
                k = [a,b]
                #c is the attacker, and d is the defender
                attacker = random.choice(attack[c][1:])
                defender = random.choice(attack[d][1:])
                if k[c] > k[d]:
                    #success
                    ev = Event(t,eventLib.GetEvent(teams[name[c]],teams[name[d]],attacker.name,defender.name,menjiang[d],1),score)
                    events.append(ev)
                    output += str(ev) + '\n'
                    score[c] += 1
                    oldscore = score
                    k[c] *= (1.0 + morale)
                    eventP *= (1.0 - weak)
                    t += 120
                    output += '当前比分: ' + str(score[0]) + ' : ' + str(score[1]) + '\n'
                    #update player info
                    teams[name[c]].players[attacker.position][attacker.name].info['g'] += 1
                else:
                    #fail
                    ev = Event(t,eventLib.GetEvent(teams[name[c]],teams[name[d]],attacker.name,defender.name,menjiang[d],0),score)
                    events.append(ev)
                    output += str(ev) + '\n'
                self.setLiveSignal.emit(str(ev))

            t += random.randint(3,180)

            if t >= time and (timeout and score[0] == score[1]):
                if addTime < 2:
                    addTime += 1
                    msg = '当前双方持平: ' + str(score[0]) + ' : ' + str(score[1]) + ', 进入第%d场加时赛' % addTime
                    ev = Event(time,msg,score)
                    events.append(ev)
                    output += str(ev) + '\n'
                    time += 15 * 60   #加时
                    eventP = eventP * (1.0 + eventA)
                    self.setLiveSignal.emit(str(ev))
                else:
                    #点球
                    suc = False
                    while not suc:
                        dq += 1
                        tmpMsg = '当前双方持平: ' + str(score[0]) + ' : ' + str(score[1]) + ', 进入点球大战第%d轮' % dq
                        ev = Event(t,tmpMsg,score)
                        msg+=tmpMsg
                        events.append(ev)
                        output += str(ev) + '\n'
                        self.setLiveSignal.emit(str(ev))
                        for c in range(2):
                            d = 1 - c
                            t += random.randint(90,180)
                            attacker = random.choice(attack[c][1:])
                            defender = random.choice(attack[d][1:])
                            if random.random() <= 0.3:
                                ev = Event(t,eventLib.GetEvent(teams[name[c]],teams[name[d]],attacker.name,defender.name,menjiang[d],1),score)
                                events.append(ev)
                                output += str(ev) + '\n'
                                score[c] += 1
                            else:
                                ev = Event(t,eventLib.GetEvent(teams[name[c]],teams[name[d]],attacker.name,defender.name,menjiang[d],0),score)
                                events.append(ev)
                                output += str(ev) + '\n'
                            self.setLiveSignal.emit(str(ev))
                        if score[0] != score[1]:
                            suc = True

                    time = t

            self.setPointsSignal.emit(score)
            sleep(self.speed)


        msg = '比赛结束！\n最终比分: ' + str(score[0]) + ' : ' + str(score[1]) + ', '

        if score[0] == score[1]:
            msg += '平局'
        else:
            msg += name[score[0] < score[1]] + '队胜利！'
        ev = Event(time,msg,score)
        events.append(ev)
        output += str(ev) + '\n'

        score = oldscore

        #统计结果
        if score[0] == score[1]:
            teams[A].info['d'] += 1
            teams[A].info['gf'] += score[0]
            teams[A].info['ga'] += score[1]

            teams[B].info['d'] += 1
            teams[B].info['gf'] += score[1]
            teams[B].info['ga'] += score[0]
        else:
            w = score[0] < score[1]
            l = 1 - w
            teams[name[w]].info['w'] += 1
            teams[name[l]].info['l'] += 1
            teams[A].info['gf'] += score[0]
            teams[A].info['ga'] += score[1]
            teams[B].info['gf'] += score[1]
            teams[B].info['ga'] += score[0]

        #update gd
        teams[A].info['gd'] = teams[A].info['gf'] - teams[A].info['ga']
        teams[B].info['gd'] = teams[B].info['gf'] - teams[B].info['ga']
        #update pts
        teams[A].info['pts'] = teams[A].info['w'] * 3 + teams[A].info['d']
        teams[B].info['pts'] = teams[B].info['w'] * 3 + teams[B].info['d']

        w = (score[0] < score[1])
        self.setLiveSignal.emit(msg+'\n')
        sleep(self.speed*5)
        return output,events,name[w],score


    def next_step(self):
        output = ''
        output += 'Group state:\n'
        for a in self.arrange:
            output += str(a) + '\n'
            op,ev,win,sco = self.Emulate(self.teams,a,self.eventLib,False)
            output += op + '\n'
        file = open('GroupMatch.txt','w')
        file.writelines(output)
        file.close()

        #小组赛结束，统计第一阶段比赛结果
        self.CountFirstStateResult(self.teams,self.groups)

        combine, wins,  output = self.Get8(output)
        self.CountStateResult(self.teams,self.arrange,8)
        combine, wins,  output = self.Taotai(output, combine, wins, 4)
        self.CountStateResult(self.teams,self.arrange,4)
        combine, wins,  output = self.Taotai(output, combine, wins, 2)
        self.CountStateResult(self.teams,self.arrange,2)
        combine, wins,  output = self.Taotai(output, combine, wins, 1)
        self.CountStateResult(self.teams,self.arrange,1)
        self.CountFinalResult(self.teams)
        self.setLiveSignal.emit("巴西世界杯正式结束！")
        self.endSignal.emit()

    def freshDataLists(self):
        self.fillTeamListSignal.emit(sorted(self.teams.values(),SortTeam))
        people = []
        for team in self.teams.values():
            for v in team.players.values():
                for p in v.values():
                    w = {
                        'name':p.name,
                        'tm':p.country,
                        'pos':p.position,
                        'g':p.info['g']
                    }
                    people.append(w)

        self.fillPersonalListSignal.emit(sorted(people,SortPlayerList))


if __name__ == "__main__":
    from mainGUI import *
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("./image/logo.png"))
    splash=QtGui.QSplashScreen(QtGui.QPixmap("./image/logo.png"))
    splash.show()
    app.processEvents()
    MainWindow = GUI()
    sleep(2)
    MainWindow.show()
    splash.finish(MainWindow)
    sys.exit(app.exec_())