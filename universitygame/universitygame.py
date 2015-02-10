class Die:

    types = {}
    types['admin'] = ['S', 'M', 'F', 'R', 'P', '']

    def __init__(self, Type):
        try:
            self.outcomes = self.types[Type]
        except:
            print "Type %s NOT defined" % Type

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


class School:

    types = {}
    types['admin'] = (None, None, None, None)
    types['lingue'] = (3, 1, 3, 4)

    def __init__(self, name, cost=0, staff=0, stud=0, keep=0):
        self.name = name
        self.cost = cost

        if name in self.types:
            (self.cost, self.staff, self.stud, self.keep) = self.types[name]
        else:
            (self.cost, self.staff, self.stud, self.keep) = (cost, staff, stud, keep)

    def __str__(self):
        out = self.name
        out += "Avviamento: " + str(self.cost) + '\n'
        out += "Staff: " + str(self.staff) + '\n'
        out += "Min Stud: " + str(self.stud) + '\n'
        out += "Mantenimento: " + str(self.keep)

        return out

    def canIbuildThis(self, staff, stud, avv):

#        return (staff >= self.staff and stud >= self.minStud and avv >= self.avv)
        return (staff >= self.staff, avv >= self.avv)

print School('cia')
print School('admin')
print School('lingue')