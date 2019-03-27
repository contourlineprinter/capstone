import time

# Import the Robot.py file (must be in the same directory as this file!).
import Robot


LEFT_TRIM   = -10
RIGHT_TRIM  = 0


# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

robot.arc(75,0,6.25)
'''
def circle(size): # direction = 'clockwise'

    inner = size*10
    outer = 50
    duration = (size+1) * 7
    if direction == 'clockwise':
        robot.arc(inner, outer, duration)
    else:
        robot.arc(inner, outer, duration


circle(1)
'''


