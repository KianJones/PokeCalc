# HP calc

import math
from dex import dex, nameList, nature


def quit():
    print 'error'
    exit(0)


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
    def __init__(self, name, level, nature, statsL=[], iv=[], ev=[]):
        # I can split this on , so that I don't have to type it repeatedly
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

        # checks if the list of stats/ev/iv was given
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
    a = (100*(stat-5))/level
    b = -(2*base)-(ev/4)
    return a+b+1


def hpiv_calc(hp, base, ev, level):
    """ Returns the calculated HP IV. """
    a = (100*(hp-10))/level
    b = -100 - (ev/4) - (2*base)
    return a+b+1


def iv_to_stats(poke):
    """ Calculates stats at given level based on IV.
        Returns dictionary of statname->statvalue. """
    level = poke.level
    name = poke.name
    base = dex.dex[int(nameList.name[name])]
    base = [int(i) for i in base]
    ev = poke.evL
    nat = nature.natures[poke.nature]

    new_HP = hpstat_calc(poke.iv["HP"], base[0], ev[0], level)
    new_Atk = stat_calc(poke.iv["Attack"], base[1], ev[1], level)
    new_Def = stat_calc(poke.iv["Defense"], base[2], ev[2], level)
    new_Spe = stat_calc(poke.iv["Speed"], base[5], ev[3], level)
    new_SpA = stat_calc(poke.iv["Special Attack"], base[3], ev[4], level)
    new_SpD = stat_calc(poke.iv["Special Defense"], base[4], ev[5], level)

    new_Stat = [new_HP, new_Atk, new_Def, new_SpA, new_SpD, new_Spe]
    new_Stat = [math.floor(i) for i in new_Stat]
    new_Stat[nat[0]-1] *= 0.9
    new_Stat[nat[1]-1] *= 1.1

    status = "HP, Attack, Defense, Special Attack, Special Defense, Speed"
    statlist = status.split(', ')
    new_Stats = dict(zip(statlist, new_Stat))
    print new_Stats
    return new_Stats


def stats_to_iv(poke):
    """ Calculates IVs based on stats.
        Returns a dict of statname->statIV."""
    level = poke.level
    name = poke.name
    base = dex.dex[int(nameList.name[name])]
    base = [int(i) for i in base]
    ev = poke.evL

    new_HP = hpiv_calc(poke.stats["HP"], base[0], ev[0], level)
    new_Atk = iv_calc(poke.stats["Attack"], base[1], ev[1], level)
    new_Def = iv_calc(poke.stats["Defense"], base[2], ev[2], level)
    new_Spe = iv_calc(poke.stats["Speed"], base[5], ev[3], level)
    new_SpA = iv_calc(poke.stats["Special Attack"], base[3], ev[4], level)
    new_SpD = iv_calc(poke.stats["Special Defense"], base[4], ev[5], level)

    new_IV = [new_HP, new_Atk, new_Def, new_SpA, new_SpD, new_Spe]
    status = "HP, Attack, Defense, Special Attack, Special Defense, Speed"
    statlist = status.split(', ')
    new_IV = dict(zip(statlist, new_Stat))
    print new_IV
    return new_IV


def hpower_calc(mon):
    """ Finds the hidden power type and power. """
    a = int(mon.iv["HP"])
    b = int(mon.iv["Attack"])
    c = int(mon.iv["Defense"])
    d = int(mon.iv["Speed"])
    e = int(mon.iv["Special Attack"])
    f = int(mon.iv["Special Defense"])

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

    mon.hpType = HPtype
    mon.hpPower = HPpower
    print "Type: %d Power: %d" % (HPtype, HPpower)
    print HPtype
    print HPpower

#Pikachu = Pokemon("absol", statsL =[135,159,75,90,81,75], level = 50, ev = [255,255,255,255,255,255])
#Absol = Pokemon("absol", iv=[20,20,20,20,20,20], level = 50, ev=[0,0,0,0,0,0])
# For = Pokemon("forretress", level = 43, statsL=[121,94,114*(10.0/9),72*(10.0/11),57,41])
# ghost = Pokemon("haunter", level = 58, nature="brave",statsL=[127,69*(10.0/11),57,148,84,116*(10.0/9)], ev=[0,0,0,0,0,0])
ghost = Pokemon("haunter", level=58, nature="brave",
                iv=[12, 0, 0, 17, 27, 24], ev=[0, 0, 0, 0, 0, 0])
#getHP(Pikachu)
#getStatsfromIV(Absol)
#print Pikachu.stats
#getIVfromStats(ghost)
ghost.stats = iv_to_stats(ghost)
print ghost.stats
