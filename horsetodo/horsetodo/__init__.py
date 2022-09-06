def addItem(file, newLine):
    f = open(file, "a")
    f.write(f"{str(newLine)}\n")
    f.close

def show(file):
    f = open (file, "r")
    TODO = f.readlines()
    f.close()

    return(TODO)

def showIndexed(file):
    TODO = show(file)
    indexedTODO = ""

    for i in range(len(TODO)):
        indexedTODO += f"{i + 1}) {TODO[i]}"
    
    return(indexedTODO[:-1])

# output for "custom" waybar module
def showIndexedWaybar(file):
    indexedTODO = showIndexed(file)
    escapedTODO = ""

    for i in indexedTODO:
        escapedTODO += i.replace("\n", "\\n")

    return ('{"text":"TODO", "tooltip":"' + escapedTODO + '"}')


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