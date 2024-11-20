import json
import pandas as pd

file = 'netflix_titles.tsv'

netflix_read = pd.read_csv(file, sep="\t", usecols=["PRIMARYTITLE", "DIRECTOR", "CAST", "GENRES", "STARTYEAR" ])
data_list = []

for x, row in netflix_read.iterrows():
    primarytitle = {
        "title": row["PRIMARYTITLE"],
        "directors": row["DIRECTOR"].split(", ") if pd.notna(row["DIRECTOR"]) else [],
        "cast": row["CAST"].split(", ") if pd.notna(row["CAST"]) else [],
        "genres": row["GENRES"].split(", ") if pd.notna(row["GENRES"]) else [],
        "decade": row["STARTYEAR"] // 10 * 10
    }
    data_list.append(primarytitle)

with open('hw02_output.json.', mode='w', encoding='utf-8') as text_write:
    json.dump(data_list, text_write, ensure_ascii=False, indent=4)
