import io
def main(inputFile,outputFile):
    info,rawData = io.readFileInput(inputFile)
    info_split=info.split()
    print(info_split)
    contNum = info_split[0]
    projNum = info_split[1]
    print(info)
    print(rawData)    
    io.generateData(contNum,projNum,rawData)     

#def chooseContributor(project):
    

if __name__ == "__main__":
    testCases = [("a_an_example.in.txt","OUT-a.txt")]
    for test in testCases:
        main( test[0], test[1])
        print("FINISHED TEST CASE ------\n" + str(test) + "-----------------------------\n")