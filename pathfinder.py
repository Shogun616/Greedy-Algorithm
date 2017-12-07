import sys, math, random, numpy

class Pathfinder:
    def __init__(self, visualiser, map):
        self._visualiser = visualiser
        self._map = map


    def findCheapestPath(self):

        # Mark's silly algorithm for finding the cheapest path:
        #   Use random logic - virtually gauranteed to give the correct answer
        #   eventually if we just run it enough times.
        #   NOTE: Since problem is NP-hard - we won't know for sure that it is
        #         the correct answer when we get it which is a bummer.

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

        # What next?  Can you do better than random?
        # TODO:  Step 1 - a greeedy algorithm from a random starting position
        # TODO:  Step 2 - best greedy of all possible starting positions
        # TODO:  Step 3 - improve even more!
        return


    def findPath(self, starting_row):
        # Code to find one path from left to right through the map
        # And return the total "cost" and path
        # Current finds only a random path - can you make it better?

        matrix = self._map.getMatrix()
        rows = self._map.getHeight()
        cols = self._map.getWidth()

        row = starting_row

        cost = 0
        col=0
        path=[ row ]

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


        return ( cost, path )



