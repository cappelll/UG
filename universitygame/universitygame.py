import random

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


class Die:

    lockSymbol = 'P'

    types = {}
    types['admin'] = ['S', 'M', 'F', 'R', 'P', '_']
    types['lingue'] = ['S', 'M', 'F', 'R', 'P', 'G']
    types['legge'] = ['S', 'M', 'F', 'R', 'P', 'G']
    types['scienze'] = ['S', 'M', 'F', 'J', 'P', 'G']
    types['economia'] = ['S', 'M', 'F', 'J', 'P', 'G']
    types['medicina'] = ['S', 'M', 'F', 'G', 'P', 'G']
    types['ingegneria'] = ['S', 'M', 'F', 'G', 'P', 'G']

    def __init__(self, name):
        try:
            self.name = name
            self.outcomes = self.types[name]
            self.actualState = None
        except:
            print "Type %s NOT defined" % name

    def __str__(self):
        return '-'.join(self.outcomes)

    def roll(self, force=False):

        if self.actualState is self.lockSymbol and force is False:
            out = 'P'

        else:
            out = random.choice(self.outcomes)

            self.actualState = out

        return out


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

class School:

    types = {}
    types['admin'] = (None, None, None, None)

    types['lingue'] = (3, 1, 3, 4)
    types['legge'] = (5, 1, 5, 4)
    types['scienze'] = (5, 2, 5, 7)
    types['economia'] = (7, 2, 9, 7)
    types['medicina'] = (7, 3, 7, 10)
    types['ingegneria'] = (9, 3, 13, 10)

    def __init__(self, name, cost=0, staff=0, stud=0, keep=0):
        self.name = name
        self.cost = cost

        if name in self.types:
            (self.cost, self.staff, self.stud, self.keep) = self.types[name]
        else:
            (self.cost, self.staff, self.stud, self.keep) = (cost, staff, stud, keep)

        self.die = Die(self.name)

    def __str__(self):
        out = self.name + '\n'
        out += "\tAvviamento: " + str(self.cost) + '\n'
        out += "\tStaff: " + str(self.staff) + '\n'
        out += "\tMin Stud: " + str(self.stud) + '\n'
        out += "\tMantenimento: " + str(self.keep) + '\n'
        out += "\tDie" + self.die.__str__()

        return out


    def canIbuildThis(self, staff, stud, avv):

#        return (staff >= self.staff and stud >= self.minStud and avv >= self.avv)
        return (staff >= self.staff, avv >= self.avv)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


class College:

    lockSymbol = 'P'

    def __init__(self, N=3):

        self.dice = []
        self.reroll = 3
        self.money = 3
        self.stud = 0
        self.vp = 0
        self.staff = 0
        self.problem = 0

        for n in range(N):
            self.dice.append(Die('admin'))

    def __str__(self):

        out = ''

        return out

    def Roll(self):

        results = []

        for die in self.dice:
            results.append(die.roll())

        return results

    def MultiRoll(self, NRR):

        for i in xrange(min(NRR, self.reroll)):
            self.reroll -= 1
            results = self.Roll()

            if set(results) is set(self.lockSymbol):
                break

            print '-'.join(results)

        return results

    def AddDie(self, die):

        if isinstance(die, Die):
            self.dice.append(die)
        elif isinstance(die, str):
            self.dice.append(Die(die))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

if __name__ == "__main__":

    sLingue = School('lingue')
    dLingue = sLingue.die

    tcd = College()

    tcd.AddDie(dLingue)
    tcd.AddDie("medicina")

    print sLingue

    tcd.MultiRoll(2)


    print tcd

"""
    print School('legge')
    print School('scienze')
    print School('economia')
    print School('medicina')
    print School('ingegneria')
"""