# HP calc

import math
from dex import dex, nameList, nature


def quit():
    print 'error'
    exit(0)

def stat_calc(stat, base, ev, level):
    """ Returns the calculated non-HP stat at given level. """
    num = (int(stat) + (2*base) + ev/4.0)*int(level)
    result = (num/100.0) + 5
    return result


def hpstat_calc(hp, base, ev, level):
    """ Returns the calculated HP stat at given level. """
    num = ((int(hp) + (2*base) + ev/4.0 + 100) * int(level))
    result = (num/100.0) + 10
    return result


def iv_calc(stat, base, ev, level):
    """ Returns the calculated non-HP IV. """
    level = float(level)
    dbase = 2.0*base
    a = math.ceil(((((stat - 5) * 100) / level) - dbase) - math.floor(ev/4.0))
    
    # testing info
    print "stat:%.1f,base:%.1f,ev:%.1f,level:%.1f,a:%.1f" % (stat,base,ev,level,a)
    
    return a


def hpiv_calc(hp, base, ev, level):
    """ Returns the calculated HP IV. """
    level = float(level)
    a = (100*(hp-10))/level
    b = -100 - (ev/4) - (2*base)
    
    # testing info
    # print "stat:%d,base:%d,ev:%d,level:%d,a:%.1f" % (hp,base,ev,level,math.ceil(a+b))
    
    return math.ceil(a+b)

class Pokemon(object):
    """ The Pokemon class that you use the pokemon methods with.

        Instance variables:
        String name -- the actual name of the pokemon, lowercase
        int level -- the level it is at, or the level you want to test
        String nature -- nature in all lowercase
        statsL -- the list of stats[HP,Atk,Def,SpA,SpD,Spe]
        iv -- the list of ivs, same order
        ev -- the list of evs, same order
       """
    def __init__(self, name, level, nature, statsL=[], iv=[], ev=[0,0,0,0,0,0]):
        # I can split this on , 
        stats = "HP, Attack, Defense, Speed, Special Attack, Special Defense"
        # Makes sure that stats are always put in in this order
        order = {1: 'HP', 2: 'Attack', 3: 'Defense', 4: 'Special Attack',
                 5: 'Special Defense', 6: 'Speed'}

        self.name = name
        self.level = level
        self.stats = {stat: None for stat in stats.split(', ')}
        self.iv = {stat: None for stat in stats.split(', ')}
        self.ev = {stat: None for stat in stats.split(', ')}
        self.evL = ev
        self.nature = nature
        self.statsL = statsL
        self.hidden_power = {'type': None, 'power': None}

        # checks if the list of stats/ev/iv was given
        # them populates the respective list
        if len(statsL) > 0:
            for i in range(1, 7):
                self.stats[order[i]] = statsL[i-1]

        if len(iv) > 0:
            for i in range(1, 7):
                self.iv[order[i]] = iv[i-1]

        if len(ev) > 0:
            for i in range(1, 7):
                self.ev[order[i]] = ev[i-1]
        else:
            for i in range(1, 7):
                self.ev[i] = 0


    def iv_to_stats(self):
        """ Calculates stats at given level based on IV.
            Returns dictionary of statname->statvalue. """
        level = self.level
        name = self.name
        base = dex.dex[int(nameList.name[name])]
        base = [int(i) for i in base]
        ev = self.evL
        nat = nature.natures[self.nature]

        new_HP = hpstat_calc(self.iv["HP"], base[0], ev[0], level)
        new_Atk = stat_calc(self.iv["Attack"], base[1], ev[1], level)
        new_Def = stat_calc(self.iv["Defense"], base[2], ev[2], level)
        new_Spe = stat_calc(self.iv["Speed"], base[5], ev[3], level)
        new_SpA = stat_calc(self.iv["Special Attack"], base[3], ev[4], level)
        new_SpD = stat_calc(self.iv["Special Defense"], base[4], ev[5], level)

        new_Stat = [new_HP, new_Atk, new_Def, new_SpA, new_SpD, new_Spe]
        new_Stat = [math.floor(i) for i in new_Stat]
        new_Stat[nat[0]-1] *= 0.9
        new_Stat[nat[1]-1] *= 1.1

        status = "HP, Attack, Defense, Special Attack, Special Defense, Speed"
        statlist = status.split(', ')
        new_Stats = dict(zip(statlist, new_Stat))
        self.stats = new_Stats
        print new_Stats
        return new_Stats


    def stats_to_iv(self):
        """ Calculates IVs based on stats.
            Returns a dict of statname->statIV."""
        level = self.level
        name = self.name
        base = dex.dex[int(nameList.name[name])]
        base = [int(i) for i in base]
        ev = self.evL
        nat = nature.natures[self.nature]
        
        this_stats = self.statsL
        
        # the boosted stat
        this_stats[nat[0]-1] /= 0.9
        this_stats[nat[0]-1] = math.ceil(this_stats[nat[0]-1])
        # the lowered stat
        this_stats[nat[1]-1] /= 1.1
        this_stats[nat[1]-1] = math.ceil(this_stats[nat[1]-1])
        
        # print self.statsL
        # print this_stats
        # print base
        
        new_HP = hpiv_calc(this_stats[0], base[0], ev[0], level)
        new_Atk = iv_calc(this_stats[1], base[1], ev[1], level)
        new_Def = iv_calc(this_stats[2], base[2], ev[2], level)
        new_Spe = iv_calc(this_stats[5], base[5], ev[3], level)
        new_SpA = iv_calc(this_stats[3], base[3], ev[4], level)
        new_SpD = iv_calc(this_stats[4], base[4], ev[5], level)

        new_IV = [new_HP, new_Atk, new_Def, new_SpA, new_SpD, new_Spe]
        status = "HP, Attack, Defense, Special Attack, Special Defense, Speed"
        statlist = status.split(', ')
        new_IV = dict(zip(statlist, new_IV))
        self.iv = new_IV
        print self.iv['HP']
        # print new_IV
        return new_IV


    def hpower_calc(self):
        """ Finds the hidden power type and power using the IVs. """
        try:
            a = int(self.iv["HP"])
            b = int(self.iv["Attack"])
            c = int(self.iv["Defense"])
            d = int(self.iv["Speed"])
            e = int(self.iv["Special Attack"])
            f = int(self.iv["Special Defense"])
        except TypeError:
            # ivs have not yet been calculated
            self.iv = self.stats_to_iv()
            a = int(self.iv["HP"])
            b = int(self.iv["Attack"])
            c = int(self.iv["Defense"])
            d = int(self.iv["Speed"])
            e = int(self.iv["Special Attack"])
            f = int(self.iv["Special Defense"])
            
        # takes the least significant bit of each stat
        # same as if odd then 1; if even then 0
        HPtype = math.floor((((a % 2) + (2*(b % 2)) + (4*(c % 2))
                            + (8*(d % 2)) + (16*(e % 2)) + (32*(f % 2)))*15.0)
                            / 63.0)

        # finds if the number has a remainder of 2 or 3 when divided by 4
        HPpower = (((((a >> 1) & 1) + 2*((b >> 1) & 1)
                   + 4*((c >> 1) & 1) + 8*((d >> 1) & 1)
                   + 16*((e >> 1) & 1) + 32*((f >> 1) & 1))*40)
                   / 63)+30

        self.hidden_power['type'] = HPtype
        self.hidden_power['power'] = HPpower
        print "Type: %d Power: %d" % (HPtype, HPpower)
        print HPtype
        print HPpower

        
# example
s = Pokemon("skarmory", level=21, nature="hasty", statsL=[64,43,61,28,40,44])
s.stats_to_iv()
s.hpower_calc()

print s.iv