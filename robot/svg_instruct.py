

from bs4 import BeautifulSoup as bs # This is my personal favorite library for HTML and XML in Python
import re
import math
import time
import sys

import Robot

LEFT_TRIM   = 0
RIGHT_TRIM  = -1


# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM) # UNCOMMENT THIS LINE ON ROBOT
FULL_REV = 4.85
DEF_SPEED = 85

def svg_to_lines(file_name):
    '''
    This method takes one parameter, an xml file_name. It extracts svg tags, and returns and list containing a tuple
    with a command and a list of points, which are also tuples.
    [(command, [(point1x, point1y), (point2x, point2y), ..., (pointNx, pointNy)]),]
    
    it's just lists of tuples all the way down
    '''
    #load file_name and get svg tag
    soup = bs(open(file_name), 'xml')
    print(soup)
    svg = soup.svg
    lines=[]

    try:
        for line in svg.find_all('line'):
            x1 = int(line.get('x1'))
            y1 = int(line.get('y1'))
            x2 = int(line.get('x2'))
            y2 = int(line.get('y2'))
        
            lines.append((x1,y1,x2,y2))
    except AttributeError as e:
        print(svg)
        raise e
        
    return lines

'''
    Store location (x and y) and angle of robot. May add speed at some point
'''
class State:
    
    '''
        Initialize robot at Origin
        Origin is top left corner of paper with Robot pointing down. Down and Right are positive
        Why it's this way, I can't say
        SVG just liked it better that way
    '''
    def __init__(self, x=0.0, y=0.0, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle

def get_theta(x1, y1, x2, y2):
    '''
        takes four arguments x1, y1, x2, y2
        returns the angle in radians of arctan(y2-y1, x2-x1)
        
        Use this to convert from cartesian coordinates to polar coordinates
    '''
    r = math.atan2(y2-y1, x2-x1)
    r = r*180/math.pi
    return r

def get_distance(x1, y1, x2, y2):
    '''
        takes four arguments x1, y1, x2, y2
        returns the distance between the points (in no units or maybe all units)
        
        Use this to convert from cartesian coordinates to polar coordinates
    '''
    x, y = x2 - x1, y2-y1
    return(math.sqrt(math.pow(x, 2) + math.pow(y, 2)))

def cart_to_polar(x1, y1, x2, y2):
    '''
        takes four arguments x1, y1, x2, y2
        returns a dictionary with the angle in radians and distance between the points 
        {'dist': 2.8284271247461903, 'theta': 0.7853981633974483}
        
        Use this to convert from cartesian coordinates to polar coordinates
    '''
    return({'theta': get_theta(x1, y1, x2, y2), 'dist': get_distance(x1, y1, x2, y2)})

def rotate(theta):
    ''' 
        this is going to be the place where we calibrate our robot, and we enter the real world, translating radians to
        1. direction of rotation (a simple if statement to turn the shortest way)
        2. speed of rotation (This should be fixed)
        3. duration of rotation 
    '''
    rev = FULL_REV # duration for one revolution or 2pi radians
    speed = DEF_SPEED # default speed
    
    #get smallest positive equivolent angle, which should never be needed
    while(theta > math.pi):
        theta = theta - math.pi*2
        
    if theta > math.pi: # rotate left
        #get equivolent negative angle
        dur = ((theta - 2*math.pi) - (2*math.pi)) * rev * -1 #keep time positive! rotate opposite
        robot.left(speed, dur) # UNCOMMENT THIS LINE ON ROBOT
    else: # rotate right
        dur = (theta / (2*math.pi)) * rev # 
        robot.right(speed, dur) # UNCOMMENT THIS LINE ON ROBOT

def go(distance):
    ''' 
        this is going to be the place where we calibrate our robot, and we enter the real world.
        Only two questions here. 
        1. How fast do we go?
        2. For how long?
    '''
    speed = DEF_SPEED
    dur = 12/500 * distance
    robot.forward(speed, dur)# UNCOMMENT THIS LINE ON ROBOT
    
def go_to(state, points):
    '''
        Takes three arguments, state, points, and absolute=True
        point should be a list of 4-tuples representing x1,y1,x2,y2 respectively
    '''
    if type(points) is not tuple:
        print('improper argument type: ', type(points), ',', points)
        return
    if len(points) != 4:
        print('improper number of points in argument: ', len(points), 'found ,', points)
        return
    x1 = points[0]
    y1 = points[1]
    x2 = points[2]
    y2 = points[3]
    
    if x1 != state.x or y1 != state.y:
        print('state does not match command: (',state.x,',',state.y,') != (',x1,',',x2,') \ignorning, output may suffer' )
    
    # get vector in polar cordinates
    polar = cart_to_polar(x1, y1, x2, y2)
    # rotate angle
    print(polar['theta'])
    robot.rotate(polar['theta'])
    #rotate(polar['theta'])
    # go to there
    go(polar['dist'])
    
    # update and return? state, now at new point and angled in direction just travelled 
    state.x = x2 
    state.y = y2 
    state.angle =  polar['theta'] 
    return state

def main():
    try:
        file_name = sys.argv[1]
        state = State()
        lines = svg_to_lines(file_name)
    except Exception as e:
        print('Error opening file \'', file_name, '\'', 'due to ', e)
        raise e
    
    if len(lines) <= 0:
        print('lines not found in file')
        return
    
    if lines[0][0] != 0 and lines[0][1] != 0:
        print('Moving to starting point (',lines[0][0],',',lines[0][1],') from origin')
        state = go_to(state, (0,0,lines[0][0],lines[0][1]))
    
    for line in lines:
        #print(line)
        if len(line) == 0:
            pass
        else:
            print('moving from (',line[0],',',line[1],') to (',line[2],',',line[3],')')
            state = go_to(state, line)


if __name__ == '__main__':
    main()
