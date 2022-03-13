from matplotlib import pyplot as plt
from Robot import Robot

robot = Robot([7.0, 270], [4.0, 270], [3.5, 270])
if robot.move_robot(5, 6):
    fore = robot.curr_forearm_pos()
    bicep = robot.curr_bicep_pos()

    x_values = [0, bicep.x, fore.x]

    y_values = [0, bicep.y, fore.y]

    plt.plot(x_values, y_values)
    plt.show()