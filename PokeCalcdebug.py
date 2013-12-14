# HP calc

import math
from dex import dex, nameList, nature
from sys import argv
#script, inputMode = argv

def quit():
    print 'error'; exit(0)

# class Pokemon(object):
	
    # def __init__(self, name, stat={}, iv={} ):
	# # order contains the stats in the numbered order i want them displayed
	# # with a for loop, I do not need to worry about the order of the order dict
	# # order[i] will return the value at i, which will be a stat
	# # then that stat will be used as the key for the status dict 
		
        # self.name = name
        # self.iv = {}
        # self.stat = {}
        # stats = "HP, Attack, Defense, Speed, Special Attack, Special Defense"
        # self.status = {stat: None for stat in stats.split(', ')}
        # order ={1:'HP', 2:'Attack', 3:'Defense', 4:'Special Attack', 
                # 5:'Special Defense', 6:'Speed'}
				
        # if (inputMode.upper() == "IV" or inputMode.upper() == "STAT") and not (self.iv):		
            # for i in range(1,7):
                # self.status[order[i]] = raw_input("Enter the %s %s: " % 
                                                    # (order[i], inputMode))
                    
                # try:
                    # int(self.status[order[i]])
                    # if int(self.status[order[i]]) > 999:
                        # quit()
                    # else:
                        # int(self.status[order[i]])
						
                # except ValueError:
                    # quit()
            
					
        # else:
            # print "That is not a proper input mode"
            # quit()
            
        # if inputMode.upper() == "IV":
            # self.iv = self.status
        # else:
            # self.stat = self.status
			
order ={1:'HP', 2:'Attack', 3:'Defense', 4:'Special Attack', 
                5:'Special Defense', 6:'Speed'}
stats = "HP, Attack, Defense, Speed, Special Attack, Special Defense"
class Pokemon(object):
    def __init__(self, name, level, nature, statsL = [], iv = [], ev = [0,0,0,0,0,0]):
        stats = "HP, Attack, Defense, Speed, Special Attack, Special Defense"
        order ={1:'HP', 2:'Attack', 3:'Defense', 4:'Special Attack', 
                5:'Special Defense', 6:'Speed'}
        self.name = name
        self.level = level
        self.stats = {stat: None for stat in stats.split(', ')}
        self.iv = {stat: None for stat in stats.split(', ')}
        self.ev = {stat: None for stat in stats.split(', ')}
        self.evL = ev
        self.nature = nature
        
        if len(statsL) > 0:
            for i in range(1,7):
                self.stats[order[i]] = statsL[i-1]
        
        if len(iv) > 0:
            for i in range(1,7):
                self.iv[order[i]] = iv[i-1]
        
        if len(ev) > 0:
            for i in range(1,7):
                self.ev[order[i]] = ev[i-1]
                
                
                
			
def stat_calc(stat, base, ev, level):
    num = (int(stat) + (2*base) + ev/4.0 )*int(level)
    result = (num/100.0) + 5
    return result
	
def hpstat_calc(hp, base, ev, level):
    num = ((int(hp) + (2*base) + ev/4.0 + 100) * int(level))
    result = (num/100.0) + 10
    return result
    
# def iv_calc(stat, base, ev, level):
    # #a = ((math.ceil(stat)-5)*100.0/level) - 2.0 * base - math.floor(ev/4.0)
    # #b = 
    # a = (((math.ceil(stat/1) - 5) * 100.0) / level) - 2*base - ev/4
    # return (a )
    
def iv_calc(stat, base, ev, level):
    a = (100*(stat-5))/level
    b = -(2*base)-(ev/4)
    return a+b+1
    
    
def hpiv_calc(hp, base, ev, level):
    #a = ((hp-level-10)*100.0 / level) - 2.0 * base - math.floor(ev/4.0)
    #a = ((hp - 10) * 100.0) / level - 2.0*base - ev/4.0 - 100
    # print (hp-level-10)
    # print 100.0/level
    # print 2.0 * base
    # print math.floor(ev/4.0)
    # b = 
    
    a = (100*(hp-10))/level
    b = -100 -(ev/4) -(2*base)
    
    return a+b+1
    
				
def getStatsfromIV(poke):
    level = poke.level                
    name = poke.name
    base = dex.dex[int(nameList.name[name])]
    base = [int(i) for i in base]
    #npos = int(raw_input("enter the boosted stat: "))
    #nneg = int(raw_input("enter the hindered stat: "))
    #print base
    ev = poke.evL
    nat = nature.natures[poke.nature]
    print nat

    new_HP  = hpstat_calc(poke.iv["HP"],base[0],ev[0],level)
    new_Atk = stat_calc(poke.iv["Attack"],base[1],ev[1],level)#*1.1
    new_Def = stat_calc(poke.iv["Defense"],base[2],ev[2],level)
    new_Spe = stat_calc(poke.iv["Speed"],base[5],ev[3],level)
    new_SpA = stat_calc(poke.iv["Special Attack"],base[3],ev[4],level)#*0.9
    new_SpD = stat_calc(poke.iv["Special Defense"],base[4],ev[5],level)

    new_Stat = [new_HP,new_Atk,new_Def,new_SpA,new_SpD,new_Spe]
    new_Stat = [math.floor(i) for i in new_Stat]
    new_Stat[nat[0]-1] *= 0.9
    new_Stat[nat[1]-1] *= 1.1
    
    status = "HP, Attack, Defense, Special Attack, Special Defense, Speed"
    statlist = status.split(',')
    new_Stats = dict(zip(statlist,new_Stat))
    print new_Stats
    return new_Stats
    
def getIVfromStats(poke):
    level = poke.level
    name = poke.name
    base = dex.dex[int(nameList.name[name])]
    base = [int(i) for i in base]
    ev = poke.evL
    #maxStat = getIVfromStats(poke)
    #print base
    
    new_HP  = hpiv_calc(poke.stats["HP"],base[0],ev[0],level)
    new_Atk = iv_calc(poke.stats["Attack"],base[1],ev[1],level)
    new_Def = iv_calc(poke.stats["Defense"],base[2],ev[2],level)
    new_Spe = iv_calc(poke.stats["Speed"],base[5],ev[3],level)
    new_SpA = iv_calc(poke.stats["Special Attack"],base[3],ev[4],level)
    new_SpD = iv_calc(poke.stats["Special Defense"],base[4],ev[5],level)
    # new_HP  = hpiv_calc(maxStat["HP"],base[0],ev[0],level)
    # new_Atk = iv_calc(maxStat["Attack"],base[1],ev[1],level)#*1.1
    # new_Def = iv_calc(maxStat["Defense"],base[2],ev[2],level)
    # new_Spe = iv_calc(maxStat["Speed"],base[5],ev[3],level)
    # new_SpA = iv_calc(maxStat["Special Attack"],base[3],ev[4],level)#*0.9
    # new_SpD = iv_calc(maxStat["Special Defense"],base[4],ev[5],level)
    
    new_IV = [new_HP,new_Atk,new_Def,new_SpA,new_SpD,new_Spe]
    #new_IV = [math.floor(i) for i in new_IV]
    print new_IV

def getHP(mon):
    a = int(mon.iv["HP"])
    b = int(mon.iv["Attack"])
    c = int(mon.iv["Defense"])
    d = int(mon.iv["Speed"])
    e = int(mon.iv["Special Attack"])
    f = int(mon.iv["Special Defense"])

    HPtype = math.floor(( ((a%2) + (2*(b%2)) + (4*(c%2)) 
                        + (8*(d%2)) + (16*(e%2)) + (32*(f%2)) )*15.0)/63.0 )
  
	
    HPpower =  (( (((a>>1) & 1) + 2*((b>>1) & 1)
                        + 4*((c>>1) & 1) + 8*((d>>1) & 1)
                        + 16*((e>>1) & 1) + 32*((f>>1) & 1))*40)
                        /63)+30
                        
    
    mon.hpType = HPtype
    mon.hpPower = HPpower
    print HPtype
    print HPpower
    

#if __name__ is "__main__":
#Pikachu = Pokemon("absol", statsL =[135,159,75,90,81,75], level = 50, ev = [255,255,255,255,255,255])
#Absol = Pokemon("absol", iv=[20,20,20,20,20,20], level = 50, ev=[0,0,0,0,0,0])
# For = Pokemon("forretress", level = 43, statsL=[121,94,114*(10.0/9),72*(10.0/11),57,41])
# ghost = Pokemon("haunter", level = 58, nature="brave",statsL=[127,69*(10.0/11),57,148,84,116*(10.0/9)], ev=[0,0,0,0,0,0])
ghost = Pokemon("haunter", level = 58, nature="brave",iv = [12,0,0,17,27,24], ev=[0,0,0,0,0,0])
#iv=[31,31,31,31,31,31]
#, ev = [74,195,86,23,48,84]
#print Pikachu.status
#getHP(Pikachu)
#getStatsfromIV(Absol)
#print Pikachu.stats
#getIVfromStats(ghost)
getStatsfromIV(ghost)








