# HP calc

import math
from dex import dex, nameList
from sys import argv
script, inputMode = argv

def quit():
    print 'error'; exit(0)

class Pokemon(object):
	
    def __init__(self, name):
	# order contains the stats in the numbered order i want them displayed
	# with a for loop, I do not need to worry about the order of the order dict
	# order[i] will return the value at i, which will be a stat
	# then that stat will be used as the key for the status dict 
		
        self.name = name
        self.iv = {}
        self.stat = {}
        stats = "HP, Attack, Defense, Speed, Special Attack, Special Defense"
        self.status = {stat: None for stat in stats.split(', ')}
        order ={1:'HP', 2:'Attack', 3:'Defense', 4:'Special Attack', 
                5:'Special Defense', 6:'Speed'}
				
        if inputMode.upper() == "IV" or inputMode.upper() == "STAT":		
            for i in range(1,7):
                self.status[order[i]] = raw_input("Enter the %s %s: " % 
                                                    (order[i], inputMode))
                    
                try:
                    int(self.status[order[i]])
                    if int(self.status[order[i]]) > 999:
                        quit()
                    else:
                        int(self.status[order[i]])
						
                except ValueError:
                    quit()
            
					
        else:
            print "That is not a proper input mode"
            quit()
            
        if inputMode.upper() == "IV":
            self.iv = self.status
        else:
            self.stat = self.status
			
			
def stat_calc(stat, base, ev, level):
    num = (int(stat) + (2*base) + ev/4.0 )*int(level)
    result = (num/100.0) + 5
    return result
	
def hpstat_calc(hp, base, ev, level):
    num = ((int(hp) + (2*base) + ev/4.0 + 100) * int(level))
    result = (num/100.0) + 10
    return result
				
def getStatsfromIV(poke):
    level = raw_input("Enter the level of the pokemon: ")                    
    name = raw_input("Enter the pokemon's name: ")
    base = dex.dex[int(nameList.name[name])]
    base = [int(i) for i in base]
    #npos = int(raw_input("enter the boosted stat: "))
    #nneg = int(raw_input("enter the hindered stat: "))
    print base
    ev = [74,195,86,23,48,84]

    new_HP = hpstat_calc(poke.status["HP"],base[0],ev[0],level)
    new_Atk = stat_calc(poke.status["Attack"],base[1],ev[1],level)*1.1
    new_Def = stat_calc(poke.status["Defense"],base[2],ev[2],level)
    new_Spe = stat_calc(poke.status["Speed"],base[5],ev[3],level)
    new_Spa = stat_calc(poke.status["Special Attack"],base[3],ev[4],level)*0.9
    new_Spd = stat_calc(poke.status["Special Defense"],base[4],ev[5],level)

    new_Stat = [new_HP,new_Atk,new_Def,new_Spe,new_Spa,new_Spd]
    new_Stat = [math.floor(i) for i in new_Stat]
    print new_Stat
        

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
                        
    
                        
    print HPtype
    print HPpower
    


Pikachu = Pokemon("Pikachu")
print Pikachu.status
getHP(Pikachu)
getStatsfromIV(Pikachu)







