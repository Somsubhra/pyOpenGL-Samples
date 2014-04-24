# Python imports
from sys import exit
from math import *

# OpenGL imports
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print "OpenGL wrapper for python not found"


# The sphere class
class Sphere:

    # Constructor for the sphere class
    def __init__(self, radius):

        # The radius of the sphere
        self.radius = radius

        self.x = 0.525731112119133606
        self.z = 0.850650808352039932

        self.vdata = [
            [-self.x, 0.0, self.z],
            [self.x, 0.0, self.z],
            [-self.x, 0.0, -self.z],
            [self.x, 0.0, -self.z],
            [0.0, self.z, self.x],
            [0.0, self.z, -self.x],
            [0.0, -self.z, self.x],
            [0.0, -self.z, -self.x],
            [self.z, self.x, 0.0],
            [-self.z, self.x, 0.0],
            [self.z, -self.x, 0.0],
            [-self.z, -self.x, 0.0]
        ]

        self.tindices = [
            [0, 4, 1],
            [0, 9, 4],
            [9, 5, 4],
            [4, 5, 8],
            [4, 8, 1],
            [8, 10, 1],
            [8, 3, 10],
            [5, 3, 8],
            [5, 2, 3],
            [2, 7, 3],
            [7, 10, 3],
            [7, 6, 10],
            [7, 11, 6],
            [11, 0, 6],
            [0, 1, 6],
            [6, 1, 10],
            [9, 0, 11],
            [9, 11, 2],
            [9, 2, 5],
            [7, 2, 11]
        ]

        self.divs = 10

    # Display the sphere
    def display(self):

        glClear(GL_COLOR_BUFFER_BIT)

        glPushMatrix()

        # Draw the sphere
        self.draw()

        glPopMatrix()

        glutSwapBuffers()

    # The reshape callback
    def reshape(self, w, h):

        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w / h, 1.0, 20.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0)

    # Draw the sphere
    def draw(self):

        glBegin(GL_TRIANGLES)

        for i in range(0, 20):
            x = self.tindices[i][0]
            y = self.tindices[i][1]
            z = self.tindices[i][2]
            self.draw_triangle(self.vdata[x], self.vdata[y], self.vdata[z], self.divs, self.radius)

        glEnd()

    # Draw the triangle
    def draw_triangle(self, m, n, o, div, r):

        if div <= 0:

            glNormal3fv(m)
            glVertex3f(m[0] * r, m[1] * r, m[2] * r)

            glNormal3fv(n)
            glVertex3f(n[0] * r, n[1] * r, n[2] * r)

            glNormal3fv(o)
            glVertex3f(o[0] * r, o[1] * r, o[2] * r)

        else:

            mn = [0.0, 0.0, 0.0]
            no = [0.0, 0.0, 0.0]
            mo = [0.0, 0.0, 0.0]

            for i in range(0, 3):
                mn[i] = (m[i] + n[i]) / 2
                no[i] = (n[i] + o[i]) / 2
                mo[i] = (m[i] + o[i]) / 2

            self.normalize(mn)
            self.normalize(no)
            self.normalize(mo)

            self.draw_triangle(m, mn, mo, div - 1, r)
            self.draw_triangle(n, no, mn, div - 1, r)
            self.draw_triangle(o, mo, no, div - 1, r)
            self.draw_triangle(mn, no, mo, div - 1, r)

    # Normalize a vector
    def normalize(self, a):

        magnitude = sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2])
        a[0] /= magnitude
        a[1] /= magnitude
        a[2] /= magnitude

    # Keyboard controls
    def control(self, key, x, y):
        if key == chr(27):
            sys.exit()

        glutPostRedisplay()


# The main function
def main():

    # Initialize the OpenGL pipeline
    glutInit(sys.argv)

    # Set OpenGL display mode
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)

    # Set the Window size and position
    glutInitWindowSize(600, 500)
    glutInitWindowPosition(0, 0)

    # Create the window with given title
    glutCreateWindow('Sphere')

    # Set background color to black
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # Set shade model
    glShadeModel(GL_SMOOTH)

    # Instantiate the sphere object
    s = Sphere(1.0)

    # Set the callback function for display
    glutDisplayFunc(s.display)

    # Set the callback function for reshape
    glutReshapeFunc(s.reshape)

    # Set the callback function for keyboard control
    glutKeyboardFunc(s.control)

    # Run the OpenGL main loop
    glutMainLoop()


# Call the main function
if __name__ == '__main__':
    main()