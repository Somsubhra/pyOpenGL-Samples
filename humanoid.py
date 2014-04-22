# OpenGL imports for python
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print "OpenGL wrapper for python not found"


# The humanoid class
class Humanoid:

    # Constructor for the humanoid class
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

    # The display function for the humanoid
    def display(self):
        # Enable the Depth test
        glEnable(GL_DEPTH_TEST)

        # Set OpenGL parameters
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Set the matrix mode to ModelView
        glMatrixMode(GL_MODELVIEW)

        # Load the identity matrix
        glLoadIdentity()

    # Te keyboard controls for the humanoid
    def controls(self):
        pass


def main():

    # Initialize the OpenGL pipeline
    glutInit(sys.argv)

    # Set OpenGL display mode
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

    # Set the Window size and position
    glutInitWindowSize(600, 500)
    glutInitWindowPosition(0, 0)

    # Create the window with given title
    glutCreateWindow('Humanoid')

    # Instantiate the humanoid
    h = Humanoid()

    # Attach the callback for the display function
    glutDisplayFunc(h.display)

    # Attach the callback for the idle function
    glutIdleFunc(h.display)

    # Attach the callback function for keyboard functions
    glutKeyboardFunc(h.controls)

    # Run the OpenGL main loop
    glutMainLoop()

# Call the main function
if __name__ == '__main__':
    main()