class Segment:
    ''' 
        Object to store current segment length and servo data,
        and move servo
    '''
    def __init__(self, length, servoDegs):
        self.length = length
        self.angle = 90.0
        self.maxAngle = servoDegs / 2

    def setServoAngle(self, newAngle):
        # TODO: Add code to set servo to new angle
        if abs(newAngle) <= self.maxAngle:
            # Move servo to new angle here
            self.angle = newAngle
            return
        return False