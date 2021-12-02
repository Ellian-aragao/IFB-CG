from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
import numpy as np
import random as rd
 
import sys
 
 
altura = 500
largura = 500
ratio = 1
 
posicoes_dos_pointers = []
 
class PointerWithBit:
   def __init__(self, x, y, bit):
       self.x = x
       self.y = y
       self.bit = bit
 
class Peixinho:
   def __init__(self):
       self._olho()
       self._corpo()
       self._nadadeira()
       self._rabo()
 
   def _olho(self):
       glBegin(GL_TRIANGLE_FAN)
       glVertex2f(-14.5, 1)
       for point in range(101):
           angle = 2 * np.pi * point / 100
           glVertex2f(np.cos(angle) * 1.6 - 14.5, np.sin(angle) * 1.6 + 1)
       glEnd()
 
       glBegin(GL_LINE_LOOP)
       for point in range(100):
           angle = 2 * np.pi * point / 100
           glVertex2f(np.cos(angle) * 1.6 - 14.5, np.sin(angle) * 1.6 + 1)
       glEnd()
 
       glBegin(GL_TRIANGLE_FAN)
       glVertex2f(-14.5, 1)
       for point in range(101):
           angle = 2 * np.pi * point / 100
           glVertex2f(np.cos(angle) * 0.75 - 14.5, np.sin(angle) * 0.72 + 1)
       glEnd()
 
   def _corpo(self):
       glBegin(GL_TRIANGLE_STRIP)
 
       glVertex2f(-18, 2)
       glVertex2f(-15, 3.5)
       glVertex2f(-16, -2)
 
       glVertex2f(-10, 7)
 
       glVertex2f(-10, -5)
 
       glVertex2f(2, 12)
 
       glVertex2f(1, -6)
 
       glVertex2f(12, 14)
 
       glVertex2f(20, -3)
 
       glVertex2f(24, 12)
 
       glVertex2f(30, 2)
 
       glVertex2f(31, 10)
       glEnd()
 
   def _rabo(self):
       glBegin(GL_TRIANGLE_FAN)
 
       glVertex2f(25, 4)
       glVertex2f(40, 29)
       glVertex2f(45, 28)
       glVertex2f(50, 25)
       glVertex2f(53, 19)
       glVertex2f(54, 15)
       glVertex2f(54, 10)
       glVertex2f(54, 6)
       glVertex2f(53, 1)
       glVertex2f(50, -5)
       glEnd()
 
   def _nadadeira(self):
       glBegin(GL_TRIANGLE_FAN)
 
       glVertex2f(0, 1)
       glVertex2f(7, 9)
       glVertex2f(8, 9)
       glVertex2f(10, 8)
       glVertex2f(11, 6)
       glVertex2f(11, 4)
       glVertex2f(11, 2)
       glVertex2f(10, 0)
       glVertex2f(9, -2)
 
       glEnd()
 
 
def quadradinho(x, y):
   glBegin(GL_QUADS)
   glVertex2f(x - 2.5, y - 2.5)
   glVertex2f(x - 2.5, y + 2.5)
   glVertex2f(x + 2.5, y + 2.5)
   glVertex2f(x + 2.5, y - 2.5)
   glEnd()
 
 
def bolinha(x, y):
   glBegin(GL_TRIANGLE_FAN)
   glVertex2f(x, y)
   for point in range(100):
       angle = 2 * np.pi * point / 100
       glVertex2f(np.cos(angle) * 3 + x, np.sin(angle) * 3 + y)
   glEnd()
 
 
def display_callback():
   glClearColor(1.0, 1.0, 1.0, 1.0)
   glClear(GL_COLOR_BUFFER_BIT)
 
   glViewport(0, 0, int(largura), int(altura))
   tela_1_peixinho()
 
   linha_divisoria_central()
 
   glViewport(int(largura), 0, int(largura), int(altura))
   tela_2_bolinha_ou_quadradinho()
 
   glFlush()
 
 
def linha_divisoria_central():
   glLineWidth(3)
   glBegin(GL_LINES)
   glColor3f(0, 0, 0)
   glVertex2f(100 * ratio, altura)
   glVertex2f(100 * ratio, 0)
   glEnd()
   glLineWidth(1)
 
 
def tela_2_bolinha_ou_quadradinho():
   glPushMatrix()
   glTranslatef(10, 90, 0)
   glColor(0, 0, 0)
   glScalef(0.05, 0.05, 0)
   glLineWidth(2)
   glutStrokeCharacter(GLUT_STROKE_ROMAN, 50)
   glPopMatrix()
 
   desenha_bolinhas_e_quadradinhos()
 
 
def desenha_bolinhas_e_quadradinhos():
   glPushMatrix()
 
   for pointer in posicoes_dos_pointers:
       x = pointer.x
       y = pointer.y
 
       if pointer.bit:
           bolinha(x, y)
       else:
           quadradinho(x, y)
       glFlush()
 
   glPopMatrix()
 
 
def tela_1_peixinho():
   glPushMatrix()
   glTranslatef(10, 90, 0)
   glColor(0, 0, 0)
   glScalef(0.05, 0.05, 0)
   glLineWidth(2)
   glutStrokeCharacter(GLUT_STROKE_ROMAN, 49)
   glPopMatrix()
 
   desenha_peixinho()
 
 
def desenha_peixinho():
   glPushMatrix()
   glTranslatef(35, 45, 0)
   glScalef(1, 1, 0)
   Peixinho()
   glPopMatrix()
 
 
def mouse_callback(button, state, x, y):
   if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
       viewport = glGetIntegerv(GL_VIEWPORT, None)
       modelview = glGetDoublev(GL_MODELVIEW_MATRIX, None)
       projection = glGetDoublev(GL_PROJECTION_MATRIX, None)
 
       (ax, ay, _) = gluUnProject(x, viewport[3] - y, 0, modelview, projection, viewport)
 
       posicoes_dos_pointers.append(PointerWithBit(ax, ay,rd.getrandbits(1)))
       glutPostRedisplay()
 
 
def main():
   glutInit(sys.argv)
   glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
   glutInitWindowSize(1000, 500)
   glutCreateWindow("Peixinhos e bolinhas/quadradinhos no OpenGL de Ellian Aragao Dias")
 
   glClearColor(1.0, 1.0, 1.0, 1.0)
   glOrtho(0, 100, 0, 100, -1, 1)
   glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
 
   glutDisplayFunc(display_callback)
   glutMouseFunc(mouse_callback)
   glutMainLoop()
 
 
if __name__ == "__main__":
   main()
 


