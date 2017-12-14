from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

time = 1000

def init():
    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,700,0,700,-100,100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def Border(w=10):
    glLoadIdentity()
    glLineWidth(w)
    glTranslate(350,350,0)
    glBegin(GL_LINE_STRIP)
    for x in range(361):
        glVertex(300*sin(x*pi/180),300*cos(x*pi/180),0)
    glEnd()

def Steps(w=5):
    glLoadIdentity()
    glLineWidth(0.5*w)
    glTranslate(350,350,0)
    glBegin(GL_LINES)
    for x in range(0,361,6):
        glVertex(280*sin(x*pi/180),280*cos(x*pi/180),0)
        glVertex(300*sin(x*pi/180),300*cos(x*pi/180),0)
    glEnd()
    glLineWidth(3*w)
    glBegin(GL_LINES)
    for x in range(0,361,30):
        glVertex(270*sin(x*pi/180),270*cos(x*pi/180),0)
        glVertex(300*sin(x*pi/180),300*cos(x*pi/180),0)
    glEnd()
    glColor(0,0,0)
    for i in range(0,361,30):
        x=252*sin(i*pi/180)+334
        y=242*cos(i*pi/180)+330
        if i:
            drawText(str(int(i/30)),x,y,0.4,4)

def drawText(string, x, y,s=0.3,w=2):
    glLineWidth(w)
    glLoadIdentity()
    glTranslate(x,y,0)
    glScale(s,s,1)
    string = string.encode()
    for c in string:
            glutStrokeCharacter(GLUT_STROKE_ROMAN , c)

thetaS=0
def SecPointer(length=240,w=12):
    global thetaS
    glLoadIdentity()
    glLineWidth(w)
    glTranslate(350,350,0)
    glRotate(thetaS,0,0,1)
    glBegin(GL_LINES)
    glVertex(0,0,0)
    glVertex(0,length,0)
    glEnd()
    thetaS-=6

thetaM=0
def MinPointer(length=240,w=12):
    global thetaM,thetaS
    glLoadIdentity()
    glLineWidth(w)
    glTranslate(350,350,0)
    glRotate(thetaM,0,0,1)
    glBegin(GL_LINES)
    glVertex(0,0,0)
    glVertex(0,length,0)
    glEnd()
    thetaM=6*(thetaS/360)

thetaH=0
def HrPointer(length=220,w=15):
    global thetaH,thetaS,thetaM
    glLoadIdentity()
    glLineWidth(w)
    glTranslate(350,350,0)
    glRotate(thetaH,0,0,1)
    glBegin(GL_LINES)
    glVertex(0,0,0)
    glVertex(0,length,0)
    glEnd()
    thetaH=30*(thetaM/360)

    
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor(0,0,1)
    Steps()
    glColor(0,0,0.2)
    drawText("QUARTZ",310,220,0.16,1)
    glColor(1,0.3,0.3)
    SecPointer(275,2) #Seconds
    glColor(0.5,0.5,1)
    MinPointer(250,4)
    glColor(0.1,0.1,0.5)
    HrPointer(220,15)
    glColor(0,0,0)
    Border()
    glLoadIdentity()
    glTranslate(350,350,0)
    glColor(0,0,0)
    glutSolidSphere(8,70,10)
    glutSwapBuffers()

def Timer(v):
    draw()
    glutTimerFunc(time,Timer,1)
    
glutInit()
glutInitWindowSize(700,700)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutCreateWindow(b"Clock")
init()
glutDisplayFunc(draw)
glutTimerFunc(time,Timer,1)
glutMainLoop()
