import sys, math, random

class Pathfinder:
    def __init__(self, visualiser, map):
        self._visualiser = visualiser
        self._map = map
        self._table = {}
        dist = {}
        prev = {}

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self._table.keys())

    def addVertex( self, v ):
        if v not in self._table.keys():
            self._table[v] = set([])

    def removevertex( self, v):
        if v in self._table.keys():
            del self._table[v]

    def addEdge( self, v1, v2):
        if not v1 in self._table.keys():
            self.addVertex(v1)
        self._table[v1].add(v2)
        if not v2 in self._table.keys():
            self.addVertex(v2)
        self._table[v2].add(v1)

    def removeEdge( self, v1, v2, directed=False ):
        for (v, w) in self._table[v1]:
            if v == v2:
                self._table[v1].remove( (v,w) )
                break
            if not directed:
                for (v,w) in self._table[v2]:
                    if v == v1:
                        self._table[v2].remove( (v,w) )
                        break


    def areNeighbours( self, v1, v2 ):
        if v1 in self._table.keys():
           for (v,w) in self._table[v1]:
               if v == v2:
                   return True
        return False

    def cost( self, v1, v2 ):
        if v1 in self._table():
            for (v,w) in self._table[v1]:
                if v == v2:
                    return w
        return 0

    def findDFSPath( self, v1, v2, visited=[] ):
        if self.areNeighbours(v1, v2):  #Base Case
            return [ v1, v2 ]

        if v1 in self._table():
            neighbours = self._table[v1]
        for (v,w) in neighbours: #Recursive Case
            if n not in visited:
                p = self.findDFSPath( n, v2, visited + [v1] )
                if p !=None:
                    return [v1] + p #path found

        return None

    def dijsktra(self, initial):
        # Keep track of which nodes we have visited and best distance to them:
        visited = {initial: 0}
        # Keep track of the paths for shortest distances to each node:
        path = {}
        # Set of all nodes that need to be visited:
        nodes = set(self._table.keys())

        while nodes:  # still nodes unvisited
            # Find the node in nodes that has the smallest distance
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                # nothing left to look for - because graph is not connected
                break

            # "pop" the nod with smallest distance
            nodes.remove(min_node)
            # update distances to each node if we have found a shorter path
            current_weight = visited[min_node]
            for (edge,distance) in self._table[min_node]:
                weight = current_weight + distance
                if edge not in visited or weight < visited[edge]:
                    # this path is shorter, update distance and path:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path

  
    
    def isConnected( self ):
        for v1 in self._table.keys():
            for v2 in self._table.keys():

                if v1 != v2 and not self.findDFSPath( v1, v2 ):
                    return False

        return True


    def findCheapestPath(self, v1, v2, visited=[]):
        cheapest_cost = None
        cheapest_path = None
        cheapest_is_neighbour = False
        if v2 not in visited and self.areNeighbours(v1, v2):
            cheapest_cost = self.cost(v1, v2)
            cheapest_path = [v1,v2]
            cheapest_is_neighbour = True

        # else use BFS..
        if v1 in self._table.keys():
            neighbours = self._table[v1]
            for (n,w) in neighbours:
                if n not in visited:
                    ( p, cost ) = self.findCheapestPath( n, v2, visited+[v1] )
                    if not cheapest_cost and not cheapest_path:
                        cheapest_cost = cost
                        cheapest_path = p
                    elif cost!= 0 and cost < cheapest_cost:
                        cheapest_cost = cost
                        cheapest_path = p
                        cheapest_is_neighbour = False

            if cheapest_path != None:
                if cheapest_is_neighbour:
                    return ( cheapest_path, cheapest_cost )
                else:
                    return ( [v1] + cheapest_path, cheapest_cost + self.cost(v1, cheapest_path[0]) )
        return (None, 0)

        
        # Starting at a random position on the left:
        starting_row = random.randint( 0, self._map.getHeight() )

        # Search for one random path:
        ( cost, path ) = self.findPath( starting_row )

        # It is the only path we have found, visualise it:
        self._visualiser.addPath(path)

        # The only path so it must also be the best path, visualise that:
        self._visualiser.setBestPath(path)

        # And the cost of this so called "best" path:
        self._visualiser.setBestPathCost( cost )

     
        return


    def findPath(self, starting_row):
          
        matrix = self._map.getMatrix()
        rows = self._map.getHeight()
        cols = self._map.getWidth()

        row = starting_row

        cost = 0
        col=0
        path=[ row ]
        shortest_path=[row]
       

        while col+1 < cols:
            # how high are we right now?
            current_altitude = matrix[row][col]

            # Pick a random direction - up/right,  right,  down/right
            r = random.randint(-1,1)
            row = row + r
            if row < 0:
                row = 0
            if row > rows-1:
                row = rows-1
            col += 1

            # how high are we now?
            new_altitude = matrix[row][col]

            # change in height:
            delta = int( math.fabs( new_altitude - current_altitude ) )

            # cost is the absolute change in height per step
            cost += delta

            # add this step to the path we are following
            path.append( row )


        return shortest_path ( cost, path )



