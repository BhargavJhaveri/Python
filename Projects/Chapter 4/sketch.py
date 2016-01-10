import os
import bhargav_mac_nester

os.chdir('/Users/bhargav/WorkSpace/TestProjects/Python/HeadFirst/Projects/Chapter 4/TextFiles')

man = []
other = []

try:
        data = open('sketch.txt')

        for each_statement in data:

                try:
                        (role, statement) = each_statement.split(':',1)
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
        with open('man_speech.txt','w') as man_file:
                bhargav_mac_nester.print_lol(man, fh=man_file)
        with open('other_man_speech.txt','w') as other_man_file:
                bhargav_mac_nester.print_lol(other, fh=other_man_file)

except IOError as err:
        print('File read/write error. \n' + str(err))
except ValueError as valErr:
        print('ValueError occurred! \n' + str(valErr))
        """
finally:
        if 'man_file' in locals():
                man_file.close()
        if 'other_man_file' in locals():
                other_man_file.close()
                """
