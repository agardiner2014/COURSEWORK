# COT 4930  Python Programming
# name: Aldrick Gardiner
# id  : agardiner2014
# lab : 06


class Node :

    def __init__( self, data = None, nextnode = None ) :
        self.data = data
        self.nextnode = nextnode

    def getdata( self ) :
        return self.data

    def getnext( self ) :
        return self.nextnode

    def setnext( self, newnext ) :
        self.nextnode = newnext


class List :

    def __init__( self, head = None ) :
        self.head = head
        self.tail = head

    def insert( self, data ):
        newnode = Node()
        newnode.data = data

        if self.head == None:
            self.head = newnode

        else:
            current = self.head
            previous = current
            while(current != None) and (current.data < data):
                previous = current
                current = current.getnext()

            if previous == current:
                newnode.setnext(current)
                self.head = newnode

            elif current == None:
                previous.setnext(newnode)

            else:
                newnode.setnext(current)
                previous.setnext(newnode)
                
        print()
        print( "insert(", data, "),")
        print()
        

        
    def print( self ) :
        cur = self.head
        print("print( )")
        while cur :
            print( id( cur ), "\t", cur.getdata( ),
                              "\t", id( cur.getnext( ) ) )
            cur = cur.getnext( )

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getdata() == data:
                found = True
            else:
                previous = current
                current = current.getnext()

        if current is None:
            current = previous
        if previous is None:
            self.head = current.getnext()
            print()
            print( "remove(", data, "),")
            print()

        else:
            previous.setnext(current.getnext())
            print()
            print( "remove(", data, "),")
            print()

            

def main( ) :


    list = List( )


    iFile = open ("llist.txt","r")

    #print("File is open, and stored in file")

    

    for word in iFile:

        #strip white space

        word = word.strip()

        word = word.rstrip()

        word = word.rstrip()



        #If statement

        if "i" in word:

            key , statement = word.split()
            list.insert(statement)


        elif "p" in word:
            list.print()

        elif "r" in word:
            key , statement = word.split()
            list.remove(statement)

        else:
            print("Incorrect Command")



    


    iFile.close( )


main( )
