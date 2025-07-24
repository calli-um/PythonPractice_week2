import random
import time

class Snake:
    def __init__(self, block_size=10,start_pos=(100,100),initial_length=3):
        self.block_size=block_size
        self.direction="RIGHT"
        self.body=[]

        #position
        x , y= start_pos
        for i in range(initial_length):
            self.body.append([x-i*block_size,y])    # This formula will handle the position by choosing segment

    def move(self, grow=False):
        head=self.body[0][:]
        if self.direction=="UP":
            head[1]-=self.block_size  # Head[1] refers to the y-axis movement 
        if self.direction=="DOWN":
            head[1]+=self.block_size
        if self.direction=="LEFT":      #Head[0] refers to the x-asix movement
            head[0]-=self.block_size
        if self.direction=="RIGHT":
            head[0]+=self.block_size
        
        self.body.insert(0,head)  # Index, Value --> insert head at start of the list
        if not grow:
            self.body.pop()
    
    def checkCollisions(self):
        return self.body[0] in self.body[1:]  # If head 0, touches any part of the body from 1-end
    def boundaryCollision(self):
        head_x,head_y=self.head_position()
        return head_x <0 or head_x >400 or head_y <0 or head_y >400
    
    def changeDirection(self, new_direction):
        opposites={"TOP":"DOWN", "DOWN":"TOP", "LEFT":"RIGHT", "RIGHT":"LEFT"}
        if new_direction!=opposites.get(self.direction):            # Because opposite movement will cause instant collide with itself(snake)
            self.direction=new_direction
    def score(self):
        return len(self.body)-3
    def current_segment(self):
        return self.body
    def head_position(self):
        return self.body[0]

'''class Food(Snake):
    def __init__(self):
        super().__init__()
    def randomSpawns():
        pass
    def snakeXscore():
        pass

class Bomb(Snake):
    def __init__(self):
        super().__init__()
    def randomSpawns():
        pass
    def hitAndOver():
        pass

class SafeZone(Snake):
    def __init__(self):
        super().__init__()
    def noBombSpawns():
        pass
    def noCollisionsFailure():
        pass
'''