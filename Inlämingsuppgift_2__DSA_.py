import pygame
import sys
import random


from map import Map
from visualiser import Visualiser
from pathfinder import Pathfinder


map = Map()
map.loadData()

visualiser = Visualiser( "Inlupp 2 - Visualiser", map.getWidth(), map.getHeight() )
visualiser.setMap( map )

pathfinder = Pathfinder( visualiser, map )
pathfinder.findCheapestPath()

visualiser.runLoop()

