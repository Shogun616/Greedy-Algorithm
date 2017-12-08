import sys, math, random

class Pathfinder:
    def __init__(self, visualiser, map):
        self._visualiser = visualiser
        self._map = map
        self._table = {}
    

    def findCheapestPath(self):

       
       

        starting_row = random.randint( 0, self._map.getHeight() )

      
        ( cost, path ) = self.findPath( starting_row,  )

       
        self._visualiser.addPath(path)

       
        self._visualiser.setBestPath(path)

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
       
       

        while col+1 < cols:
            # how high are we right now?
            current_altitude = matrix[row][col]
            right_altitude = matrix[row][col+1]
            up_altiude = matrix[row-1][col+1]
            down_altitude = matrix[row+1][col+1]
            cost_up = math.fabs( current_altitude - up_altiude)
            cost_right = math.fabs(current_altitude - right_altitude)
            cost_down = math.fabs( current_altitude - down_altitude)


            # Pick a random direction - up/right,  right,  down/right
            if cost_up < cost_right and cost_up < cost_down:
                r = -1
            elif cost_down < cost_up and cost_down < cost_right:
                r = 1
            else:
                r = 0

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



