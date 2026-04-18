from turtle import *

class face:

    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
        self.noswSize = 'small'

    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.goHome