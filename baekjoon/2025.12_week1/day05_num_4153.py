# 251212

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    sides = [a, b, c]
    sides.sort()       
    x, y, h = sides[0], sides[1], sides[2]
    if x*x + y*y == h*h:
        print("right")
    else:
        print("wrong")


# ===============================================

