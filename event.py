#coding=utf-8
import random
class EventLib:
    def __init__(self):
        self.events = [[],[]]
        file = open('events.txt','r')
        for line in file:
            sp = line.replace('\n','').split(' ')
            if sp[-1] == '\n' or sp[-1] == '':
                del sp[-1]
            sen = ' '.join(sp[1:])
            self.events[int(sp[0])].append(sen)
    def GetEvent(self,teamA,teamB,nameA,nameB,menjiangB,success):
        #teamA is class Team
        #nameA is the name of the attacker
        #when success is 1, return the success event;
        #otherwise, return the fail event
        sen = random.choice(self.events[success])
        sen = sen.replace('{teamA}',teamA.country)
        sen = sen.replace('{teamB}',teamB.country)
        sen = sen.replace('{nameA}',nameA)
        sen = sen.replace('{nameB}',nameB)
        sen = sen.replace('{menjiangB}',menjiangB)
        return sen
		
class Event:
	def __init__(self,time,context,score):
		self.time = time
		self.context = context
		self.score = score
	def __str__(self):
		return '[%.2d:%.2d] ' % (self.time / 60, self.time % 60) + self.context + '\n'
