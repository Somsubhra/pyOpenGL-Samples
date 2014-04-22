# OpenGL imports for python

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print "OpenGL wrapper for python not found"

class Humanoid:

    def __init__(self):
        # Head angle horizontally(left/right)
        self.head_angle_lr = 0

        # Head angle vertically(up/down)
        self.head_angle_ud = 0

        # Neck angle horizontally
        self.neck_angle_lr = 0

        # Neck angle vertically
        self.neck_angle_ud = 0

        # Right Shoulder angle horizontally(left/right)
        self.right_shoulder_angle_lr = 0

        # Right Shoulder angle vertically(up/down)
        self.right_shoulder_angle_ud = 0

        # Left Shoulder angle horizontally(left/right)
        self.left_shoulder_angle_lr = 0

        # Left Shoulder angle vertically(up/down)
        self.left_shoulder_angle_ud = 0

        # Right Ankle angle vertically
        self.right_ankle_angle_ud = 0

        # Left Ankle angle vertically
        self.left_ankle_angle_ud = 0

        # Torso angle vertically(up/down)
        self.torso_angle_ud = 0

        # Torso angle horizontally(left/right)
        self.torso_angle_lr = 0

        # Left leg angle vertically(up/down)
        self.left_leg_ud = 0

        # Right leg angle vertically(up/down)
        self.right_leg_ud = 0

        # Left knee angle vertically(up/down)
        self.left_knee_ud = 0

        # Right knee angle vertically(up/down)
        self.right_knee_ud = 0

    def display(self):
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def controls(self):
        pass


def main():
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    glutInitWindowSize(600, 500)
    glutInitWindowPosition(0, 0)

    glutCreateWindow('Humanoid')

    h = Humanoid()

    glutDisplayFunc(h.display)
    glutIdleFunc(h.display)
    glutKeyboardFunc(h.controls())

    glutMainLoop()

if __name__ == '__main__':
    main()