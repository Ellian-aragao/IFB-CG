from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import random as rd

height = 500
width = 500
ratio = 1

# se tudo der errado observer o glutPostRedisplay()
teclaT = False
teclaR = False
teclaS = False


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(0, 100, 0, 100, -1, 1)


def reshape(w, h):
    global width
    width = w / 2

    global height
    height = h

    global ratio

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (w <= h):
        ratio = height / width
        glOrtho(0, 100, 0, 100 * ratio, -1.0, 1.0)
    else:
        ratio = width / height
        glOrtho(0, 100 * ratio, 0, 100, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(key, x, y):
    # Tecla I
    if ord(key) == ord('i') or ord(key) == ord('I'):
        glLoadIdentity()
        glutPostRedisplay()
    if ord(key) == ord('m') or ord(key) == ord('M'):
        glScalef(1, -1, 0)
        glutPostRedisplay()
    if ord(key) == ord('r') or ord(key) == ord('R'):
        global teclaR
        teclaR = True
    if ord(key) == ord('s') or ord(key) == ord('S'):
        global teclaS
        teclaS = True
    if ord(key) == ord('t') or ord(key) == ord('T'):
        global teclaT
        teclaT = True
    tecla_esc = 27
    if ord(key) == tecla_esc:
        glutLeaveMainLoop()


def specialKeys(key, mouseX, mouseY):
    if teclaT:
        if key == GLUT_KEY_LEFT:
            glTranslatef(-15, 0, 0)
            glutPostRedisplay()
        if key == GLUT_KEY_RIGHT:
            glTranslatef(15, 0, 0)
            glutPostRedisplay()
        if key == GLUT_KEY_UP:
            glTranslatef(0, 15, 0)
            glutPostRedisplay()
        if key == GLUT_KEY_DOWN:
            glTranslatef(0, -15, 0)
            glutPostRedisplay()
    if teclaR:
        if key == GLUT_KEY_UP:
            glRotatef(50, 0, 0, 1)
            glutPostRedisplay()
        if key == GLUT_KEY_DOWN:
            glRotatef(-20, 0, 0, 1)
            glutPostRedisplay()
    if teclaS:
        if key == GLUT_KEY_UP:
            glScalef(1, 1, 0)
            glutPostRedisplay()
        if key == GLUT_KEY_DOWN:
            glScalef(1, 1, 0)
            glutPostRedisplay


def draw_square(x, y):
    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex2f(x + 2.5, y + 2.5)
    glVertex2f(x - 2.5, y + 2.5)
    glVertex2f(x - 2.5, y - 2.5)
    glVertex2f(x + 2.5, y - 2.5)
    glEnd()
    glFlush()


def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # Escreve "1" para a viewport 1
    glPushMatrix()
    draw_square(50, 50)
    glPopMatrix()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 500)
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
