import time

# Import the Robot.py file (must be in the same directory as this file!).
import Robot


LEFT_TRIM   = 0
RIGHT_TRIM  = 0


# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

#robot.forward(100, 1.0)
#robot.left(100, 1.0)
#robot.right(100, 1.0)

def go(max_speed, duration):
    if duration < 0.5:
        robot.forward(max_speed, duration)
    else:
        robot.forward(max_speed/4, 0.125)
        robot.forward(max_speed/2, 0.125)
        robot.forward(max_speed, (duration - 0.5))
        robot.forward(max_speed/4, 0.125)
        robot.forward(max_speed/2, 0.125)

#go(100, 1)
#robot.arc(100,50, 6)

def square(speed, duration):
    for i in range(0,4):
        robot.right(speed, .80)
        go(speed, duration)


def triangle(speed, duration):
    for i in range(0,3):
        robot.right(speed, 1.3)
        robot.forward(speed, duration)

def circle(size, direction = 'clockwise'):
    inner = size*10
        robot.forward(max_speed/4, 0.125)
        robot.forward(max_speed/2, 0.125)
        robot.forward(max_speed, (duration - 0.5))
        robot.forward(max_speed/4, 0.125)
        robot.forward(max_speed/2, 0.125)

#go(100, 1)
#robot.arc(100,50, 6)

def square(speed, duration):
    for i in range(0,4):
        robot.right(speed, .80)
        go(speed, duration)


def triangle(speed, duration):
    for i in range(0,3):
        robot.right(speed, 1.3)
        robot.forward(speed, duration)

def circle(size, direction = 'clockwise'):

    inner = size*10
    outer = 50
    duration = (size+1) * 7
    if direction == 'clockwise':
        robot.arc(inner, outer, duration)
    else:
        robot.arc(inner, outer, duration

)
#square(50, 2)
triangle(50, 1.6)
#circle(2)

