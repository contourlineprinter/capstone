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
rotTime = .932

def rectangle(len, wid):
        robot.forward(50, len)
        robot.right(50, rotTime)
        robot.forward(50, wid)
        robot.right(50, rotTime)
        robot.forward(50, len)
        robot.right(50, rotTime)
        robot.forward(50, wid)

rectangle(2,1)
