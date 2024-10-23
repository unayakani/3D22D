import matplotlib.pyplot as plt
import math

focal_length = 2
z = 5
rotation_amount = 0.785 # 45 deg

cube = [(-0.5, 0.5, z), (-0.5, -0.5, z), (0.5, 0.5, z), (0.5, -0.5, z), (-0.5, 0.5, z + 1), (-0.5, -0.5, z + 1), (0.5, 0.5, z + 1), (0.5, -0.5, z + 1)]

cube2d = list()
cube2dx = list()
cube2dy = list()

def to2d(x, y, z):
    xp = (x * focal_length) / (z + focal_length)
    yp = (y * focal_length) / (z + focal_length)
    return (xp, yp)

for i, j, k in cube:
    cube2d.append(to2d(i, j, k))

for i, j in cube2d:
    cube2dx.append(i)
    cube2dy.append(j)

cuberotated = list()

def rotatex(x, y, z, a):
    return (x, y * math.cos(a) + z * math.sin(a), z * math.cos(a) - y * math.sin(a))

for k, l, m in cube:
    cuberotated.append(rotatex(k, l, m, rotation_amount))

cuberotated2d = list()
cuberotated2dx = list()
cuberotated2dy = list()

for i, j, k in cuberotated:
    cuberotated2d.append(to2d(i, j, k))

for i, j in cuberotated2d:
    cuberotated2dx.append(i)
    cuberotated2dy.append(j)

# ---------

x1 = [cuberotated2dx[0], cuberotated2dx[1]]
y1 = [cuberotated2dy[0], cuberotated2dy[1]]
x2 = [cuberotated2dx[0], cuberotated2dx[2]]
y2 = [cuberotated2dy[0], cuberotated2dy[2]]
x3 = [cuberotated2dx[3], cuberotated2dx[2]]
y3 = [cuberotated2dy[3], cuberotated2dy[2]]
x4 = [cuberotated2dx[3], cuberotated2dx[1]]
y4 = [cuberotated2dy[3], cuberotated2dy[1]]

x5 = [cuberotated2dx[4], cuberotated2dx[5]]
y5 = [cuberotated2dy[4], cuberotated2dy[5]]
x6 = [cuberotated2dx[4], cuberotated2dx[6]]
y6 = [cuberotated2dy[4], cuberotated2dy[6]]
x7 = [cuberotated2dx[7], cuberotated2dx[5]]
y7 = [cuberotated2dy[7], cuberotated2dy[5]]
x8 = [cuberotated2dx[7], cuberotated2dx[6]]
y8 = [cuberotated2dy[7], cuberotated2dy[6]]

x9 = [cuberotated2dx[4], cuberotated2dx[0]]
y9 = [cuberotated2dy[4], cuberotated2dy[0]]
x10 = [cuberotated2dx[6], cuberotated2dx[2]]
y10 = [cuberotated2dy[6], cuberotated2dy[2]]
x11 = [cuberotated2dx[5], cuberotated2dx[1]]
y11 = [cuberotated2dy[5], cuberotated2dy[1]]
x12 = [cuberotated2dx[7], cuberotated2dx[3]]
y12 = [cuberotated2dy[7], cuberotated2dy[3]]

x13 = [cube2dx[0], cube2dx[1]]
y13 = [cube2dy[0], cube2dy[1]]
x14 = [cube2dx[0], cube2dx[2]]
y14 = [cube2dy[0], cube2dy[2]]
x15 = [cube2dx[3], cube2dx[2]]
y15 = [cube2dy[3], cube2dy[2]]
x16 = [cube2dx[3], cube2dx[1]]
y16 = [cube2dy[3], cube2dy[1]]

x17 = [cube2dx[4], cube2dx[5]]
y17 = [cube2dy[4], cube2dy[5]]
x18 = [cube2dx[4], cube2dx[6]]
y18 = [cube2dy[4], cube2dy[6]]
x19 = [cube2dx[7], cube2dx[5]]
y19 = [cube2dy[7], cube2dy[5]]
x20 = [cube2dx[7], cube2dx[6]]
y20 = [cube2dy[7], cube2dy[6]]

x21 = [cube2dx[4], cube2dx[0]]
y21 = [cube2dy[4], cube2dy[0]]
x22 = [cube2dx[6], cube2dx[2]]
y22 = [cube2dy[6], cube2dy[2]]
x23 = [cube2dx[5], cube2dx[1]]
y23 = [cube2dy[5], cube2dy[1]]
x24 = [cube2dx[7], cube2dx[3]]
y24 = [cube2dy[7], cube2dy[3]]

plt.subplot(122).set_title('After rotation')
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.plot(x6, y6)
plt.plot(x7, y7)
plt.plot(x8, y8)
plt.plot(x9, y9)
plt.plot(x10, y10)
plt.plot(x11, y11)
plt.plot(x12, y12)
plt.axis('off')

plt.subplot(121).set_title('Before rotation')
plt.plot(x13, y13)
plt.plot(x14, y14)
plt.plot(x15, y15)
plt.plot(x16, y16)
plt.plot(x17, y17)
plt.plot(x18, y18)
plt.plot(x19, y19)
plt.plot(x20, y20)
plt.plot(x21, y21)
plt.plot(x22, y22)
plt.plot(x23, y23)
plt.plot(x24, y24)
plt.axis('off')

plt.show()

# ===============================================================

# plt.xlim(-1, 1)
# plt.ylim(-1, 1)
# plt.scatter(cube2dx, cube2dy)
# plt.scatter(cuberotated2dx, cuberotated2dy)
