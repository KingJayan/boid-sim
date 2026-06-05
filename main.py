import pygame as pg
import random as rand
from math import dist
from util import cap_mag
from config import *

pg.init()

screen = pg.display.set_mode((w,h))
pg.display.set_caption("boid simulation")
clock = pg.time.Clock()
font = pg.font.SysFont("Arial", 18)

running = True
paused = False
show_prox = False
bypass = False
max_history = 600

keybinds = Keybinds()

class Boid:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self, dt):
        if (not paused) or bypass:
            self.x += self.vx * dt
            self.y += self.vy * dt

    def get_pose(self):
        return (self.x, self.y)
    
    def set_pose(self, x, y):
        self.x = x
        self.y = y

def draw_boid(boid):
    pg.draw.circle(screen, (255,255,255), (int(boid.x), int(boid.y)), 5)

def update_boid(boid, dt):
    boid.update(dt)
def reverse_update(boid, dt):
    boid.update(-dt)

def snapshot_boids(boids):
    return [(boid.x, boid.y, boid.vx, boid.vy) for boid in boids]

def restore_boids(boids, state):
    for boid, (x, y, vx, vy) in zip(boids, state):
        boid.x = x
        boid.y = y
        boid.vx = vx
        boid.vy = vy

def find_neighbors(boid, boids, rad):
    neighbors = []
    for other in boids:
        if other != boid and dist(boid.get_pose(), other.get_pose()) < rad:
            neighbors.append(other)
    return neighbors


boids = []
for i in range(50):
    boids.append(Boid(rand.random()*w, rand.random()*h, rand.random()*2-1, rand.random()*2-1))

history = [snapshot_boids(boids)]

while running:
    dt = clock.tick(60) / (1000 / 60)
    bypass = False

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYUP and event.key == pg.K_ESCAPE):
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == keybinds.toggle_pause:
                paused = not paused
            elif event.key == keybinds.step_forward and paused:
                bypass = True
            elif event.key == keybinds.step_back and paused:
                if len(history) > 1:
                    history.pop()
                    restore_boids(boids, history[-1])
        elif event.type == pg.KEYUP:
            if event.key == keybinds.toggle_prox:
                show_prox = not show_prox
    screen.fill((20,20,20))
    
    for boid in boids:
        step_dt = dt if (not paused) or bypass else 0

        neighbors = find_neighbors(boid, boids, min_prox)
        if len(neighbors) > 0:
            acc_x, acc_y = 0,0
            for neighbor in neighbors:
                acc_x += boid.x - neighbor.x
                acc_y += boid.y - neighbor.y

            boid.vx += acc_x * avoid_factor * step_dt
            boid.vy += acc_y * avoid_factor * step_dt
        
        boid.vx, boid.vy = cap_mag(boid.vx, boid.vy, max_vel)
        boid.update(step_dt)
    
        if boid.x > w or boid.x < 0:
            boid.x = boid.x % w
        if boid.y > h or boid.y < 0:
            boid.y = boid.y % h
        
        draw_boid(boid)

    if step_dt != 0:
        history.append(snapshot_boids(boids))
        if len(history) > max_history:
            history.pop(0)

    bypass = False
    
    screen.blit(font.render(f"boids: {len(boids)}", True, (255,255,255)), (10,10))
    screen.blit(font.render(f"fps: {int(clock.get_fps())}", True, (255,255,255)), (10,30))
    screen.blit(font.render("paused" if paused else "", True, (255,255,255)), (10,50))

    pg.display.flip()

pg.quit()