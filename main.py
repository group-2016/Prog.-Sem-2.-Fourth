#Логунов Алексей
#Группа P3175
#ДЗ номер 4
#Поворот куба (без графики)

import math

#класс куба
class Cube:
    halfLength = 0
    angles = [0, 0, 0]
    vertices = []

    def __init__(self, halfLength):
        self.length = halfLength
        self.vertices = \
        [
            [-halfLength, -halfLength, -halfLength],
            [-halfLength, -halfLength, halfLength],
            [-halfLength, halfLength, -halfLength],
            [-halfLength, halfLength, halfLength],
            [-halfLength, -halfLength, -halfLength],
            [halfLength, -halfLength, halfLength],
            [halfLength, halfLength, -halfLength],
            [halfLength, halfLength, halfLength],
        ]

    # поворот вокруг оси Х
    def rotateX(self, angle):
        cos = float(math.cos(angle))
        sin = float(math.sin(angle))
        for num in range(8):
            vertex = self.vertices[num]
            self.vertices[num] = [vertex[0], (cos * vertex[1]) - (sin * vertex[2]), sin * vertex[1] + cos * vertex[2]]
        self.angles[0] = angle

    # поворот вокруг оси Y
    def rotateY(self, angle):
        cos = math.cos(angle)
        sin = math.sin(angle)
        for num in range(8):
            vertex = self.vertices[num]
            self.vertices[num] = [cos * vertex[0] - sin * vertex[2], vertex[1], sin * vertex[0] + cos * vertex[2]]
        self.angles[1] = angle

    # поворот вокруг оси Z
    def rotateZ(self, angle):
        cos = math.cos(angle)
        sin = math.sin(angle)
        for num in range(8):
            vertex = self.vertices[num]
            self.vertices[num] = [cos * vertex[0] - sin * vertex[1], sin * vertex[0] + cos * vertex[1], vertex[2]]
        self.angles[2] = angle



cube = Cube(10)
print(cube.vertices)

#поворот не коммутативен - то есть поворот на одни и те же углы, но в разном порядке, даст разные результаты
cube.rotateX(45)
cube.rotateY(45)
cube.rotateZ(45)
print(cube.vertices)
