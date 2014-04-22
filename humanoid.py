# OpenGL imports for python
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Head angle horizontally(left/right)
head_angle_lr = 0

# Head angle vertically(up/down)
head_angle_ud = 0

# Neck angle horizontally
neck_angle_lr = 0

# Neck angle vertically
neck_angle_ud = 0

# Right Shoulder angle horizontally(left/right)
right_shoulder_angle_lr = 0

# Right Shoulder angle vertically(up/down)
right_shoulder_angle_ud = 0

# Left Shoulder angle horizontally(left/right)
left_shoulder_angle_lr = 0

# Left Shoulder angle vertically(up/down)
left_shoulder_angle_ud = 0

# Right Ankle angle vertically
right_ankle_angle_ud = 0

# Left Ankle angle vertically
left_ankle_angle_ud = 0

# Torso angle vertically(up/down)
torso_angle_ud = 0

# Torso angle horizontally(left/right)
torso_angle_lr = 0

# Left leg angle vertically(up/down)
left_leg_ud = 0

# Right leg angle vertically(up/down)
right_leg_ud = 0

# Left knee angle vertically(up/down)
left_knee_ud = 0

# Right knee angle vertically(up/down)
right_knee_ud = 0


def display_humanoid():

    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()


def keyboard_controls():
    pass

glutInit(sys.argv)

glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

glutInitWindowSize(600, 500)
glutInitWindowPosition(0, 0)

glutCreateWindow('Humanoid')

glutDisplayFunc(display_humanoid)
glutIdleFunc(display_humanoid)
glutKeyboardFunc(keyboard_controls)

glutMainLoop()