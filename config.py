from dataclasses import dataclass
import pygame as pg

w,h = 800,800

# separation
min_prox = 50
avoid_factor = 0.05

# alignment

# cohesion

# other
max_vel = 2

@dataclass
class Keybinds:
    toggle_pause: int = pg.K_SPACE
    step_forward: int = pg.K_PERIOD
    step_back: int = pg.K_COMMA
    toggle_prox: int = pg.K_p