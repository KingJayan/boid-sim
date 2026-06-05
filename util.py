from math import hypot, atan2

def clamp(v, low, high):
    return max(low, min(v, high))

def cap_mag(vx, vy, max_mag):
    mag = hypot(vx, vy)

    if mag > max_mag:
        scale = max_mag / mag
        return vx * scale, vy * scale

    return vx, vy

def mag_sq(x, y):
    return x*x + y*y

def heading(vx, vy):
    return atan2(vy, vx)


if __name__ == "__main__":
    print("youre an idiot")
    print("(sorry)")