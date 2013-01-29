import re
inFile = open('ERR0498-04-05.soft')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    s = re.search('(\d+)S',fields[5])
    if s:
        if int(s.group(1))>5:
            print(line)

inFile.close()
