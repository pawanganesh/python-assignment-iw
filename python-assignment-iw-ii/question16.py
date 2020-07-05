# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

class Mario():
    def __init__(self, level, screen, dashboard, sound, gravity=1):
        self.level = level
        self.screen = screen
        self.dashboard = dashboard
        self.sound = sound
        self.gravity = gravity
        print("Welcome to Mario")

    def moveMario(self):
        pass

    def bounce(self):
        pass

    def kill(self):
        pass

    def gameOver(self):
        pass

    def getPos(self):
        pass

    def setPos(self,x,y):
        pass

mario = Mario(45, 'test', 'test', '85%')
