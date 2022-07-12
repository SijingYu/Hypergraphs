import pandas as pd
import re

# returns a dictionary storing id-name pairs of everyone in the senate or the house
def combine_SH_senate_house():
    house = pd.read_csv('raw-data/Legislative-Cosponsorship/house.csv')
    senate = pd.read_csv('raw-data/Legislative-Cosponsorship/senate.csv')
    SH = pd.read_csv('raw-data/Legislative-Cosponsorship/SH.csv')

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
        print("There's not much need in cleaning this data. Instead, unifying the id (which is a number) for each author is needed. Therefore, the parser generates the reference file for it.")

    return id_name_updated_index, old_id_to_new_id

def main():
    pass

if __name__ == "__main__":
   change_index(combine_SH_senate_house(),save_file=True)