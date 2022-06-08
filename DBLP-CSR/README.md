# DBLP Records and Entries for Key Computer Science Conferences
[original source](https://data.mendeley.com/datasets/3p9w84t5mr/1)
## Description

This dataset has 16-year (2000-2015) records of 81 Computer Science Research conferences for the purpose of a study done in paper *Women in Computer Science Research- What is Bibliography Data Telling Us?* by Agarwal et al. in 2016. ([link to the paper](http://dl.acm.org/citation.cfm?id=J198))

The original data contains 7 .sql files and the *DBLP-CSR-README.pdf* offers comprehensive description of each data file and its attributes. For the purpose of parsing, we delete extra lines associated with the .sql file format and save the remaining text as .txt file which can be directly parsed using a delimiter '),(', detailed in parser files.

To parsing the original files in the *raw-data* folder, run
`python parser.py file-name format` where 'file-name' is one of 
\"affiliation\", \"affiliation_coord\", \"authors_gender\", \"authors\", \"main\"; format is one of \".csv\" and \".txt\".

