from matplotlib import pyplot as plt
from Robot import Robot

robot = Robot([1, 270], [1.0, 270], [2.0, 270])
robot.move_robot(1, 1)

fore = robot.curr_forearm_pos()
bicep = robot.curr_bicep_pos()

x_values = [0, bicep.x, fore.x]

y_values = [0, bicep.y, fore.y]

plt.plot(x_values, y_values)
plt.show()