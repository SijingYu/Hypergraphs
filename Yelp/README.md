# Yelp Open Dataset
[original source](https://www.yelp.com/dataset)
## Description

This dataset has records of 6990280 reviews, 150346 businesses, 200100 pictures and 11 metroplitan areas

The original data contains 5 .json files. For our focus on hypergraph where restaurants are hyperedges, *yelp_academic_dataset_business.json*, *yelp_academic_dataset_review.json* and *yelp_academic_dataset_user.json* are used. 

Before running the code, please include the *raw-data* folder within the folder to access files.

However, original data files are omitted in the raw-data repository due to its size. The whole dataset can be directly downloaded from [https://www.yelp.com/dataset](https://www.yelp.com/dataset)

To get the cleaned data for each raw data file, run `python parsers.py`. 

To generate the hypergraph where each hyperedge is a paper and each node is an author, run `python hypergraph_generator.py`. Corresponding categorical labels for each edge will also be generated.  
