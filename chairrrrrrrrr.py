from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1, 1, 1, 1)   # clear background
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(50,1,0.1,50)
    gluLookAt(10, 10, 10 ,0, 0, 0, 0, 1, 0 )
def seat():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(0, 0, 0)
    glTranslate(0, 0, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(0, 0, 0)
    glTranslate(-2.2, 1.7, -0.5)
    glScale(0.2, 0.6, 0.5)
    glutSolidCube(5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(0, 0, 0)
    glTranslate(2, -0.48, 0.3)
    glScale(0.1, 0.4, 0.1)
    glutSolidCube(5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(0, 0, 0)
    glTranslate(2, -0.5, 1.9)
    glScale(0.1, 0.4, 0.1)
    glutSolidCube(5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor3f(0, 0, 0)
    glTranslate(-.3, -0.56, 1.6)
    glScale(0.1, 0.4, 0.1)
    glutSolidCube(5)

    glPopAttrib()
    glPopMatrix()
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    seat()
    glTranslate(-2.2, 0,-5.5)
    seat()



    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"program")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myInit()
glutMainLoop()

