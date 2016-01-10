import os
import bhargav_mac_nester
import pickle

os.chdir('/Users/bhargav/WorkSpace/TestProjects/Python/HeadFirst/Projects/Chapter 4/TextFiles')

new_man = []
man = []
other = []

try:
    data = open('sketch.txt')

    for each_statement in data:

        try:
            (role, statement) = each_statement.split(':', 1)
            statement = statement.strip()
            if role == 'Man':
                man.append(statement)
            elif role == 'Other Man':
                other.append(statement)

        except ValueError:
            pass

    data.close()
except IOError as ioErr:
    print('IO Error' + str(ioErr))

try:
    with open('new_man_data.txt', 'wb') as new_man_file, open('new_other_man_data.txt', 'wb') as new_other_man_file:
        pickle.dump(man, new_man_file)
        pickle.dump(other, new_other_man_file)

except IOError as ioErr:
    print('IO Error' + str(ioErr))

except pickle.PickleError as pickleError:
    print('Pickle Error occurred: ' + str(pickleError))

try:
    with open('new_man_data.txt','rb') as new_man_file:
        bhargav_mac_nester.print_lol(pickle.load(new_man_file))
except IOError as ioErr:
    print('IO Error' + str(ioErr))
except pickle.PickleError as pickleError:
    print('Pickle Error' + str(pickleError))
