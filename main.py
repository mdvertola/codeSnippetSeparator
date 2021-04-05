import re
import time
# import h5py
# open file to read from dataset
file = open('LabeledToySet.csv', 'r')

# create txt files for each model input


# Write to txt File
gitFunctionsFile = open('data/train.git_methname.txt', 'a')
gitOperationsFile = open('data/train.git_apiseq.txt', 'a')
gitTokensFile = open('data/train.git_token.txt', 'a')
stackFunctionsFile = open('data/train.stack_methname.txt', 'a')
stackOperationsFile = open('data/train.stack_apiseq.txt', 'a')
stackTokensFile = open('data/train.stack_tokens.txt', 'a')
rawCode = open('data/use.rawcode.txt', 'a')
# # Write to h5 for model loading
# gitFunctionsFile = h5py.File('data/train.git_methname.h5', 'a')
# gitOperationsFile = h5py.File('data/train.git_apiseq.h5', 'a')
# gitTokensFile = h5py.File('data/train.git_token.h5', 'a')
# stackFunctionsFile = h5py.File('data/train.stack_methname.h5', 'a')
# stackOperationsFile = h5py.File('data/train.stack_apiseq.h5', 'a')
# stackTokensFile = h5py.File('data/train.stack_tokens.h5', 'a')

# read each line
for l in file:
    splitLine = l.split(',')
    # create dict containing values
    line = {
        "path": splitLine[0],
        "vulnName": splitLine[1],
        "gitSnip": splitLine[2],
        "stackTags": splitLine[3],
        "stackSnip": splitLine[4],
        "label": splitLine[5].replace('\n','')
    }
    # print(line)

    # define regex pattern to find functions within
    functionPattern = '[a-zA-Z._]+\(.*?\)+'
    functionNamePattern = '[a-zA-Z._]+\('
    operationsPattern = '\(.*?\)+'
    cleanOperationsPattern = "[^a-zA-Z0-9 .:&%*\-_+=/%><!\[\]]+"

    # print('-----GitHub-----')
    # # clean up code snippet
    # cleanGitSnip = line['gitSnip'][:-8]

    # # use regex to extract each component from the code snippets
    # gitFunctions = re.findall(functionPattern, cleanGitSnip)
    # gitFunctionNames = str(re.findall(functionNamePattern, cleanGitSnip)).replace('\'','').replace(',','').replace('(','').replace('  ',' ')[1:-1]
    # gitOperations = str(re.sub(cleanOperationsPattern,'',str(re.findall(operationsPattern, str(gitFunctions)))).split(' ')).replace("'",'').replace(']]',']').replace('[[','[').replace('\'','').replace(',','').replace('  ',' ')[1:-1]
    # gitTokens = line['vulnName']

    # # print cleaned output
    # print('Snippet: '+ cleanGitSnip)
    # print('Function Names: ' + str(gitFunctionNames))
    # print('Operations: ' + str(gitOperations))
    # print('Tokens: ' + gitTokens)

    # # write cleaned output to corresponding files
    # gitFunctionsFile.write(gitFunctionNames + '\n')
    # gitOperationsFile.write(gitOperations + '\n')
    # gitTokensFile.write(gitTokens + '\n')

    print('-----StackOverflow-----')
    stackSnip = line['stackSnip']

    # use regex to extract each component from the code snippets
    stackFunctions = re.findall(functionPattern, stackSnip)
    stackFunctionNames = str(re.findall(functionNamePattern, stackSnip)).replace('\'','').replace(',','').replace('(','').replace('  ',' ')[1:-1]
    stackOperations = str(re.sub(cleanOperationsPattern, '', str(re.findall(operationsPattern, str(stackFunctions)))).split(' ')).replace("'",'').replace(']]',']').replace('[[','[').replace('\'','').replace(',','').replace('  ',' ')[1:-1]
    stackTokens = line['stackTags'].replace('><',' ').replace('<','').replace('>','')
    print('Snippet: ' + stackSnip)
    # print('Function Names: ' + str(stackFunctionNames))
    # print('Operations: ' + str(stackOperations))
    # print('Tokens: ' + stackTokens + '\n')
    rawCode.write(stackSnip + '\n')
    # stackFunctionsFile.write(stackFunctionNames + '\n')
    # stackOperationsFile.write(stackOperations + '\n')
    # stackTokensFile.write(stackTokens + '\n')
rawCode.close()
# gitFunctionsFile.close()
# gitOperationsFile.close()
# gitTokensFile.close()
# stackFunctionsFile.close()
# stackOperationsFile.close()
# stackTokensFile.close()