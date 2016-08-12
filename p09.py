
class Node :

    def __init__( self, data = None, next_node = None ) :
        self.data = data
        self.next_node = next_node

    def get_data( self ) :
        return self.data

    def get_next( self ) :
        return self.next_node

    def set_next( self, new_next ) :
        self.next_node = new_next


class List :

    def __init__( self, head = None ) :
        self.head = head
        self.tail = head

    def insert( self, data ) :
        new_node = Node( data )

        #new_node.set_next( self.head )

        if self.head == None :
            self.head = new_node
        else :
            self.tail.set_next( new_node )

        self.tail = new_node

        print( "insert(", data, "), new_node\t", id( new_node ),
                "\tnext_node\t", id( new_node.get_next( ) ) )

    def print( self ) :
        cur = self.head
        while cur :
            print( id( cur ), "\t", cur.get_data( ),
                              "\t", id( cur.get_next( ) ) )
            cur = cur.get_next( )

def main( ) :

    print( "\naddress of None is: ", id( None ) )

    print( )
    list = List( );
    list.insert( 10 )
    list.insert( 20 )
    list.insert( 30 )

    print( "\nFinal List:" )
    list.print( )

main( )
