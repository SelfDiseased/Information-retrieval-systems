import string
import inverted_index

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def modify_document(text):
    textArray = text.split()
    array = []
    modifiedTerm = ''
    for term in textArray:
        modifiedTerm = term.strip(string.punctuation)
        modifiedTerm = modifiedTerm.lower()
        if len(modifiedTerm) > 0:
            array.append(modifiedTerm)
    return array

def get_text_title(text):
    return text.partition('\n')[0]

def create_index(filenames, index, file_titles):
    for file in filenames:
        text = read_text_file(file) 
        file_titles[file] = get_text_title(text)
        terms = modify_document(text)
        inverted_index.append_entry(index, terms, file)

def print_index(index):
    inverted_index.print_dictionary(index)