# To get the all csv files from the mentioned path and its sub directories
import os, re, csv, time, itertools
import math
import pandas as pd

#print(time.time())
with open('Directorypath\\result.txt', 'w') as a:
    for path , subdirs, files in os.walk('Data directorypath\\data\\'):
        for filenames in files:
            if re.match("^.*.csv$", filenames):
                f = os.path.join(path,filenames)
                fn=f.rstrip('\r\n')
                a.write(str(fn))
                a.write('\n')
a.close()

paths = []

with open("Directorypath\\result.txt")as file:
    filecount = 0
    for line in file:
        line = line.rstrip()
        paths.append(line)
        filecount = filecount + 1
    print("File count is ", filecount)

    with open('Directorypath\\columns.txt', 'w') as cf:
        sumcolum = 0
        for singlefile in paths:
            #print(singlefile)
            exampleFile = open(singlefile, 'r', encoding="utf8", errors='ignore')
            reader = csv.reader(exampleFile)
            ncol = len(next(reader))  # Read first line and count columns
            sumcolum = sumcolum + ncol
            #print('File name is:', singlefile, ncol)
            cf.write(str(ncol))
            cf.write('\n')
            exampleFile.seek(0)
    print("Average no. of columns in all files:", math.ceil(sumcolum/filecount))
    cf.close()

    with open('Directorypath\\rows.txt', 'w') as rf:
        for singlefile in paths:
            exampleFile = open(singlefile, 'r', encoding="utf8", errors='ignore')

            df = pd.read_csv(exampleFile,error_bad_lines=False)

            words_count = df.count().sum()
            print(singlefile, words_count)

            rf.write(str(singlefile))
            #rf.write(str(words_count))
            #Need to check how to populate , after filename?
            rf.write(','.join(str(words_count)))
            rf.write('\n')
    rf.close()

    with open('Directorypath\\Total.txt', 'w') as tf:
        totalrowcount = 0
        for singlefile in paths:
            exampleFile = open(singlefile, 'r', encoding="utf8", errors='ignore')

            reader = csv.reader(exampleFile)
            row_count = sum(1 for row in reader)
            totalrowcount = totalrowcount + row_count
            #print(row_count)
        print("Total row count is ", totalrowcount-filecount)
            #tf.write('\n')
    tf.close()

print(time.time())
