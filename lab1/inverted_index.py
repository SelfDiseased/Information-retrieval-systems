import os

def createDictionary():
    wordsAdded = {}
    cwd = os.getcwd()
    os.chdir(cwd + '/text-files')
    fileList = os.listdir(os.getcwd())
    fileList.sort()
    for file in fileList:
        with open(file, 'r') as f:
            words = f.read().lower().split()
            for word in words:
                fileName = f.name
                if word[-1] in [',', '!', '?', '.']:
                    word = word[:-1]
                if word not in wordsAdded.keys():
                    wordsAdded[word] = [fileName]
                else:
                    if file not in wordsAdded[word]:
                        wordsAdded[word] += [fileName]
    os.chdir(cwd)
    return wordsAdded, cwd

def writeToFile(words, cwd):
    os.chdir(cwd)
    with open('inverted_index_file.txt', 'w') as indexFile:
        for word, files in words.items():
            indexFile.write(word + " ")
            for file in files:
                indexFile.write(file[:file.find(".txt") + 4] + " ")
            indexFile.write('\n')

writeToFile(*createDictionary()) 