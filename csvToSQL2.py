import csv
import sqlite3
# TODO Allow the entry of the .csv filename by a user manually - including errors for
    # a.) wrong file extension
    # b.) files that are not in the current directory
# TODO Make the name of the table the same as the original CSV - so in this case, everything called "ReaearchData"
print "starting"
researchData = open('researchData.csv')
csvfile = csv.reader(researchData, delimiter = ',')

connect = sqlite3.connect('researchData2.sqlite')
cur = connect.cursor()
cur.execute('''DROP TABLE IF EXISTS ResearchData2 ''')

count = 0
num = 1
headers = " \""
values_ = ""
for line in csvfile:
    if num == 1:
        while count < len(line)-1:
            item = line[count]
            print item
            if item == "":
                item = "column_"+str(count+1)
                count += 1
                headers = headers + item + "\", \""
                values_ = values_ + " ?,"
            else:
                pass
                headers = headers + item + "\", \""
                values_ = values_ + " ?,"
                count += 1
        while count == len(line)-1:
            item = line[count]
            print item
            if item == "":
                item = "column_"+str(count+1)
                count += 1
                headers = headers + item + "\""
                values_ = values_ + " ?"
            else:
                pass
                headers = headers + item + "\""
                values_ = values_ + " ?"
                count += 1
        num += 1
        print headers
        print values_
        print cur.execute("CREATE TABLE ResearchData2 ("+headers+");")
        executionFirstArg = "INSERT OR IGNORE INTO ResearchData2 ("+headers+") VALUES ("+values_+")"
        print executionFirstArg
    else:
        cur.execute(executionFirstArg, line)
connect.commit()
