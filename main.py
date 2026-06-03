import pygame as pg
import random as rand
from math import dist
from util import cap_mag
from config import *

pg.init()

screen = pg.display.set_mode((w,h))
pg.display.set_caption("boid simulation")
clock = pg.time.Clock()

running = True

class Boid:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def get_pose(self):
        return (self.x, self.y)
    
    def set_pose(self, x, y):
        self.x = x
        self.y = y

def draw_boid(boid):
    pg.draw.circle(screen, (255,255,255), (int(boid.x), int(boid.y)), 5)

def update_boid(boid):
    boid.update()

def find_neighbors(boid, boids, rad):
    neighbors = []
    for other in boids:
        if other != boid and dist(boid.get_pose(), other.get_pose()) < rad:
            neighbors.append(other)
    return neighbors


b1 = Boid(400, 400, 1, 1)
boids = [b1]
for i in range(50):
    boids.append(Boid(rand.random()*w, rand.random()*h, rand.random()*2-1, rand.random()*2-1))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill((20,20,20))

    for boid in boids:
        draw_boid(boid)
    
    for boid in boids:
        neighbors = find_neighbors(boid, boids, min_prox)
        if len(neighbors) > 0:
            acc_x, acc_y = 0,0
            for neighbor in neighbors:
                acc_x += boid.x - neighbor.x
                acc_y += boid.y - neighbor.y

            boid.vx += acc_x * avoid_factor
            boid.vy += acc_y * avoid_factor
        
        boid.vx, boid.vy = cap_mag(boid.vx, boid.vy, max_vel)
        update_boid(boid)
    
    for boid in boids:
        if boid.x > w or boid.x < 0:
            boid.x = boid.x % w
        if boid.y > h or boid.y < 0:
            boid.y = boid.y % h

    pg.display.flip()
    clock.tick(60)

pg.quit()