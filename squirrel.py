from acorn import Acorn


class Squirrel:
    
    squirrel_traits = \
    {'gender':['male','female'], \
    'tail':['long','short','bushy'], \
    'fur':['brown','gray','brindle'], \
    'ears':['pointed','rounded']}

    def __init__(self):
        self.traits = {}
        for trait, options in self.squirrel_traits.iteritems():
            print("Enter the %s of the squirrel" % trait)
            for i_option in range(len(options)):
                print str(i_option+1) + ". " + self.squirrel_traits[trait][i_option]
            selection = 0
            while selection < 1 or selection > len(options):
                selection = input('> ')
            self.traits[trait] = self.squirrel_traits[trait][selection - 1]
            
        self.acorns = []
        self.show()
        
    def show(self):
        print "Squirrel Description: " 
        for trait, value in self.traits.iteritems():
            print (" - " + trait + ": " + value)
        print (" - acorns: " + str(self.acorns))
        
    def hide_acorn(self, acorn):
        street = 0
        avenue = 0
        while street < 59 or street > 110:
            street = input ("Enter street (between 59th and 110th, inclusive) > ")
        while avenue < 5 or avenue > 8:
            avenue = input ("Enter avenue (between 5th and 8th, inclusive) > ")
        acorn.set_location((street, avenue))
        self.acorns.append(acorn)
        
    def retrieve_acorn(self):
        print "Enter the characteristics of the acorn you are looking for..."
        target_acorn = Acorn()
        i_acorn = 0
        for acorn in self.acorns:
            found = True
            for trait, value in target_acorn.traits.iteritems():
                if value != acorn.traits[trait]:
                    found = False
            if found:
                print "Acorn found!"
                acorn.show()
                return True, i_acorn
            i_acorn = i_acorn + 1
        return False, target_acorn
    
    def swap_acorn(self, other_squirrel, swap):
        i_acorn = 0
        for acorn in other_squirrel.acorns:
            found = True
            for trait, value in acorn.traits.iteritems():
                if value != swap.traits[trait]:
                    found = False
            if found:
                acorn.set_owner(self.make_name())
                self.acorns.append(acorn)
                del other_squirrel.acorns[i_acorn]
                break
            i_acorn = i_acorn + 1                
    
    def make_name(self):
        name = "-".join(['%s' % v for k,v in self.traits.iteritems()])
        return name
    
    def fight(self, opponent):
        if self.traits['tail'] == opponent.traits['tail'] and \
        self.traits['ears'] == opponent.traits['ears']:
            return self # Tie goes to the aggressor
        elif self.traits['tail'] == 'bushy':
            return self
        elif opponent.traits['tail'] == 'bushy':
            return opponent
        elif self.traits['tail'] == 'long' and opponent.traits['tail'] == 'short':
            return self
        elif self.traits['tail'] == 'short' and opponent.traits['tail'] == 'long':
            return opponent
        elif self.traits['ears'] == 'pointed':
            return self
        elif opponent.traits['ears'] == 'pointed':
            return opponent
        else:
            return 'Error in fight'
                