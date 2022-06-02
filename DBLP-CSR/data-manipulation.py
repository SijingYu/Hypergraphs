
import pandas as pd

# combine affiliation_coord with affiliation with unified paper id
def combine_affiliation(save = True, save_name = "affiliation_complete"):
    affiliation_df = pd.read_csv('cleaned-data/DBLP-CSR/affiliation.txt', lineterminator="\r", header=None)
    affiliation_coord_df = pd.read_csv('cleaned-data/DBLP-CSR/affiliation_coord.txt', lineterminator="\r", header=None)
    
    affiliation_df[6] = affiliation_coord_df[2]
    affiliation_df[7] = affiliation_coord_df[3]
    affiliation_df[8] = affiliation_coord_df[7]
    affiliation_df[9] = affiliation_coord_df[8]

    if save:
        affiliation_df.to_csv(save_name+".txt", header=None, index=None)
    
    return affiliation_df.values.tolist()

# classify authors.txt' entries by authors, store corresponding information in lists
def clean_authors(save = True, save_name = "authors_cleaned"):
    authors_df = pd.read_csv('cleaned-data/DBLP-CSR/authors.txt',lineterminator="\n", header=None)
    
    authors_df.columns = ["id",'key','Pos','Name','Gender','Prob']
    name_groups = authors_df.groupby('Name').groups
    names = name_groups.keys()
    papers = [[]]*len(names)
    pos = [[]]*len(names)
    gender = [" "]*len(names)
    prob = [" "]*len(names)

    for i, val in enumerate(names):
        gender[i] = authors_df['Gender'][i]
        prob[i] = authors_df['Prob'][i]
        papers[i] = [""]*len(name_groups[val])
        pos[i] = [100]*len(name_groups[val])
        for index, j in enumerate(name_groups[val]):
            papers[i][index]=authors_df['key'][j]
            pos[i][index]= authors_df['Pos'][j]
    
    new_authors_df = pd.DataFrame({'Name': names,
                        'Papers': papers,
                        "Gender": gender,
                        'Pos':pos,
                        'Prob':prob})
    if save:
        new_authors_df.to_csv(save_name+".txt", header=None, index=None)
    
    return new_authors_df.values.tolist()

# combine dataframes 
'''
authors_df = main_df = pd.read_csv('cleaned-data/DBLP-CSR/authors_complete.txt', lineterminator="\n", header=None)
papers_column = [[]]*len(authors_df[1])
for index, papers_string in enumerate(authors_df[1]):
    papers = papers_string.replace('\'','').strip('][').split(', ')
    author_papers = [0]*len(papers)
    for index2, paper in enumerate(papers):
        author_papers[index2] = int(main_df.index[main_df[0]==paper][0])
    papers_column [index] = author_papers
    if index % 1000== 0:
        print(index)

authors_column = [[]]*len(main_df)

for index, key_list_string in enumerate(authors_df[1]):
    key_list = key_list_string.replace('\'','').strip('][').split(', ')
    
    author = []
    
    for index2, key in enumerate(key_list):
        #print(key)
        paper_id = int(main_df.index[main_df[0]==key][0])
        #print(paper_id)
        position = int(authors_df[3][index].replace('\'','').strip('][').split(', ')[index2])
        # a dictionary where key is the postion and the value is the author's name
        if len(authors_column[paper_id]) == 0:
            authors_column[paper_id] = {position: index}
        else:
            authors_column[paper_id][position] = index

    if index %200 == 0:
        print(index)


institution_column = [[]]*len(authors_df)
position_column = [[]]*len(authors_df)

for index, key_list_string in enumerate(authors_df[1]):
    key_list = key_list_string.replace('\'','').strip('][').split(', ')
    institutions = ["-"]*len(key_list)
    positions = ["-"]*len(key_list)

    for index2, key in enumerate(key_list):
        entries = affiliation_df.loc[affiliation_df[1]==key].loc[affiliation_df[2]==authors_df[0][index]]
        if not entries.empty:
            institutions[index2]=entries[3].values[0]
            positions[index2]=entries[4].values[0]

    institution_column[index] = institutions
    position_column[index] = positions 

    if index%200 == 0:
        print(index/200)


    main = pd.read_csv('data/clean/main.csv')
    main["Authors"]=[None]*148520
    for i, val in enumerate(main["Key"]):
    if val in paper_authors.groups.keys():
        main.at[i, 'Authors'] = []
        for j, name in enumerate(paper_authors.get_group(val)["Name"]):
            main.at[i, 'Authors'].append(name)
    else:
        
#len(main)
'''