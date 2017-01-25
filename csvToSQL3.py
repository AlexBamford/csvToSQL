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

headers = []
values_questionmarks = []

headers_string = ""
values_questionmarks_string = ""

for row, line in enumerate(csvfile):
    if row == 0:
        for column_num, item in enumerate(line):
            if item == "":
                item = "column_%d" % column_num
            headers.append(item)
            values_questionmarks.append("?")
        headers_string = ", ".join(headers)
        values_questionmarks_string = ", ".join(values_questionmarks)

        print headers_string
        print values_questionmarks_string

        cur.execute("CREATE TABLE ResearchData ("+headers_string+");")
        executionTemplate = "INSERT OR IGNORE INTO ResearchData (%s) VALUES (%s);" % (headers_string, values_questionmarks_string)

        print executionTemplate
    else:
        cur.execute(executionTemplate, line)
        connect.commit()
