from squirrel import Squirrel
from acorn import Acorn
from copy import deepcopy
import json

if __name__ == "__main__":
    squirrels = {}
    acorns = []
    
    selection = 0
    name = ""
    EXIT = 9
    while selection != EXIT:
        print "Enter your selection:"
        print "1. Squirrel login"
        print "2. Hide Acorn"
        print "3. Retrieve Acorn"
        print "4. Write squirrels to file"
        print "5. Write acorns to file"
        print "9. Exit"
        while selection < 1 or (selection > 5 and selection != EXIT):
            selection = input (name + "> ")
            
        if selection == 1:
            print "Squirrel login..."
            squirrel = Squirrel()
            name = squirrel.make_name()
            if name in squirrels:
                squirrel = squirrels[name]
                print "Returning squirrel has acorns at:"
                for acorn in squirrel.acorns:
                    acorn.show()
                print "Ready to retrieve or add new acorns..."
            else:
                squirrels[name] = squirrel
                print "New squirrel.  Ready to add new acorns..."
        elif selection == 2:
            print "Hide acorn..."
            new_acorn = Acorn()
            print name
            new_acorn.set_owner(name)
            squirrel.hide_acorn(new_acorn)
            acorns.append(new_acorn)
        elif selection == 3:
            print "Retrieve acorn..."
            success, target_acorn = squirrel.retrieve_acorn()
            if success:
                print "Acorn successfully retrieved. Updated list."
                i_acorn = 0
                for acorn in acorns:
                    if acorn == squirrel.acorns[target_acorn]:
                        del acorns[i_acorn]
                    i_acorn = i_acorn + 1
                del squirrel.acorns[target_acorn]
            else:
                print "You do not have an acorn like that."
                print "Do you want to steal one?"
                print "1. Steal"
                print "2. Don't steal"
                steal = 0
                while steal < 1 or steal > 2:
                    steal = input (name + "> ")
                if steal == 1:
                    print "Choose a squirrel to steal from:"
                    squirrel_list = target_acorn.list_squirrels(acorns)
                    if len(squirrel_list) > 0:
                        for i_squirrel in range(len(squirrel_list)):
                            print str(i_squirrel+1) + ". " + squirrel_list[i_squirrel]
                        selection = 0
                        while selection < 1 or selection > len(squirrel_list):
                            selection = input(name + '> ')
                        winner = squirrel.fight(squirrels[squirrel_list[selection - 1]])
                        if winner == squirrel:
                            print "Successfully stolen!"
                            winner.swap_acorn(squirrels[squirrel_list[selection - 1]],target_acorn)
                            old_name = squirrels[squirrel_list[selection - 1]].make_name()
                            if squirrels[squirrel_list[selection - 1]].traits['tail'] == 'bushy':
                                squirrels[squirrel_list[selection - 1]].traits['tail'] = 'long'
                            elif squirrels[squirrel_list[selection - 1]].traits['tail'] == 'long':
                                squirrels[squirrel_list[selection - 1]].traits['tail'] = 'short'
                            elif squirrels[squirrel_list[selection - 1]].traits['tail'] == 'short':
                                if squirrels[squirrel_list[selection - 1]].traits['ears'] == 'pointed':
                                    squirrels[squirrel_list[selection - 1]].traits['ears'] = 'rounded'
                            new_name = squirrels[squirrel_list[selection - 1]].make_name()
                        elif winner == squirrels[squirrel_list[selection - 1]]:
                            print "You failed to steal the acorn."
                            winner.swap_acorn(squirrel,target_acorn)
                            old_name = squirrel.make_name()
                            if squirrel.traits['tail'] == 'bushy':
                                squirrel.traits['tail'] = 'long'
                            elif squirrel.traits['tail'] == 'long':
                                squirrel.traits['tail'] = 'short'
                            elif squirrel.traits['tail'] == 'short':
                                if squirrel.traits['ears'] == 'pointed':
                                    squirrel.traits['ears'] = 'rounded'
                            new_name = squirrel.make_name()
                        if old_name != new_name:
                            if new_name in squirrels:
                                # Compare acorns
                                if len(squirrels[new_name].acorns) > len(squirrels[old_name].acorns):
                                    squirrels[new_name].acorns.append(squirrels[old_name].acorns)
                                    for acorn in acorns:
                                        acorn.update(new_name, old_name)
                                else:
                                    squirrels[old_name].acorns.append(squirrels[new_name].acorns)
                                    for acorn in acorns:
                                        acorn.update(old_name, new_name)
                            else:
                                # Add squirrel with new name
                                squirrels[new_name] = deepcopy(squirrels[old_name])
                                # Remove squirel with old name
                                del squirrels[old_name]
                                # Update acorn link to squirrels
                                for acorn in acorns:
                                    acorn.update(new_name, old_name)
                    else:
                        print "There are no squirrels with an acorn of that type." # Doesn't hit this

        elif selection == 4:
            print "Write squirrels to file..."
            squirrel_dict = {}
            for key in squirrels:
                acorn_list = []
                squirrel_dict[key] = deepcopy(squirrels[key].__dict__)
                for acorn in squirrels[key].acorns:
                    acorn_list.append([acorn.traits, acorn.location, acorn.squirrel_owner])
                squirrel_dict[key]['acorns'] = acorn_list
            with open('/home/squirrel/squirrels.json', 'w') as outfile:
                json.dump(squirrel_dict, outfile)

        elif selection == 5:
            print "Write acorns to file..."
            acorn_list = []
            for acorn in acorns:
                acorn_list.append([acorn.traits, acorn.location, acorn.squirrel_owner])
            with open('/home/squirrel/acorns.json', 'w') as outfile:
                json.dump(acorn_list, outfile)
            
        if selection != EXIT:
            selection = 0
