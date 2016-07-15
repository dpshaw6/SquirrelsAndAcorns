

class Acorn:
    
    acorn_traits = \
        {'appearance':['smooth','rough'], \
        'odor':['sweet','savory']}

    def __init__(self):
        self.traits = {}
        for trait, options in self.acorn_traits.iteritems():
            print("Enter the %s of the acorn" % trait)
            for i_option in range(len(options)):
                print str(i_option+1) + ". " + self.acorn_traits[trait][i_option]
            selection = 0
            while selection < 1 or selection > len(options):
                selection = input('> ')
            self.traits[trait] = self.acorn_traits[trait][selection - 1]
            
        self.location = ()
        self.squirrel_owner = ""
        
    def show(self):
        print "Acorn Description:"
        for trait, value in self.traits.iteritems():
            print (" - " + trait + ": " + value)
        print (" - location: " + str(self.location))
        print (" - belongs to: " + self.squirrel_owner)
        
    def update(self, new_owner, old_owner):
        if self.squirrel_owner == old_owner:
            self.squirrel_owner = new_owner
        
    def set_owner(self, name):
        self.squirrel_owner = name
        
    def set_location(self, location):
        self.location = location
        
    def list_squirrels(self, acorns):
        name_list = []
        for acorn in acorns:
            found = True
            for trait, value in self.traits.iteritems():
                if value != acorn.traits[trait]:
                    found = False
            if found:
                name_list.append(acorn.squirrel_owner)
        return name_list
                