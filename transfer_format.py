import pandas as pd
import json

# Converts corpus.tsv from News-Media-Reliability to JSON list of source urls, compliant with NewsScraper format

df = pd.read_csv('corpus.tsv', delimiter='\t')
urls = df['source_url']

obj = {}
source_names = df['source_url_normalized'].values
urls = df['source_url'].values
for i in range(len(df)):
    obj.update({source_names[i]: {"link": urls[i]}})

with open("EMNLP18NewsSources.json", "w") as f:
    json.dump(obj, f)
