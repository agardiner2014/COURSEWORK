# COT 4930  Python Programming
# name: Aldrick Gardiner
# id  : agardiner2014
# lab : 04



dict = {}  


def main():

    makedict()        
    testdict()

    

def makedict():
    iFile = open ("fl-cities.txt","r")

    #print("File is open, and stored in file")

    for word in iFile:
        #strip white space
        word = word.rstrip()  
        
        #split word
        ( code, city ) = word.split( ":" )

    
        #dict
        dict [ city ] = code
  
    iFile.close( )

def testdict():
    cFile = open ("fl-maint.txt","r")

    #print ("File with commands is open")

    for Line in cFile:
        Line = Line.rstrip()
        cmd , var = Line.split("-")
        #print
        print (cmd)
        
        if (cmd == "p"):
            orderedList = list( dict.keys())
            orderedList.sort()
            #print List of the cities in order 
            for city in orderedList:
                print ('{0:15}  {1:15}'.format(city,dict[city]))
                    
        elif (cmd == "f"): 
            if var in dict:
                print ('{0:15}  {1:15}'.format(var,dict[var]))
            else:
                print ("%-6s"% city, "\t City Unknown \n")
                
        elif (cmd == "c"):
            change , city = var.split(":")
            if city in dict:
                dict[city] = change
                print ('{0:15}  {1:15}'.format(city, dict[city]))
            else:
                print ("%-6s"% city, "\t City Unknown \n")
                
        else:
            print ("unknown cmd \n")


main()
        
