'''
 * remove item from list
'''
from operator import index
import random

def addItem(file, newLine):
    f = open(file, "a")
    f.write(f"{str(newLine)}\n")
    f.close

def show(file):
    f = open (file, "r")
    TODO = f.readlines()
    f.close()

    for i in range(len(TODO)):
        TODO[i] = TODO[i].replace("\n", "")

    return(TODO)

def showIndexed(file):
    TODO = show(file)
    indexedTODO = ""

    for i in range(len(TODO)):
        indexedTODO += f"{i + 1}) {TODO[i]}\n"
    
    return(indexedTODO[:-2])

def removeItem(file, line):
    f = open (file, "r")
    TODO = f.readlines()
    f.close()

    try:
        TODO.pop(line - 1)
    except IndexError:
        return("This line does not exist!")

    f = open(file, "w")

    for i in TODO:
        f.write(i)

    f.close()