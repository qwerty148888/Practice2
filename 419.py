import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

def hypot(x, y):
    return math.hypot(x, y)

def angle(x, y):
    return math.atan2(y, x)

def shortest_path(A, B, R):
    ax, ay = A
    bx, by = B
    OA = hypot(ax, ay)
    OB = hypot(bx, by)

    # Проверка: прямая не пересекает круг
    dx, dy = bx - ax, by - ay
    distAB = hypot(dx, dy)
    t = ((-ax*dx - ay*dy) / (dx*dx + dy*dy))
    t = max(0, min(1, t))
    closest_x = ax + t*dx
    closest_y = ay + t*dy
    closest_dist = hypot(closest_x, closest_y)
    if closest_dist >= R:
        return distAB

    # Длина касательных и углы
    alphaA = math.acos(R / OA)
    alphaB = math.acos(R / OB)
    thetaA = angle(ax, ay)
    thetaB = angle(bx, by)

    results = []
    for signA in [1, -1]:
        for signB in [1, -1]:
            tA = thetaA + signA * alphaA
            tB = thetaB + signB * alphaB
            tangentA = math.sqrt(OA**2 - R**2)
            tangentB = math.sqrt(OB**2 - R**2)
            # Короткая дуга между точками касания
            dtheta = abs(tA - tB)
            if dtheta > math.pi:
                dtheta = 2*math.pi - dtheta
            arc = R * dtheta
            total = tangentA + arc + tangentB
            results.append(total)

    return min(results)

length = shortest_path((x1, y1), (x2, y2), R)
print(f"{length:.10f}")