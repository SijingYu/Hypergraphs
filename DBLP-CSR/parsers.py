import csv
import re
import sys

# save_format: 1--".cvs", 2--".txt", else--not save

def affiliation_parser(file_name = 'raw-data/DBLP-CSR/affiliation.txt',
    save_format = 1, save_name='affiliation'):

    affiliation_str = open(file_name, "r").read()
    entries = affiliation_str.split("),(")
    arr = []

    for i, entry in enumerate(entries):
        col = []
        id = re.search("\d+", entry)[0]
        year = int(entry[-4:])
        info = entry[len(id)+1:][:-5].split('\',\'')
        col.append(int(id))
        col.append(info[0].replace("\'",""))
        col.append(info[1].replace("\'",""))
        pos = info[2].find("\\n")
        if pos == -1:
            col.append(info[2].replace("\'",""))
            col.append("-")
        else:
            col.append(info[2][:pos].replace("\'",""))
            col.append(info[2][(pos+2):].replace("\'",""))
        col.append(year)
        arr.append(col)

    if save_format == 1:
        with open("parsed_"+save_name+".txt", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)
    elif save_format == 2:
        with open("parsed_"+save_name+".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)

    return arr
    

def affiliation_coord_parser(file_name = 'raw-data/DBLP-CSR/affiliation_coord.txt',
    save_format = 1, save_name='affiliation_coord'):

    affiliation_coord_str = open(file_name, "r").read()
    entries = affiliation_coord_str.split("),(")
    affiliation = affiliation_parser(save_format=0)
    arr = [[0]*9]*len(affiliation)

    for i, entry in enumerate(entries):
        col = []
        id = re.search("\d+", entry)[0]
        year = re.findall(",\d{4},",entry)[0][1:5]
        latitude = re.findall('\d{1,3}.\d{7}', entry)[0]
        longtitude = re.findall('\d{1,3}.\d{7}', entry)[1]
        if entry[entry.find(latitude)-1]=='-':
            latitude = "-"+latitude
        if entry[entry.find(longtitude)-1]=='-':
            longtitude = "-"+longtitude
        others = entry.replace(id+",","").replace(","+year,"").replace(","+latitude+","+longtitude,"").split("\',\'")
        
        col.append(int(id))
        col.append(int(year))
        col.append(latitude)
        col.append(longtitude)
        for other in others:
            col.append(other.replace("\'","").replace("\\r",""))

        arr[int(id)-1]=col

    if save_format == 1:
        with open("parsed_"+save_name+".txt", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)
    elif save_format == 2:
        with open("parsed_"+save_name+".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)

    return arr


def authors_gender_parser(file_name = 'raw-data/DBLP-CSR/authors_gender.txt',
    save_format = 1, save_name='authors_gender'):

    authors_gender_str = open(file_name, "r").read()
    entries = authors_gender_str.split("),(")
    arr = [[0]*3]*len(entries)

    for i, entry in enumerate(entries):
        col = []
        info = entry.split(',')
        name = info[0].replace("\'","")
        gender = info[1].replace("\'","")
        prob = float(re.search('[.\d]+',info[2])[0].replace("\'",""))
        for item in [name, gender, prob]:
            col.append(item)
        arr[i]=col

    if save_format == 1:
        with open("parsed_"+save_name+".txt", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)
    elif save_format == 2:
        with open("parsed_"+save_name+".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)

    return arr


def authors_parser(file_name = 'raw-data/DBLP-CSR/authors.txt',
    save_format = 1, save_name='authors'):

    authors_str = open(file_name, "r").read()
    entries = authors_str.split("),(")
    arr = [[0]*6]*len(entries)

    for i, entry in enumerate(entries):
        col = []
        info = entry.split(',')
        id = int(re.search('\d+',info[0])[0])
        key = info[1].replace("\'","")
        pos = int(info[2])
        name = info[3].replace("\'","")
        gender = info[4].replace("\'","")
        prob = float(re.search('[.\d]+',info[5])[0].replace("\'",""))
        for item in [id, key, pos, name, gender, prob]:
            col.append(item)
        arr[id-1]=col

    if save_format == 1:
        with open("parsed_"+save_name+".txt", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)
    elif save_format == 2:
        with open("parsed_"+save_name+".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)

    return arr


def main_parser(file_name = 'raw-data/DBLP-CSR/main.txt',
    save_format = 1, save_name='main'):

    main_str = open(file_name, "r").read()
    entries = main_str.split("),(")
    arr=[]

    for i, entry in enumerate(entries):
        col = []
        info = entry.split(',')    
        key = info[0].replace("\'","")
        year = int(info[1])
        conf = info[2].replace("\'","")
        crossref = info[3].replace("\'","")
        cs_de_se_th = 0
        for i in range(4,8):
            if info[i]=="1":
                cs_de_se_th = i-4
        publisher = info[8].replace("\'","")
        link = info[9].replace("\'","")
        for j in [key,year,conf,crossref,cs_de_se_th,publisher,link]:
            col.append(j)
        arr.append(col)
    
    if save_format == 1:
        with open("parsed_"+save_name+".txt", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)
    elif save_format == 2:
        with open("parsed_"+save_name+".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(arr)

    return arr


'''if sys.argv[1] == "affiliation": 
    if len(sys.argv) > 2:
        if sys.argv[2] == ".csv":
            affiliation_parser(save_format=2)
        else:
            affiliation_parser()

elif sys.argv[1] == "affiliation_coord": 
    if len(sys.argv) > 2:
        if sys.argv[2] == ".csv":
            affiliation_coord_parser(save_format=2)
        else:
            affiliation_coord_parser()

elif sys.argv[1] == "authors_gender":
    if len(sys.argv) > 2:
        if sys.argv[2] == ".csv":
            authors_gender_parser(save_format=2)
        else:
            authors_gender_parser()

elif sys.argv[1] == "authors":
    if len(sys.argv) > 2:
        if sys.argv[2] == ".csv":
            authors_parser(save_format=2)
        else:
            authors_parser()

elif sys.argv[1] == "main":
    if len(sys.argv) > 2:
        if sys.argv[2] == ".csv":
            main_parser(save_format=2)
        else:
            main_parser()'''


def main():
    pass

if __name__ == "__main__":
    format = 1

    if len(sys.argv) > 1 and sys.argv[1]  == 'csv':
            format = 2
            
    affiliation_parser(save_format=format)
    affiliation_coord_parser(save_format=format)
    authors_gender_parser(save_format=format)
    authors_parser(save_format=format)
    main_parser(save_format=format)