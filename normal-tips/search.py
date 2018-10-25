import re
import os

for i in range(252):
    filename = str(i+1) + '.txt'
    line = open(filename, encoding="UTF-8").read()
    s = line.split('责编')[0]

    try:
        f = open(os.path.join("data/", filename), "w")
        f.write(s)
        f.close()
    except:
        f.close()
        os.remove(os.path.join("data/", filename))

