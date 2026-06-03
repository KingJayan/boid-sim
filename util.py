def clamp(v, min, max):
    if v<min:
        return min
    elif v>max:
        return max
    else:
        return v
def cap(v, max):
    if abs(v) > max:
        return max * (v/abs(v))
    else:
        return v
def cap_mag(vx, vy, max):
    mag = dist((0,0), (vx,vy))
    if mag > max:
        return (max * (vx/mag), max * (vy/mag))
    else:
        return (vx, vy)
    
if __name__ == "__main__":
    print("youre an idiot")
    print("(sorry)")