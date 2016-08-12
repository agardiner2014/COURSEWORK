

zipFinder = {}  #global dictionary

def make_dict():
    labFile = open ("fl_cities.txt","r")

    #print("File is open, and stored in lab file")

    for detail in labFile:
        #print ("%s" % detail) #test
        detail = detail.rstrip()  #remove the white space on the right hand side
        
        ( code, city ) = detail.split( ":" )
        #print ("City = ", city, " zip code = ", code ) #test
        
        zipFinder [ city ] = code
        #print ("the zip code for ",city, " is ",zipFinder[city], sep = "")          #test

    #print (zipFinder.keys())
    #print (zipFinder.values())

    labFile.close( )

def test_dict():
    commandFile = open ("fl_maint.txt","r")

    #print ("File with commands is open")

    for commandLine in commandFile:
        #print ("Currrnt command line: ", commandLine)
        commandLine = commandLine.rstrip()
        command , variable = commandLine.split("-")
        #print ( "the comand is: ", command , "and the object is ", variable)
        
        print (command)
        
        if (command == "p"):
            orderedList = list( zipFinder.keys())
            orderedList.sort()
            #print ( "List of the cities in order = ", keys , "\n")
            for city in orderedList:
                print ("%-6s\t%-6s" %(city,zipFinder[city]))
                    
        elif (command == "f"): #finds the city's availability in the list and returns the city and its zipcode
            if variable in zipFinder:
                print ("%-6s\t%-6s"%(variable,zipFinder[variable]))
            else:
                print ("%-6s"% city, "\t City Unknown \n")
                
        elif (command == "c"):
            #print ( "new detail: " varable)
            change , city = variable.split(":")
            if city in zipFinder:
                zipFinder[city] = change
                print ("%-6s\t%-6s" % (city, zipFinder[city]))
            else:
                print ("%-6s"% city, "\t City Unknown \n")
                
        else:
            print ("unknown cmd \n")
        
make_dict()        
test_dict()
