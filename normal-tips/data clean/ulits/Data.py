import csv

def read_csv(path):
    dict_id = {}
    dict_mesg = {}
    reader = []
    csv_reader = csv.reader(open(path, encoding='utf-8'))
    for row in csv_reader:
        reader.append(row)
    list_id = reader[0]
    del reader[0]
    for mesg in  reader:
        for i in range(len(list_id)-1):
            dict_mesg[list_id[i + 1]] = mesg[i + 1]
        dict_id[mesg[0]] = dict_mesg
        dict_mesg = {}

    return dict_id
