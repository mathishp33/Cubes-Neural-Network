import pygame as pg
import math
import random as rnd
import numpy as np
import time
import tkinter as tk
from tkinter import ttk
import pickle

def main(c, g, x, y, w, h, m):
    if not isinstance(c,int):
        c = int(c.get())
        g = int(g.get())
        x = int(x.get())
        y = int(y.get())
        w = int(w.get())
        h = int(h.get())
        m = int(m.get())

    BLACK = (0, 0, 0)

    pg.init()
    WIDTH = 900
    HEIGHT = 900
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption("Smart Cubes")
    clock = pg.time.Clock()
    cubes = []
    babies = []
    
    class Food():
        def __init__(self):
            self.x = x
            self.y = y
            self.width = w
            self.height = h
        def update(self):
            pg.draw.rect(screen, (125,255,125), (self.x, self.y, self.width, self.height))
        def check(self, x, y):
            if self.x<x<self.width and self.y<y<self.height: return True
            else: return False
    class Cube():
        def __init__(self):
            self.x = rnd.randrange(0, WIDTH)
            self.y = rnd.randrange(0, HEIGHT)
            self.genes = [(rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)), rnd.random()*2 -1, rnd.randint(0, 19)]
            self.clock = self.genes[2]
            self.neurals = [0,0,0,self.genes[1],0,0]
            self.connections = [(4,rnd.randint(0, 3)), (0,0)]
            self.connections[1] = (5,rnd.randint(0, 3))
            while self.connections[0][1] == self.connections[1][1]:
                self.connections[1] = (5,rnd.randint(0, 3))
        def update(self, index):
            if clok>self.clock:
                self.neurals[0] = rnd.random()*2 -1
                self.neurals[1] = self.x/WIDTH *2 - 1
                self.neurals[2] = self.y/HEIGHT *2 - 1
                self.neurals[3] = self.neurals[3]
                self.neurals[4] = self.neurals[self.connections[0][1]]
                self.neurals[5] = self.neurals[self.connections[1][1]]
                self.x += self.neurals[4]
                self.y += self.neurals[5]
                if self.x<0:self.x=10
                if self.y<0:self.y=10
                if self.x>WIDTH:self.x=WIDTH-10
                if self.y>HEIGHT:self.y=HEIGHT-10
            pg.draw.rect(screen, self.genes[0], (self.x, self.y, 10, 10))
        def save(self):
            if food_area.check(self.x, self.y) == True:
                babies.append([self.connections, self.genes])
                if rnd.randint(0, 3)==0: babies.append([self.connections, self.genes])
        def birth(self, mum):
            if rnd.randint(0, 1000) > m:
                self.genes = mum[1]
                self.clock = self.genes[2]
                self.neurals = [0,0,0,self.genes[1],0,0]
                self.connections = mum[0]
                
    for i in range(c):
        cubes.append(Cube())
    food_area = Food()
    
    while True:
        babies = []
        start = time.time()
        clok = 0
        
        while time.time()-start<g :
            screen.fill(BLACK)
            food_area.update()
            if clok > 20: clok=0
            clok += 1
            
            for i in range(len(cubes)):
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                cubes[i].update(i)
            pg.display.flip()
            clock.tick(100)
            
        for i in range(len(cubes)):
            cubes[i].save()
        cubes = []
        for i in range(len(babies)):
            cubes.append(Cube())
            cubes[i].birth(babies[i])
    
root = tk.Tk()
root.geometry("300x400")
root.resizable(False, False)
root.title('Menu')

signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

c = tk.StringVar()
g = tk.StringVar()
x = tk.StringVar()
y = tk.StringVar()
w = tk.StringVar()
h = tk.StringVar()
m = tk.StringVar()

cc = ttk.Label(signin, text="number of entities : ")
cc.pack(fill='x', expand=True)
ce = ttk.Entry(signin, textvariable=c)
ce.pack(fill='x', expand=True)

gg = ttk.Label(signin, text="duration of a generation : ")
gg.pack(fill='x', expand=True)
ge = ttk.Entry(signin, textvariable=g)
ge.pack(fill='x', expand=True)

z = ttk.Label(signin, text="FOOD AREA : ")
z.pack(fill='x', expand=True)

xx = ttk.Label(signin, text="x : ")
xx.pack(fill='x', expand=True)
xe = ttk.Entry(signin, textvariable=x)
xe.pack(fill='x', expand=True)

yy = ttk.Label(signin, text="y : ")
yy.pack(fill='x', expand=True)
ye = ttk.Entry(signin, textvariable=y)
ye.pack(fill='x', expand=True)

ww = ttk.Label(signin, text="width : ")
ww.pack(fill='x', expand=True)
we = ttk.Entry(signin, textvariable=w)
we.pack(fill='x', expand=True)

hh = ttk.Label(signin, text="height : ")
hh.pack(fill='x', expand=True)
he = ttk.Entry(signin, textvariable=h)
he.pack(fill='x', expand=True)

mm = ttk.Label(signin, text="mutation /1000: ")
mm.pack(fill='x', expand=True)
me = ttk.Entry(signin, textvariable=m)
me.pack(fill='x', expand=True)

def get():
    main(c, g, x, y, w, h, m)
def load():
    file = open("data", 'rb')
    c, g, x, y, w, h, m = pickle.load(file)
    file.close
    main(c, g, x, y, w, h, m)
def save2():
    save(c, g, x, y, w, h, m)
def save(c, g, x, y, w, h, m):
    c = int(c.get())
    g = int(g.get())
    x = int(x.get())
    y = int(y.get())
    w = int(w.get())
    h = int(h.get())
    m = int(m.get())
    file = open('data', 'wb')
    pickle.dump((c, g, x, y, w, h, m), file)
    file.close

submit_button = ttk.Button(signin, text="Launch Simulation", command= get)
submit_button.pack(fill='x', expand=True, pady=0)
submit_button = ttk.Button(signin, text="Load Settings", command= load)
submit_button.pack(fill='x', expand=True, pady=0)
submit_button = ttk.Button(signin, text="Save Settings", command= save2)
submit_button.pack(fill='x', expand=True, pady=0)

root.mainloop()