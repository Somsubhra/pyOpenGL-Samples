# author: Somsubhra Bairi (201101056)

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

        # Neck angle horizontally
        self.neck_angle_lr = 0

        # Neck angle vertically
        self.neck_angle_ud = 0

        # Right Shoulder angle vertically(up/down)
        self.right_shoulder_angle_ud = 160

        # Left Shoulder angle vertically(up/down)
        self.left_shoulder_angle_ud = 160

        # Right Ankle angle vertically
        self.right_ankle_angle_ud = 0

        # Left Ankle angle vertically
        self.left_ankle_angle_ud = 0

        # Torso angle horizontally(left/right)
        self.torso_angle_lr = 0

        # Left leg angle vertically(up/down)
        self.left_leg_angle_ud = 180

        # Right leg angle vertically(up/down)
        self.right_leg_angle_ud = 180

        # Left knee angle vertically(up/down)
        self.left_knee_angle_ud = 0

        # Right knee angle vertically(up/down)
        self.right_knee_angle_ud = 0

        # Radius of the torso
        self.torso_radius = 0.1

        # Torso length
        self.torso_length = 0.4

        # Upper arm length
        self.upper_arm_length = 0.15

        # Lower arm length
        self.lower_arm_length = 0.15

        # Upper arm width
        self.upper_arm_width = 0.05

        # Lower arm width
        self.lower_arm_width = 0.03

        # Upper leg length
        self.upper_leg_length = 0.2

        # Lower leg length
        self.lower_leg_length = 0.2

        # Upper leg width
        self.upper_leg_width = 0.08

        # Lower leg width
        self.lower_leg_width = 0.06

        # Shoulder width
        self.shoulder_width = 0.2

        # Hip width
        self.hip_width = 0.2

        # X coordinate of head
        self.head_x = 0.1

        # Y coordinate of head
        self.head_y = self.torso_length

        # X coordinate of left upper arm
        self.left_upper_arm_x = -self.torso_radius

        # X coordinate of right upper arm
        self.right_upper_arm_x = self.torso_radius

        # Y coordinate of left upper arm
        self.left_upper_arm_y = self.torso_length

        # Y coordinate of right upper arm
        self.right_upper_arm_y = self.torso_length

        # Y coordinate of left lower arm
        self.left_lower_arm_y = self.lower_arm_length

        # Y coordinate of right lower arm
        self.right_lower_arm_y = self.lower_arm_length

        # X coordinate of left upper leg
        self.left_upper_leg_x = -1.0 * self.hip_width / 2

        # X coordinate of right upper leg
        self.right_upper_leg_x = self.hip_width / 2

        # Y coordinate of left upper leg
        self.left_upper_leg_y = 0

        # Y coordinate of right upper leg
        self.right_upper_leg_y = 0

        # Y coordinate of left lower leg
        self.left_lower_leg_y = self.lower_leg_length

        # Y coordinate of right lower leg
        self.right_lower_leg_y = self.lower_leg_length

        # X coordinate of camera
        self.eye_x = 2.0

        # Y coordinate of camera
        self.eye_y = 2.0

        # Z coordinate of camera
        self.eye_z = 2.0

        # The X coordinate of up vector
        self.up_x = 0.0

        # The Y coordinate of up vector
        self.up_y = 1.0

        # The Z coordinate of up vector
        self.up_z = 0.0

        # The angle of view
        self.angle = 0.0

        # The quadric
        self.p = None

        # Direction of light
        self.direction = [-4.0, 2.0, -1.0, 1.0]

        # Intensity of light
        self.intensity = [0.7, 0.7, 0.0, 0.25]

        # The intensity of ambient light
        self.ambient_intensity = [0.3, 0.3, 0.0, 0.25]

        # State of walk of humanoid
        self.dir = 'front'

    # Initialize
    def init(self):

        self.p = gluNewQuadric()

        gluQuadricDrawStyle(self.p, GLU_LINE)

        # Set background to black
        glClearColor(0.0, 0.0, 0.0, 0.0)

        # Set matrix mode
        glMatrixMode(GL_PROJECTION)

        # Reset matrix
        glLoadIdentity()

        # Set the perspective
        gluPerspective(30, 1.0, 0.0, 100.0)

        # Enable lighting of the scene
        glEnable(GL_LIGHTING)

        # Set light model to ambient
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient_intensity)

        # Enable light number 0
        glEnable(GL_LIGHT0)

        # Setup direction and intensity of light
        glLightfv(GL_LIGHT0, GL_POSITION, self.direction)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.intensity)

        # Set up the material
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # The display function for the humanoid
    def display(self):

        # Set OpenGL parameters
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Set the matrix mode to ModelView
        glMatrixMode(GL_MODELVIEW)

        # Load the identity matrix
        glLoadIdentity()

        # Set the camera position
        self.change_camera_position(self.eye_x, self.eye_y, self.eye_z, self.up_x, self.up_y, self.up_z)

        glColor3f(0.75, 0.75, 0.75)

        glTranslatef(0.0, 0.0, self.angle)

        # Draw the torso
        glRotatef(self.torso_angle_lr, 0.0, 1.0, 0.0)
        self.display_torso()
        glPushMatrix()

        # Draw the head
        glColor3f(1.0, 0.0, 0.0)
        glTranslatef(0.0, self.head_x, 0.0)
        glRotatef(self.neck_angle_ud, 1.0, 0.0, 0.0)
        glRotatef(self.neck_angle_lr, 0.0, 1.0, 0.0)
        glTranslatef(0.0, self.head_y, 0.0)
        self.display_head()

        # Draw left upper arm
        glColor3f(0.0, 1.0, 0.0)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(self.left_upper_arm_x, self.left_upper_arm_y, 0.0)
        glRotatef(self.left_shoulder_angle_ud, 1.0, 0.0, 0.0)
        self.display_upper_arm()

        # Draw left lower arm
        glColor3f(1.0, 0.0, 0.0)
        glTranslatef(0.0, self.left_lower_arm_y, 0.0)
        glRotatef(self.left_ankle_angle_ud, 1.0, 0.0, 0.0)
        self.display_lower_arm()

        # Draw right upper arm
        glColor3f(0.0, 1.0, 0.0)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(self.right_upper_arm_x, self.right_upper_arm_y, 0.0)
        glRotatef(self.right_shoulder_angle_ud, 1.0, 0.0, 0.0)
        self.display_upper_arm()

        # Draw right lower arm
        glColor3f(1.0, 0.0, 0.0)
        glTranslatef(0.0, self.right_lower_arm_y, 0.0)
        glRotatef(self.right_ankle_angle_ud, 1.0, 0.0, 0.0)
        self.display_lower_arm()

        # Draw left upper leg
        glColor3f(0.0, 1.0, 0.0)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(self.left_upper_leg_x, self.left_upper_leg_y, 0.0)
        glRotatef(self.left_leg_angle_ud, 1.0, 0.0, 0.0)
        self.display_upper_leg()

        # Draw left lower leg
        glColor3f(1.0, 0.0, 0.0)
        glTranslatef(0.0, self.left_lower_leg_y, 0.0)
        glRotatef(self.left_knee_angle_ud, 1.0, 0.0, 0.0)
        self.display_lower_leg()

        # Draw right upper leg
        glColor3f(0.0, 1.0, 0.0)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(self.right_upper_leg_x, self.right_upper_leg_y, 0.0)
        glRotatef(self.right_leg_angle_ud, 1.0, 0.0, 0.0)
        self.display_upper_leg()

        # Draw left lwer leg
        glColor3f(1.0, 0.0, 0.0)
        glTranslatef(0.0, self.left_lower_leg_y, 0.0)
        glRotatef(self.right_knee_angle_ud, 1.0, 0.0, 0.0)
        self.display_lower_leg()

        glPopMatrix()

        glFlush()

    # Change camera position
    def change_camera_position(self, eye_x, eye_y, eye_z, up_x, up_y, up_z):
        gluLookAt(eye_x, eye_y, eye_z, 0.0, 0.0, 0.0, up_x, up_y, up_z)

    # Display the head of humanoid
    def display_head(self):
        glPushMatrix()
        glRotatef(90, 1.0, 0.0, 0.0)
        glutSolidSphere(0.1, 100, 100)
        glPopMatrix()

    # Display the torso of humanoid
    def display_torso(self):
        glPushMatrix()
        glRotatef(-90.0, 1.0, 0.0, 0.0)
        gluCylinder(self.p, self.torso_radius, self.torso_radius, self.torso_length, 100, 100)
        glPopMatrix()

    # Display the upper arm of humanoid
    def display_upper_arm(self):
        glPushMatrix()
        glTranslatef(0.0, 0.5 * self.upper_arm_length, 0.0)
        glScalef(self.upper_arm_width, self.upper_arm_length, self.upper_arm_width)
        glutSolidCube(1.0)
        glPopMatrix()

    # Display the lower arm of humanoid
    def display_lower_arm(self):
        glPushMatrix()
        glTranslatef(0.0, 0.5 * self.upper_arm_length, 0.0)
        glScalef(self.lower_arm_width, self.lower_arm_length, self.lower_arm_width)
        glutSolidCube(1.0)
        glPopMatrix()

    # Display the upper leg of humanoid
    def display_upper_leg(self):
        glPushMatrix()
        glTranslatef(0.0, 0.5 * self.lower_arm_length, 0.0)
        glScalef(self.upper_leg_width, self.upper_leg_length, self.upper_leg_width)
        glutSolidCube(1.0)
        glPopMatrix()

    # Display the lower leg of humanoid
    def display_lower_leg(self):
        glPushMatrix()
        glTranslatef(0.0, 0.5 * self.lower_arm_length, 0.0)
        glScalef(self.lower_leg_width, self.lower_leg_length, self.lower_leg_width)
        glutSolidCube(1.0)
        glPopMatrix()

    # Te keyboard controls for the humanoid
    def controls(self, key, x, y):
        # Walk action of humanoid
        if key == 'w':
            if self.left_leg_angle_ud == 210:
                self.dir = 'back'
            if self.left_leg_angle_ud == 150:
                self.dir = 'front'

            if self.dir == 'front':
                self.left_leg_angle_ud += 3
                self.left_knee_angle_ud += 2
                self.right_leg_angle_ud -= 3
                self.right_knee_angle_ud -= 2
                self.right_shoulder_angle_ud += 3
                self.right_ankle_angle_ud += 2
                self.left_shoulder_angle_ud -= 3
                self.left_ankle_angle_ud -= 2
            else:
                self.left_leg_angle_ud -= 3
                self.left_knee_angle_ud -= 2
                self.right_leg_angle_ud += 3
                self.right_knee_angle_ud += 2
                self.right_shoulder_angle_ud -= 3
                self.right_ankle_angle_ud -= 2
                self.left_shoulder_angle_ud += 3
                self.left_ankle_angle_ud += 2

        glutPostRedisplay()


def main():

    # Initialize the OpenGL pipeline
    glutInit(sys.argv)

    # Set OpenGL display mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Set the Window size and position
    glutInitWindowSize(600, 500)
    glutInitWindowPosition(0, 0)

    # Create the window with given title
    glutCreateWindow('Humanoid')

    # Instantiate the humanoid
    h = Humanoid()

    # Attach the callback for the display function
    glutDisplayFunc(h.display)

    # Attach the callback function for keyboard functions
    glutKeyboardFunc(h.controls)

    h.init()

    # Run the OpenGL main loop
    glutMainLoop()

# Call the main function
if __name__ == '__main__':
    main()