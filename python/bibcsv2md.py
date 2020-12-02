#!/usr/bin/env python3

# Author: Daniel Burkhardt
# Copyright: 2020-present
# License GPLv3
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("bib_path", type=str,
                    help="Path to the bib.csv file needing translating.")
args = parser.parse_args()


data = pd.read_csv(args.bib_path)

data = data.sort_values("Publication Year", ascending=False)

curr_year = -1

for i, pub in data.iterrows():
    if pub["Publication Year"] != curr_year:
        print("<br>\n\n## {}  \n\n<br>  \n".format(pub["Publication Year"]))
        curr_year = pub["Publication Year"]
    ref = []
    ref.append("* **{}**".format(pub['Title']))
    ref.append('  \n')
    authors = pub["Author"]
#    authors = authors.replace(";", ",")
    if not authors.endswith('.'):
        authors += '.'
    ref.append(authors + ' ')
    journal = pub["Publication Title"]
    if not journal.endswith("."):
        journal += "."
    ref.append("***{}*** ".format(journal))
    ref.append(str(pub["Publication Year"]) + ". ")
    extra_data = data['Extra'].loc[0].split(' ')
    for i, val in enumerate(extra_data):
        if val == 'PMID:':
            key = extra_data[i+1]
    pmid = "PMID: [{}](https://www.ncbi.nlm.nih.gov/pubmed/{})  \n  ".format(key,key)
    ref.append(pmid)
    print(''.join(ref))
