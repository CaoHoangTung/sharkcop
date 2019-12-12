import sys
import os
import time

cur_path = os.getcwd()
sys.path.insert(1,cur_path)

from utils.Helper import Helper

f = open("%s/raw_data2.csv" % os.path.dirname(os.path.abspath(__file__)),"r",encoding="UTF-8")

rows = f.read().split("\n")
index = 1

def write_to_file(file_name, vector):
    data_f = open("%s/output/%s"% (os.path.dirname(os.path.abspath(__file__)),file_name),"a",encoding="UTF-8")
    data_f.write(vector)

begin = 858
for index in range(begin,len(rows)):
    row = rows[index]
    url = row.split(",")[0]
    label = int(row.split(",")[1])
    if label == 0:
        label = -1

    print(url)

    vector = [index]
    vector += Helper.embed_url(url)
    vector += [label]

    if (len(vector) != 32):
        write_to_file("logging.txt",str(index)+","+url+","+str(len(vector))+"\n")

    vector = [str(num) for num in vector]
    print(vector)
    write_to_file("data.csv",",".join(vector)+"\n")
    time.sleep(3)    
