from Segment import Segment
from numpy import cos, arcsin, rad2deg, sin
from point2d import Point2D as p2d
from formulas import *

class Robot:
    def __init__(self, bicep, forearm, wrist):
        self.bicep = Segment(length=bicep[0], servoDegs=bicep[1])
        self.forearm = Segment(length=forearm[0], servoDegs=forearm[1])
        self.wrist = Segment(length=wrist[0], servoDegs=wrist[1])

        self.minRadius = bicep.length - cos(forearm.maxAngle - 90) # Closest arm can move to itself.
        self.maxRadius = bicep.length + forearm.length # Radius of half-circle arm can make


    def calculate_bicep_move_to_final(self, newCoords):

        intersection_points = get_circle_intersections(r0=self.bicep.length,x1=newCoords.x, y1=newCoords.y, r1 = self.forearm.length)
        
        if not intersection_points:
            return False

        op_point = None
        
        if get_distance(self.curr_forearm_pos(), intersection_points[0]) < get_distance(self.curr_forearm_pos(), intersection_points[1]):
            op_point = intersection_points[0]
        else:
            op_point = intersection_points[1]

        return rad2deg(arcsin(op_point.y/self.bicep.length))
        

    def calculate_forearm_move_to_final(self, newCoords):
        return rad2deg(arcsin((self.curr_forearm_pos().y - newCoords.y) / (self.curr_forearm_pos().x - newCoords.x)))

    def calculate_wrist_angle(self):
        return self.forearm.angle + self.bicep.angle - 90

    def curr_forearm_pos(self):
        return p2d(self.bicep.length * cos(self.bicep.angle), self.bicep.length * sin(self.bicep.angle))

    def move_robot(self, newX, newY):
        newCoords = p2d(newX, newY)
        
        newBicepPosition = self.calculate_bicep_move_to_final(newCoords)
        self.bicep.setServoAngle(newBicepPosition)

        newForearmPosition = self.calculate_forearm_move_to_final(newCoords)
        self.forearm.setServoAngle(newForearmPosition)






