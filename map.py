class Map:
    def __init__(self):
        self._matrix = []
        self._width = None
        self._height = None

    def loadData( self, filename="../Colorado_844x480.dat" ):
        # read in data
        f = open( filename )
        lines=f.read().split("\n")
        matrix=[]
        for line in lines:
            m=[]
            for h in line.split(" "):
                if len(h)>0:
                    m.append( int( h ) )

            if len( m ) > 1:
                matrix.append( m )
        self._matrix = matrix
        self._width=len(matrix[0])
        self._height=len(matrix)

    def getMatrix(self):
        return self._matrix

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height




