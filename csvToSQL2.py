import csv
import sqlite3
# TODO Allow the entry of the .csv filename by a user manually - including errors for
    # a.) wrong file extension
    # b.) files that are not in the current directory
# TODO Make the name of the table the same as the original CSV - so in this case, everything called "ReaearchData"
researchData = open('researchData.csv')
csvfile = csv.reader(researchData, delimiter = ',')

connect = sqlite3.connect('researchData.sqlite')
cur = connect.cursor()
cur.execute('''DROP TABLE IF EXISTS ResearchData ''')

count = 0
num = 1
headers = " \""
values_ = ""
insertValues = ""
for line in csvfile:
    while num == 1:
        while count < len(line)-1:
            item = line[count]
            if item == "":
                item = "column_"+str(count+1)
            else:
                pass
            headers = headers + item + "\", \""
            values_ = values_ + " ?,"
            insertValues = insertValues + "line["+str(count)+"], "
            count += 1
        while count < len(line):
            item = line[count]
            if item == "":
                item = "column_"+str(count+1)
            else:
                pass
            headers = headers + item + "\""
            values_ = values_ + " ?"
            insertValues = insertValues + "line["+str(count)+"]"
            count += 1
        num += 1
        cur.execute("CREATE TABLE ResearchData ("+headers+");")
    # print num
    # print len(line)
    # print headers
    # print values_
    # print insertValues
print line[0]
execution = "INSERT OR IGNORE INTO ResearchData ("+headers+") VALUES ("+values_+"),  ( "+insertValues+"))"
print execution
print cur.execute(execution)

#     cur.execute(execution)

#     cur.execute('''INSERT OR IGNORE INTO ResearchData (column_1 , A1 , A2 , A3 , A4 , A5 , C1 , C2 , C3 , C4 , C5 , E1 , E2 , E3 , E4 , E5 , N1 , N2 , N3 , N4 , N5 , O1 , O2 , O3 , O4 , O5 , gender , education , age) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', ( line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17], line[18], line[19], line[20], line[21], line[22], line[23], line[24], line[25], line[26], line[27], line[28]))
# connect.commit()
# connect.commit()
# cur.close()
# print "... task complete"
