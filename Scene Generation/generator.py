import bpy
import os
from math import *
from mathutils import *

#set your own target object here
OBJECT = 'Bridge'
#set your camera here
CAMERA = 'Camera.001'
#set your path here
PATH = 'D:\images'
#how many rotation steps
num_steps = 36

target = bpy.data.objects[OBJECT]
cam = bpy.data.objects[CAMERA]
t_loc_x = target.location.x
t_loc_y = target.location.y
cam_loc_x = cam.location.x
cam_loc_y = cam.location.y

#dist = sqrt((t_loc_x-cam_loc_x)**2+(t_loc_y-cam_loc_y)**2)
dist = (target.location.xy-cam.location.xy).length
#ugly fix to get the initial angle right
init_angle  = (1-2*bool((cam_loc_y-t_loc_y)<0))*acos((cam_loc_x-t_loc_x)/dist)-2*pi*bool((cam_loc_y-t_loc_y)<0)

for x in range(num_steps):
    alpha = init_angle + (x+1)*2*pi/num_steps
    cam.rotation_euler[2] = pi/2+alpha
    cam.location.x = t_loc_x+cos(alpha)*dist
    cam.location.y = t_loc_y+sin(alpha)*dist
    file = os.path.join(PATH, str(x))
    bpy.context.scene.render.filepath = file
    bpy.ops.render.render( write_still=True )