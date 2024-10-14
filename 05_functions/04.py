import math

def circle_stats(rad):
  return {
    'Area': round(math.pi * (rad ** 2), 2),
    'Circumference': round(2 * math.pi * rad, 2),
  }

circle_stats = circle_stats(50)

print(circle_stats)
