import pandas as pd


authors = pd.read_csv("authors_final.txt", lineterminator="\n", header=None)
papers = pd.read_csv("papers_final.txt", lineterminator="\n", header=None)

def strp(s): 
    return s.replace("[", "").replace("]",'')
    
with open('paper_as_edge.txt', 'w') as f:
    for item in list(map(strp, papers[8])):
        f.write("%s\n" % item)