import sys
import os
import format_text
import inverted_index

foldername = False
searchmode = False
path = ''
query = ''
filenames = []
query_res = []
index = {}
file_titles = {}

if len(sys.argv) > 1 and sys.argv[1]:
    foldername = sys.argv[1]
if len(sys.argv) > 2 and sys.argv[2]:
    if sys.argv[2] == "-s":
        searchmode = True

if foldername:
    path = "./" + foldername
    for file in os.listdir(path):
        if file.endswith(".txt"):
            file_path = f"{path}/{file}"
            filenames.append(file_path)
    format_text.create_index(filenames, index, file_titles)

if searchmode:
    query = input("Query (empty query to stop): ")
    if query != "\n":
        query_res = inverted_index.search(index, query)
        if len(query_res) > 0:
            for doc in query_res:
                print(f'Title: "{file_titles[doc]}", File: {doc}')
        else:
            print("No results")