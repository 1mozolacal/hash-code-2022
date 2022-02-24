pathToFile = 'inputFiles/'


def main(inputFile,outputFile):
    info,rawData = readFileInput(inputFile)
    info_split=info.split()
    print(info_split)
    contNum = info_split[0]
    projNum = info_split[1]
    print(info)
    print(rawData)    
   
class Contributor:
    def __init__(self,name,skills):
        self.name=name
        self.skills=skills

class Project:
    def __init__():
        print(1)

class Skill:
    def __init__(self,skillName,skillLevel):
        self.skillName=skillName
        self.skillLevel=skillLevel        

def readFileInput(inputFile):
    filepath= pathToFile + inputFile
    f = open(filepath,"r")
    return f.readline(),f.read()

def generateData(contNum,projNum,data):
    contributors = {}
    projects = {}
    counter = 0
    splitlines = data.splitlines()
    for i in range(contNum):
        contSplit = splitlines[counter].split()
        name = contSplit[0]
        skills = []
        for skills in range(contSplit[1]):
            skillsplit = 
            #change


if __name__ == "__main__":
    testCases = [("a_an_example.in.txt","OUT-a.txt")]
    for test in testCases:
        main( test[0], test[1])
        print("FINISHED TEST CASE ------\n" + str(test) + "-----------------------------\n")