import parsers
import re

def hypergraph_generator(save_file = True, file_name = "bill_as_hyperedge.txt"):
    #id_name = parsers.combine_SH_senate_house()
    #id_name_updated_index, old_id_to_new_id = parsers.change_index(id_name, save_file = False, file_name = "id-name.txt")
    sponsor_file = open('raw-data/Legislative-Cosponsorship/sponsors.txt', 'r')
    cosponsor_file = open('raw-data/Legislative-Cosponsorship/cosponsors.txt', 'r')
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
    pass

if __name__ == "__main__":
   hypergraph_generator()