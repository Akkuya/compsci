import math

running = True


total = 0
while running:
    angle = int(input("Enter angle: "))
    if angle == 0:
        running = False
    else:
        total = total + angle

direction = total % 360

if direction <= 45 or direction >= 316:
    print("East")

elif direction <= 135:
    print("North")

elif direction <= 225:
    print("West")

elif direction <= 315:
    print("South")

print("Degrees: ", direction)
print("Radians: ", math.radians(direction))