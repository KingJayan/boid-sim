import pygame as pg
import random as rand

pg.init()
w,h = 800,800

screen = pg.display.set_mode((w,h))
pg.display.set_caption("boid simulation")
clock = pg.time.Clock()

running = True

class boid:
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

b1 = boid(400, 400, 1, 1)
boids = [b1]
for i in range(50):
    boids.append(boid(rand.random()*w, rand.random()*h, rand.random()*2-1, rand.random()*2-1))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill((20,20,20))

    for boid in boids:
        draw_boid(boid)
        update_boid(boid)

    for boid in boids:
        if boid.get_pose()[0] > w or boid.get_pose()[0] < 0:
            boid.x = boid.get_pose()[0] % w
        if boid.get_pose()[1] > h or boid.get_pose()[1] < 0:
            boid.y = boid.get_pose()[1] % h

    pg.display.flip()
    clock.tick(60)

pg.quit()