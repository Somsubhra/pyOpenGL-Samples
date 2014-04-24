try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print "OpenGL wrapper for python not found"


# The cube class
class Cube:

    # Constructor for the cube class
    def __init__(self):
        self.rotate_y = 0.0
        self.rotate_x = 0.0
        self.scale = 2.0

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glShadeModel(GL_FLAT)

    # The display function
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)

        eqn = [1, 1, 1, 2.6]

        glColor3f(1.0, 1.0, 1.0)
        glLoadIdentity()
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        glClipPlane(GL_CLIP_PLANE0, eqn)
        glEnable(GL_CLIP_PLANE0)

        glScalef(self.scale, self.scale, self.scale)
        glRotatef(self.rotate_y, 0.0, 1.0, 0.0)
        glRotatef(self.rotate_x, 1.0, 0.0, 0.0)
        glutSolidCube(1.0)
        glColor3f(1.0, 0.0, 0.0)
        glutWireCube(1.0)
        glFlush()

    # The reshape function
    def reshape(self, w, h):
        glViewport(0, 0, GLsizei(w), GLsizei(h))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
        glMatrixMode(GL_MODELVIEW)

    def special(self, key, x, y):
        if key == GLUT_KEY_RIGHT:
            self.rotate_y += 5
        if key == GLUT_KEY_LEFT:
            self.rotate_y -= 5
        if key == GLUT_KEY_UP:
            self.rotate_x += 5
        if key == GLUT_KEY_DOWN:
            self.rotate_x -= 5
        glutPostRedisplay()


# The main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Cube")

    cube = Cube()
    cube.init()

    glutDisplayFunc(cube.display)
    glutReshapeFunc(cube.reshape)
    glutSpecialFunc(cube.special)
    glutMainLoop()

# Call the main function
if __name__ == '__main__':
    main()