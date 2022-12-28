import json  
  
def search(index, query):
    if query in index:
        return index[query]
    return []

def append_entry_key(dictionary, keyword, document):
    if keyword not in dictionary:
        dictionary[keyword] = [document]
    elif keyword in dictionary:
        if document not in dictionary[keyword]:
            dictionary[keyword].append(document)
      
def append_entry(dictionary, keywords, document):
    for key in keywords:
        append_entry_key(dictionary, key, document)

def print_dictionary(dictionary):
    print(json.dumps(dictionary, sort_keys = False, indent = 2))