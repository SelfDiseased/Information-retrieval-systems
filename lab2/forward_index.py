import json

def search(index, query):
    pages = []
    for key in index.keys():
        if query in index[key]:
            pages.append(key)
    return pages

def append_entry(dictionary, document, keywords):
    if document not in dictionary:
        dictionary[document] = keywords
    elif document in dictionary:
        dictionary[document] += keywords
        dictionary[document] = list(set(dictionary[document]))
  
def print_dictionary(dictionary):
    print(json.dumps(dictionary, sort_keys=False, indent=2))