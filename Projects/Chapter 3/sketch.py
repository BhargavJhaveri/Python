import os
os.chdir('/Users/bhargav/WorkSpace/TestProjects/Python/HeadFirst/Projects/Chapter 3/TextFiles')

data = open('sketch.txt')

for each_statement in data:

        try:
                (role, statement) = each_statement.split(':',1)

                print(role, end = '')
                print(' said: ' , end = '')
                print(statement, end = '')
        except:
                pass

data.close()
