import sys
import pygame

class Visualiser:
    def __init__(self, name, width, height):
        self._name = name
        self._width = width
        self._height = height
        self._running = True
        self._matrix = None
        self._paths = []
        self._best_path = None
        self._best_path_cost = None
        self._max_alt = -sys.maxsize
        self._min_alt = sys.maxsize

        pygame.init()
        self._screen = pygame.display.set_mode((width, height))
        pygame.font.init()
        pygame.display.set_caption(self._name)

    def setMap(self, map):
        self._map = map
        mx = self._map.getMatrix()
        for row in range(self._height):
            for col in range(self._width):
                if mx[row][col] < self._min_alt:
                    self._min_alt = mx[row][col]
                if mx[row][col] > self._max_alt:
                    self._max_alt = mx[row][col]

    def drawMatrix(self):
        if self._map:
            mx = self._map.getMatrix()
            for row in range(self._height):
                for col in range(self._width):
                    h = (255 * (mx[row][col] - self._min_alt)) // (self._max_alt - self._min_alt)
                    # print(row, col, h)
                    self._screen.set_at((col, row), (h, h, h))

    def addPath(self, path):
        self._paths.append( path )

    def drawPaths(self):
        if self._paths:
            for path in self._paths:
                for col in range(self._width):
                    row = path[col]
                    h = (255, 0, 0)
                    self._screen.set_at((col, row), h)

    def setBestPath(self, path):
        self._best_path = path

    def setBestPathCost(self, cost):
        self._best_path_cost = cost

    def drawBestPath(self):
        if self._best_path:
            for col in range(self._width):
                row = self._best_path[col]
                h = (0,255,0)
                self._screen.set_at((col, row), h)

    def drawBestPathCost(self):
        if self._best_path_cost:
            myfont = pygame.font.SysFont('arial', 36)
            textsurface = myfont.render('Shortest path found: {}m'.format(self._best_path_cost), False, (0, 255, 0))
            x= ( self._width - textsurface.get_width()  )//2
            y= ( self._height - textsurface.get_height())//2
            self._screen.blit(textsurface, (x,y))

    def runLoop(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();
                    sys.exit();

            self.drawMatrix()
            self.drawPaths()
            self.drawBestPath()
            self.drawBestPathCost()

            pygame.display.update()
            
        pygame.quit()
