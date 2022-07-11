import pandas as pd
import re

# returns a dictionary storing id-name pairs of everyone in the senate or the house
def combine_SH_senate_house():
    house = pd.read_csv('house.csv')
    senate = pd.read_csv('senate.csv')
    SH = pd.read_csv('SH.csv')

    SH_keys = SH.groupby('ids').groups.keys()
    house_keys = house.groupby('id').groups.keys()
    senate_keys = senate.groupby('id').groups.keys()

    SH = SH.drop(list(SH.columns)[4:], axis=1)
    id_name = { } # dictionary storing id-name pair from the SH file
    for id, group in SH.groupby('ids'):
        name = max(group["labels"], key = len)
        id_name[id] = name

    if not set(list(house_keys)).issubset(set(list(SH_keys))):
        print("There are house keys not included in the SH keys.")
        for id, group in house.groupby('id'):
            name = max(group["name"], key = len)
            if not id in id_name.keys():
                id_name[id] = name

    if not set(list(senate_keys)).issubset(set(list(SH_keys))):
        print("There are senate keys not included in the SH keys.")
        for id, group in senate.groupby('id'):
            name = max(group["name"], key = len)
            if not id in id_name.keys():
                id_name[id] = name
    return id_name

# change the original id of each one to numbers starting from 0 for the purpose of 
# constructing hypergraph, returns the dictionary storing id-name pair with updated id
def change_index(id_name, save_file = False, file_name = "id-name.txt"):
    ids = list(id_name.keys())
    ids.sort()
    id_name_updated_index = {}
    old_id_to_new_id = {}

    for index, id in enumerate(ids):
        id_name_updated_index[index] = id_name[id]
        old_id_to_new_id[id] = index
    
    if save_file:
        with open(file_name, 'w') as f:
            for key, value in id_name_updated_index.items():
                f.write(str(key) + ": " + value + "; " + "original id: " + str(ids[key]))
                f.write('\n')

    return id_name_updated_index, old_id_to_new_id

def hypergraph_generator(save_file = False, file_name = "hypergraph.txt"):
    id_name = combine_SH_senate_house()
    id_name_updated_index, old_id_to_new_id = change_index(id_name, save_file = False, file_name = "id-name.txt")
    sponsor_file = open('sponsors.txt', 'r')
    cosponsor_file = open('cosponsors.txt', 'r')
    count = 0
    all_sponsors = [[0]]*283994

    while True:
        sponsor_line = sponsor_file.readline()
        cosponsor_line = cosponsor_file.readline()

        if not sponsor_line:
            break

        all_sponsors[count][0]=list(map(int, re.findall("\d+", sponsor_line)))
        cosponsors = []

        if not "NA" in cosponsor_line:
            cosponsors = list(map(int, re.findall("\d+", cosponsor_line)))

        all_sponsors[count] =  all_sponsors[count][0] + cosponsors
        count += 1
    
    if save_file:
        with open(file_name, 'w') as f:
            for index, sponsor_line in enumerate(all_sponsors):
                for index2, sponsor in enumerate(sponsor_line):
                    f.write(str(sponsor))
                    if sponsor != sponsor_line[-1]:
                        f.write(" ,")
                    else:
                        f.write('\n')

    return all_sponsors


def main():
    hypergraph_generator()