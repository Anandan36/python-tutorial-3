x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On Y-axis")
elif y == 0:
    print("On X-axis")
elif x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
