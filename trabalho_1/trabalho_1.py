from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import random as rd

height = 500
width = 500
ratio = 1

teclaT = False
teclaR = False
teclaS = False


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-50, 50, -50, 50, -1, 1)


def reshape(w, h):
    global width
    width = w

    global height
    height = h

    global ratio

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (w <= h):
        ratio = height / width
        glOrtho(-50, 50, -50 * ratio, 50 * ratio, -1, 1)
    else:
        ratio = width / height
        glOrtho(-50 * ratio, 50 * ratio, -50, 50, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def resetTeclas():
    global teclaR, teclaS, teclaT
    teclaR = False
    teclaS = False
    teclaT = False
    
def keyboard(key, x, y):
    if ord(key) == ord('i') or ord(key) == ord('I'):
        resetTeclas()
        glLoadIdentity()
        glutPostRedisplay()
    if ord(key) == ord('m') or ord(key) == ord('M'):
        resetTeclas()
        glScalef(-1, 1, 0)
        glutPostRedisplay()
    if ord(key) == ord('r') or ord(key) == ord('R'):
        resetTeclas()
        global teclaR
        teclaR = True
    if ord(key) == ord('s') or ord(key) == ord('S'):
        resetTeclas()
        global teclaS
        teclaS = True
    if ord(key) == ord('t') or ord(key) == ord('T'):
        resetTeclas()
        global teclaT
        teclaT = True
    tecla_esc = 27
    if ord(key) == tecla_esc:
        glutLeaveMainLoop()


def specialKeys(key, mouseX, mouseY):
    if teclaT:
        if key == GLUT_KEY_LEFT:
            glTranslatef(-5, 0, 0)
            glutPostRedisplay()
        if key == GLUT_KEY_RIGHT:
            glTranslatef(5, 0, 0)
            glutPostRedisplay()
        if key == GLUT_KEY_UP:
            glTranslatef(0, 5, 0)
            glutPostRedisplay()
        if key == GLUT_KEY_DOWN:
            glTranslatef(0, -5, 0)
            glutPostRedisplay()
    if teclaR:
        if key == GLUT_KEY_UP:
            glRotatef(5, 0, 0, 1)
            glutPostRedisplay()
        if key == GLUT_KEY_DOWN:
            glRotatef(-5, 0, 0, 1)
            glutPostRedisplay()
    if teclaS:
        if key == GLUT_KEY_UP:
            glScalef(2, 2, 0)
            glutPostRedisplay()
        if key == GLUT_KEY_DOWN:
            glScalef(0.5, 0.5, 0)
            glutPostRedisplay()


def draw_square(x = 0, y = 0):
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 0)
    glVertex2f(x + 2.5, y + 2.5)
    glVertex2f(x - 2.5, y + 2.5)
    glVertex2f(x - 2.5, y - 2.5)
    glEnd()
    glFlush()


def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    draw_square()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow(
        "Trabalho 1 - Joao Vitor Souza Rezende e Ellian Aragao"
    )
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(specialKeys)
    glutMainLoop()


if __name__ == "__main__":
    main()
