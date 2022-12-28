import os

def createDictionary():
    wordsAdded = {}
    keywords = {}
    with open('keywords.txt', 'r') as KeywordsFile:
        keywords = KeywordsFile.read().lower().split()
    cwd = os.getcwd()
    os.chdir(cwd + '/text-files')
    fileList = os.listdir(os.getcwd())
    fileList.sort()
    for file in fileList:
        with open(file, 'r') as f:
            words = f.read().lower().split()
            wordsAdded[f.name] = []
            for word in words:
                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word in keywords and word not in wordsAdded[f.name]:
                    wordsAdded[f.name] += [word]
    os.chdir(cwd)
    return wordsAdded, cwd

def writeToFile(words, cwd):
    os.chdir(cwd)
    with open('forward_index_file.txt', 'w') as indexFile:
        for file, files in words.items():
            indexFile.write(file[:file.find(".txt")] + " ")
            for word in files:
                indexFile.write(word + " ")
            indexFile.write('\n')

writeToFile(*createDictionary())