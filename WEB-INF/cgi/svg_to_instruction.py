from bs4 import BeautifulSoup as bs # This is my personal favorite library for HTML and XML in Python
import re
import math
import time
import sys

#FULL_REV = 4.85
DEF_SPEED = 65
SCALE = 3/1000

def svg_to_lines(file_name):
    '''
    This method takes one parameter, an xml file_name. It extracts svg tags, and returns and list containing a tuple
    with a command and a list of points, which are also tuples.
    [(command, [(point1x, point1y), (point2x, point2y), ..., (pointNx, pointNy)]),]
    
    it's just lists of tuples all the way down
    '''
    #load file_name and get svg tag
    soup = bs(open(file_name), 'xml')
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

def get_theta(x1, y1, x2, y2, angle):
    '''
        takes four arguments x1, y1, x2, y2
        returns the angle in degrees of arctan(y2-y1, x2-x1)
        
        Use this to convert from cartesian coordinates to polar coordinates
    '''
    #print('in get_theta @ (',x1,',',y1,') going to (',x2,',',y2,')')
    r = math.atan2(y2-y1, x2-x1)
    #print('arctan(', y2-y1, '/', x2-x1, '=', r*180/math.pi)
    r = r*180/math.pi
    r = r-angle
    return r

def get_distance(x1, y1, x2, y2):
    '''
        takes four arguments x1, y1, x2, y2
        returns the distance between the points (in no units or maybe all units)
        
        Use this to convert from cartesian coordinates to polar coordinates
    '''
    x, y = x2 - x1, y2-y1
    return(math.sqrt(math.pow(x, 2) + math.pow(y, 2)))

def cart_to_polar(x1, y1, x2, y2,state):
    '''
        takes four arguments x1, y1, x2, y2
        returns a dictionary with the angle in radians and distance between the points 
        {'dist': 2.8284271247461903, 'theta': 0.7853981633974483}
        
        Use this to convert from cartesian coordinates to polar coordinates
    '''
    return({'theta': get_theta(x1, y1, x2, y2,state.angle), 'dist': get_distance(x1, y1, x2, y2)})

def go(distance):
    ''' 
        Given an integer, distance, this returns a string of the backward command of the given distance
    '''
    speed = DEF_SPEED
    dur = distance * SCALE
    # UNCOMMENT ONE OF THESE LINES ON ROBOT
    #robot.forward(speed, dur)
    return "robot.backward({s}, {d})\n".format(s = speed, d = dur)
  
def rotate(theta):
    ''' 
        Given an integer, theta, this returns a string of the rotate command of the given angle, theta
    '''
    # UNCOMMENT ONE OF THESE LINES ON ROBOT
    #robot.forward(speed, dur)
    return "robot.rotate({t})\n".format(t=theta)


def init_file():
    '''
    Taking no parameters. This returns a string with the necessary imports and setup
    '''
    s = ('import time\n'
          'import Robot\n\n'
          'LEFT_TRIM = 0\n'
          'RIGHT_TRIM = 0\n\n'
          '#initialize the robot\n'
          'robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)\n'
          'DEF_SPEED = 65\n\n\n'
          '#the commands begin now\n'
        )
    # this try-catch block is pointless right now, but should be useful in the distant future, the year 2000
    return s

    
def go_to(state, points):
    '''
        Takes three arguments, state, points, and absolute=True
        point should be a list of 4-tuples representing x1,y1,x2,y2 respectively
        returns a state and a string
    '''
    #s is the string we return
    s = ""
    
    if type(points) is not tuple:
        print('improper argument type: ', type(points), ',', points)
        return s
    if len(points) != 4:
        print('improper number of points in argument: ', len(points), 'found ,', points)
        return s
    x1 = points[0]
    y1 = points[1]
    x2 = points[2]
    y2 = points[3]
    
    if x1 != state.x or y1 != state.y:
        print('state does not match command: (',state.x,',',state.y,') != (',x1,',',x2,') \ignorning, output may suffer' )
    
    # get vector in polar cordinates
    polar = cart_to_polar(x1, y1, x2, y2,state)
    # rotate angle
    #print('theta =',polar['theta'],'distance =',polar['dist'],'state =',state.x,state.y,state.angle,'target =',x2,y2)
    
    # append the two lines of commands to the string
    s += rotate(polar['theta']) 
    s += go(polar['dist'])
    
    # update and return? state, now at new point and angled in direction just travelled 
    state.x = x2 
    state.y = y2 
    state.angle += polar['theta'] 
    
    return state, s

def robot_convert(file_name,scale=3):
    '''
        convert takes an .svg file name, file_name, and an integer, scale
        it creates or over writes a file named 'script.py', which contains robot commands in python,
        from the given svg file, and scales the drawing according to scale
    '''
    scale = scale/1000
    SCALE = scale
    
    #open the file we're writing to
    file = open('../../network/send/script.py','w')
    file.write(init_file())
    
    try:
        state = State()
        lines = svg_to_lines(file_name)
    except Exception as e:
        print('Error opening file \'', file_name, '\'', 'due to ', e)
        raise e
    try:
        if len(lines) <= 0:
            print('lines not found in file')
            return

        if lines[0][0] != 0 and lines[0][1] != 0:
            #print('Moving to starting point (',lines[0][0],',',lines[0][1],') from origin')
            state,s = go_to(state, (0,0,lines[0][0],lines[0][1]))
            file.write(s)

        for line in lines:
            #print(line)
            if len(line) == 0:
                pass
            else:
                #print('moving from (',line[0],',',line[1],') to (',line[2],',',line[3],')')
                state,s = go_to(state, line)
                file.write(s)
    except Exception as e:
        print('File not written due to following exception')
        print(e)
        return False
            
    # close our file
    file.close()
    return True
