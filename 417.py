import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx*dx + dy*dy
b = 2*(dx*x1 + dy*y1)
c = x1*x1 + y1*y1 - R*R

discriminant = b*b - 4*a*c

if discriminant < 0:
    # Нет пересечений, проверяем полностью внутри
    if x1*x1 + y1*y1 <= R*R and x2*x2 + y2*y2 <= R*R:
        length = math.hypot(dx, dy)
    else:
        length = 0.0
else:
    sqrt_disc = math.sqrt(discriminant)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    # Ограничиваем [0,1]
    t1 = max(0.0, min(1.0, t1))
    t2 = max(0.0, min(1.0, t2))
    if t2 < t1:
        t1, t2 = t2, t1
    length = math.hypot(dx, dy) * (t2 - t1)

print(f"{length:.10f}")