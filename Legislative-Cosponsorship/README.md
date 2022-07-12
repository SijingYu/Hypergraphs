# Legislative Cosponsorship Networks in the U.S. House and Senate

[original source](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/O22JMY)

## Description

This dataset has sponsor/cosponsor network behind the legislation bills, used to study the social networks of legislators, done by James H. Fowler in 2007. ([link to the paper](https://www.sciencedirect.com/science/article/pii/S0378873305000730?via%3Dihub))

The original data contains 17 files and the *Readme.txt* offers comprehensive description of each data file and its attributes. For our focus, *bills.txt*, "cosponsors.txt", "sponsors.txt", "house.csv", "party.txt", "passedbills.txt" and "senate.csv" are used.

To get the cleaned data for each raw data file, run `python parsers.py`. 

To generate the hypergraph where each hyperedge is a bill and each node is sponsor/cosponsor, run `python hypergraph_generator.py`. Corresponding categorical labels for each edge will also be generated.  
