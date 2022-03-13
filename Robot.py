from Segment import Segment
from numpy import arctan, cos, rad2deg, sin, arccos
from point2d import Point2D as p2d
from formulas import *

class Robot:
    def __init__(self, bicep, forearm, wrist):
        self.bicep = Segment(length=bicep[0], servoDegs=bicep[1])
        self.forearm = Segment(length=forearm[0], servoDegs=forearm[1])
        self.wrist = Segment(length=wrist[0], servoDegs=wrist[1])

        self.minRadius = self.bicep.length - cos(self.forearm.maxAngle - 90) # Closest arm can move to itself.
        self.maxRadius = self.bicep.length + self.forearm.length # Radius of half-circle arm can make


    def calculate_bicep_move_to_final(self, newCoords):
        part1 = arctan(newCoords.y / newCoords.x)
    
        p2p1 = self.forearm.length*sin(self.forearm.angle)
        p2p2 = self.bicep.length + (self.forearm.length * cos(self.forearm.angle))
        part2 = arctan(p2p1 / p2p2)
        
        return rad2deg(part1 + part2)        

    def calculate_forearm_move_to_final(self, newCoords):
        p1p1 = math.pow(newCoords.x, 2) + math.pow(newCoords.y, 2)

        p1p2 = -1 * (math.pow(self.bicep.length, 2) + math.pow(self.forearm.length, 2))
        
        part1 = p1p1 + p1p2

        part2 = 2 * (self.bicep.length * self.forearm.length)

        total = arccos(part1 / part2)

        return rad2deg(-1 * total)
        

    def calculate_wrist_angle(self):
        # Currently unused
        return self.forearm.angle + self.bicep.angle - 90

    def curr_forearm_pos(self):
        return p2d(self.bicep.length * cos(self.bicep.angle), self.bicep.length * sin(self.bicep.angle))
    def curr_bicep_pos(self):
        return p2d(self.bicep.length*cos(self.bicep.angle), self.bicep.length*sin(self.bicep.angle))

    def move_robot(self, newX, newY):
        newCoords = p2d(newX, newY)
        point_dist = get_distance(p2d(0, 0), newCoords)
    

        if point_dist < self.minRadius or point_dist >= self.maxRadius:
            print("Out of bounds!")
            return False
        

        newForearmPosition = self.calculate_forearm_move_to_final(newCoords)

        self.forearm.setServoAngle(newForearmPosition)

        newBicepPosition = self.calculate_bicep_move_to_final(newCoords)
        
        self.bicep.setServoAngle(newBicepPosition)

        

        return True






