import pygame as pg
import random as rnd
import time

class Window:
    def __init__(self, c, g, x, y, w, h, m):
        self.cubes_0 = int(c.get())
        self.gen_time = int(g.get())
        self.food_x = int(x.get())
        self.food_y = int(y.get())
        self.food_width = int(w.get())
        self.food_height = int(h.get())
        self.mutation_odd = int(m.get())
    def main(self):
        pg.init()
        WIDTH = 900
        HEIGHT = 900
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Smart Cubes")
        clock = pg.time.Clock()
        cubes = []
        babies = []
        

                    
        for i in range(self.cubes_0):
            cubes.append(Cube(WIDTH, HEIGHT))
        
        self.running = True
        while self.running:
            babies = []
            start = time.time()
            
            while time.time() - start < self.gen_time:

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.running = False
                        pg.quit()

                screen.fill((0, 0, 0))

                pg.draw.rect(screen, (125,255,125), (self.food_x, self.food_y, self.food_width, self.food_height))
                
                for i, j in enumerate(cubes):
                    j.update()
                    pg.draw.rect(screen, j.genes[0], (j.x, j.y, 10, 10))
                pg.display.flip()
                clock.tick(100)
                
            for k in cubes:
                if pg.Rect(self.food_x, self.food_y, self.food_width, self.food_height).colliderect(pg.Rect(k.x, k.y, 10, 10)) and rnd.randint(0, 3):
                    babies.append((k.connections, k.genes))
            cubes = []
            for i in range(len(babies)):
                cubes.append(Cube(WIDTH, HEIGHT))
                cubes[i].birth(babies[i], self.mutation_odd)

class Cube():
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH, self.HEIGHT = WIDTH, HEIGHT
        self.x = rnd.randrange(0, WIDTH)
        self.y = rnd.randrange(0, HEIGHT)
        self.genes = [(rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)), rnd.random()*2 -1, rnd.random()*2] # color, constant, speed
        self.neurals = [0,0,0,self.genes[1],0,0]
        self.connections = [(4,rnd.randint(0, 3)), (0,0)]
        self.connections[1] = (5,rnd.randint(0, 3))
        while self.connections[0][1] == self.connections[1][1]:
            self.connections[1] = (5,rnd.randint(0, 3))

    def update(self):
        self.neurals[0] = rnd.random()*2 -1
        self.neurals[1] = self.x/self.WIDTH *2 - 1
        self.neurals[2] = self.y/self.HEIGHT *2 - 1
        self.neurals[3] = self.neurals[3]
        self.neurals[4] = self.neurals[self.connections[0][1]]
        self.neurals[5] = self.neurals[self.connections[1][1]]
        self.x += self.neurals[4] * self.genes[2]
        self.y += self.neurals[5] * self.genes[2]
        if self.x<0:self.x=10
        if self.y<0:self.y=10
        if self.x>self.WIDTH:self.x=self.WIDTH-10
        if self.y>self.HEIGHT:self.y=self.HEIGHT-10

    def birth(self, mum, mutation_odd):
        if rnd.randint(0, 1000) > mutation_odd:
            self.genes = mum[1]
            self.neurals = [0,0,0,self.genes[1],0,0]
            self.connections = mum[0]