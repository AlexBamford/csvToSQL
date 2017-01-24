import csv
import sqlite3

researchData = open('researchData.csv')
file = csv.reader(researchData, delimiter = ',')

connect = sqlite3.connect('researchData.sqlite')
cur = connect.cursor()
cur.execute('''DROP TABLE IF EXISTS ResearchData ''')


headersList = list()
count = 0
headers = ""
num = 0
for line in file:
    # while count == 0:
    #     print line
    #     count += 1
    while count < len(line)-1:
        item = line[count]
        if item == "":
            item = "column_"+str(count+1)
        else:
            pass
        headers = headers + item + " , "
        count += 1
        headersList.append(item)
    while count < len(line):
        item = line[count]
        if item == "":
            item = "column_"+str(count+1)
        else:
            pass
        headers = headers + item
        count += 1
        headersList.append(item)
    num += 1
    if num == 1:
        break
print num
print len(line)
print headers
print headersList
cur.execute("CREATE TABLE ResearchData ("+headers+");")
count3 = 0
for line in file:
    insertValues = ""
    while count3 <= len(line):
        insertValues = insertValues + "line["+str(count3)+"], "
        print insertValues
        count3 += 1
    cur.execute('''INSERT OR IGNORE INTO ResearchData (Column_1 , A1 , A2 , A3 , A4 , A5 , C1 , C2 , C3 , C4 , C5 , E1 , E2 , E3 , E4 , E5 , N1 , N2 , N3 , N4 , N5 , O1 , O2 , O3 , O4 , O5 , gender , education , age)
    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', ( line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17], line[18], line[19], line[20], line[21], line[22], line[23], line[24], line[25], line[26], line[27], line[28]))
connect.commit()
cur.close()
print "... task complete"
