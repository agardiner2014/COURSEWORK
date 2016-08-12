# COT 4930  Python Programming
# name: Aldrick Gardiner
# id  : agardiner2014
# lab : 04



dict = {}  


def main():

    iFile = open ("bib.txt","r")

    #print("File is open, and stored in file")


    for word in iFile:
        #strip white space
        word = word.strip()
        word = word.rstrip(',')
        word = word.rstrip('.')

        #If statement
        if "\\bibitem" in word:
            print("<doi>")

        elif "\\bibitem" != word:
            if not word:
                continue

            else:
                #split word
                key , statement = word.split(" ",1)
                
                #dict
                dict [ key ] = statement

                commands(key)
            
        elif not word:
            print("</doi>")


    iFile.close( )


def commands(key):
    if key == "\\A":
        print("<Author>",dict[key],"</Author>")

    elif key == "\\B":
        print("<Book>",dict[key],"</Book>")

    elif key == "\\R":
        print("<Article>",dict[key],"</Article>")

    elif key == "\\P":
        print("<Publisher>",dict[key],"</Piblisher>")

    elif key == "\\J":
        print("<Journal>",dict[key],"</Journal>")

    elif key == "\\Y":
        print("<Year>",dict[key],"</Year>")

    else:
        print("+++ Unknown: ", key, " An inalid command here.")



      
main()
