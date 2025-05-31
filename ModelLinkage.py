"""
Model our creature and wrap it in one class.
First version on 09/28/2021

:author: micou(Zezhou Sun)
:version: 2021.2.1

----------------------------------

Modified by Daniel Scrivener 09/2023
"""

from Component import Component
from Point import Point
import ColorType as Ct
from Shapes import Cube
from Shapes import Cylinder
from Shapes import Sphere
from Shapes import Cone
import numpy as np
import ColorType





class ModelLinkage(Component):
    """
    Define our linkage model
    """

    ##### TODO 2: Model the Creature
    # Build the class(es) of objects that could utilize your built geometric object/combination classes. E.g., you could define
    # three instances of the cyclinder trunk class and link them together to be the "limb" class of your creature. 
    #
    # In order to simplify the process of constructing your model, the rotational origin of each Shape has been offset by -1/2 * dz,
    # where dz is the total length of the shape along its z-axis. In other words, the rotational origin lies along the smallest 
    # local z-value rather than being at the translational origin, or the object's true center. 
    # 
    # This allows Shapes to rotate "at the joint" when chained together, much like segments of a limb. 
    #
    # In general, you should construct each component such that it is longest in its local z-direction: 
    # otherwise, rotations may not behave as expected.
    #
    # Please see Blackboard for an illustration of how this behavior works.

    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)
        self.contextParent = parent

        # Define colors
        Yellow = ColorType.ColorType(255, 255, 0)
        Purple = ColorType.ColorType(196 / 255, 0, 255 / 255)
        Green = ColorType.ColorType(64 / 255, 241 / 255, 0)

        # Create body and head
        body = Sphere(Point((0, 0, 0)), shaderProg, [1, 1, 1], Yellow)
        head = Sphere(Point((0, 0.3, -0.1)), shaderProg, [1, 1.3, 0.9], Yellow)

        # Create ears
        left_ear = Sphere(Point((-0.65, 1, 0)), shaderProg, [0.2, 0.2, 0.2], Yellow)
        right_ear = Sphere(Point((0.65, 1, 0)), shaderProg, [0.2, 0.2, 0.2], Yellow)

        # Create eyes and inner eyes
        left_eye = Sphere(Point((-0.4, 0.49, 0.55)), shaderProg, [0.25, 0.15, 0.15], Purple)
        right_eye = Sphere(Point((0.4, 0.49, 0.55)), shaderProg, [0.25, 0.15, 0.15], Purple)
        left_eye.setDefaultAngle(160, body.w())

        right_eye.setDefaultAngle(-160, body.w())

        inner_left_eye = Sphere(Point((0.03, 0, 0.05)), shaderProg, [0.2, 0.10, 0.10], Green)
        inner_right_eye = Sphere(Point((-0.03, 0, 0.05)), shaderProg, [0.2, 0.10, 0.10], Green)
        inner_left_eye.setDefaultAngle(185, body.w())
        inner_right_eye.setDefaultAngle(185, body.w())

        # Create left arm (shoulder, elbow, fingers)
        left_shoulder = Sphere(Point((0.85, 0, 0)), shaderProg, [0.2, 0.2, 0.2], Yellow)
        left_arm1 = Cylinder(Point((0.15, 0, 0.3)), shaderProg, [0.2, 0.2, 0.3], Yellow)
        # left_arm1.rotate(90, body.v())
        left_arm1.setDefaultAngle(90, body.v())
        left_elbow = Sphere(Point((0.01, 0, 0.45)), shaderProg, [0.2, 0.2, 0.2], Purple)
        left_arm2 = Cylinder(Point((0, 0, 0.35)), shaderProg, [0.2, 0.2, 0.2], Purple)
        left_finger1 = Cone(Point((0.15, 0, 0.25)), shaderProg, [0.05, 0.05, 0.05], Yellow)
        left_finger2 = Cone(Point((-0.15, 0, 0.25)), shaderProg, [0.05, 0.05, 0.05], Yellow)

        # Create right arm (shoulder, elbow, fingers)
        right_shoulder = Sphere(Point((-0.85, 0, 0)), shaderProg, [0.2, 0.2, 0.2], Yellow)
        right_arm1 = Cylinder(Point((-0.15, 0, 0.3)), shaderProg, [0.2, 0.2, 0.3], Yellow)
        right_arm1.setDefaultAngle(-90, body.v()) 
        right_elbow = Sphere(Point((0.01, 0, 0.45)), shaderProg, [0.2, 0.2, 0.2], Purple) 
        right_arm2 = Cylinder(Point((0, 0, 0.35)), shaderProg, [0.2, 0.2, 0.2], Purple)
        right_finger1 = Cone(Point((0.15, 0, 0.25)), shaderProg, [0.05, 0.05, 0.05], Yellow)
        right_finger2 = Cone(Point((-0.15, 0, 0.25)), shaderProg, [0.05, 0.05, 0.05], Yellow)

        # Create left leg (hip, knee, foot)
        left_hip = Sphere(Point((0.7, -0.6, 0)), shaderProg, [0.25, 0.25, 0.25], Purple)  
        left_thigh = Cylinder(Point((0, -0.35, 0)), shaderProg, [0.15, 0.4, 0.15], Purple)  
        left_knee = Sphere(Point((0, -0.4, 0)), shaderProg, [0.15, 0.15, 0.15], Purple) 
        left_leg = Cylinder(Point((0, -0.4, 0)), shaderProg, [0.15, 0.4, 0.15], Purple)  
        left_foot = Sphere(Point((0, -0.2, 0.2)), shaderProg, [0.2, 0.2, 0.2], Yellow) 

        # Create right leg (hip, knee, foot)
        right_hip = Sphere(Point((-0.7, -0.6, 0)), shaderProg, [0.25, 0.25, 0.25], Purple)  
        right_thigh = Cylinder(Point((0, -0.35, 0)), shaderProg, [0.15, 0.4, 0.15], Purple)  
        right_knee = Sphere(Point((0, -0.4, 0)), shaderProg, [0.15, 0.15, 0.15], Purple) 
        right_leg = Cylinder(Point((0, -0.4, 0)), shaderProg, [0.15, 0.4, 0.15], Purple)  
        right_foot = Sphere(Point((0, -0.2, 0.2)), shaderProg, [0.2, 0.2, 0.2], Yellow)  

        # Build the hierarchy for the left leg
        left_hip.addChild(left_thigh)
        left_thigh.addChild(left_knee)
        left_knee.addChild(left_leg)
        left_leg.addChild(left_foot)

        # Build the hierarchy for the right leg
        right_hip.addChild(right_thigh)
        right_thigh.addChild(right_knee)
        right_knee.addChild(right_leg)
        right_leg.addChild(right_foot)

        # Attach arms to shoulders, fingers to arms
        left_shoulder.addChild(left_arm1)
        left_arm1.addChild(left_elbow)
        left_elbow.addChild(left_arm2)
        left_arm2.addChild(left_finger1)
        left_arm2.addChild(left_finger2)

        right_shoulder.addChild(right_arm1)
        right_arm1.addChild(right_elbow)
        right_elbow.addChild(right_arm2)
        right_arm2.addChild(right_finger1)
        right_arm2.addChild(right_finger2)

        # Attach shoulders, eyes, ears, and head to body
        body.addChild(head)
        body.addChild(left_hip) 
        body.addChild(right_hip)  
        head.addChild(left_ear)
        head.addChild(right_ear)
        head.addChild(left_eye)
        head.addChild(right_eye)
        left_eye.addChild(inner_left_eye)
        right_eye.addChild(inner_right_eye)
        head.addChild(left_shoulder)
        head.addChild(right_shoulder)

        # Add body to the model
        self.addChild(body)

        # Create component lists and dictionaries for easy access
        self.componentList = [
            body, head, left_ear, right_ear, left_eye, right_eye,
            left_shoulder, right_shoulder, left_hip, right_hip,
            left_knee, right_knee, left_thigh, right_thigh,
            left_leg, right_leg, left_foot, right_foot,
            left_elbow, right_elbow, left_arm1, left_arm2,
            right_arm1, right_arm2, left_finger1, left_finger2,
            right_finger1, right_finger2
        ]

        self.componentDict = {
            "body": body, "head": head, "right_ear": right_ear, "left_ear": left_ear,
            "right_eye": right_eye, "left_eye": left_eye, "left_shoulder": left_shoulder,
            "right_shoulder": right_shoulder, "left_hip": left_hip, "right_hip": right_hip,
            "left_knee": left_knee, "right_knee": right_knee, "left_thigh": left_thigh,
            "right_thigh": right_thigh, "left_leg": left_leg, "right_leg": right_leg,
            "left_foot": left_foot, "right_foot": right_foot, "left_elbow": left_elbow,
            "right_elbow": right_elbow, "left_arm1": left_arm1, "left_arm2": left_arm2,
            "right_arm1": right_arm1, "right_arm2": right_arm2, "left_finger1": left_finger1,
            "left_finger2": left_finger2, "right_finger1": right_finger1, "right_finger2": right_finger2
        }
                        
                
        ##### TODO 4: Define creature's joint behavior
        # Requirements:
        #   1. Set a reasonable rotation range for each joint,
        #      so that creature won't intersect itself or bend in unnatural ways
        #   2. Orientation of joint rotations for the left and right parts should mirror each other.
        

        # Head
        head = self.componentDict["head"]
        head.setRotateExtent(head.uAxis, -5, 5)
        head.setRotateExtent(head.vAxis, -20, 20)
        head.setRotateExtent(head.wAxis, -20, 20)

        # Ears 
        left_ear = self.componentDict["left_ear"]
        right_ear = self.componentDict["right_ear"]
        left_ear.setRotateExtent(left_ear.uAxis, -10, 10)
        left_ear.setRotateExtent(left_ear.vAxis, -10, 10)
        left_ear.setRotateExtent(left_ear.wAxis, -10, 10)
        right_ear.setRotateExtent(right_ear.uAxis, -10, 10)
        right_ear.setRotateExtent(right_ear.vAxis, -10, 10)
        right_ear.setRotateExtent(right_ear.wAxis, -10, 10)

        # Eye
        left_eye = self.componentDict["left_eye"]
        right_eye = self.componentDict["right_eye"]
        left_eye.setRotateExtent(left_eye.uAxis, -10, 10)
        left_eye.setRotateExtent(left_eye.vAxis, -10, 10)
        left_eye.setRotateExtent(left_eye.wAxis, -10, 10)
        right_eye.setRotateExtent(right_eye.uAxis, -10, 10)
        right_eye.setRotateExtent(right_eye.vAxis, -10, 10)
        right_eye.setRotateExtent(right_eye.wAxis, -10, 10)


        # Shoulder joint behavior (for both arms)
        left_shoulder = self.componentDict["left_shoulder"]
        right_shoulder = self.componentDict["right_shoulder"]
        left_shoulder.setRotateExtent(left_shoulder.uAxis, -60, 60)  
        left_shoulder.setRotateExtent(left_shoulder.vAxis, -60, 60)  
        left_shoulder.setRotateExtent(left_shoulder.wAxis, -60, 60)  
        right_shoulder.setRotateExtent(right_shoulder.uAxis, -60, 60)
        right_shoulder.setRotateExtent(right_shoulder.vAxis, -60, 60)
        right_shoulder.setRotateExtent(right_shoulder.wAxis, -60, 60)



        # Elbow joint behavior (for both arms)
        left_elbow = self.componentDict["left_elbow"]
        right_elbow = self.componentDict["right_elbow"]
        left_elbow.setRotateExtent(left_elbow.uAxis, -30, 30)
        left_elbow.setRotateExtent(left_elbow.vAxis, -30, 30) 
        left_elbow.setRotateExtent(left_elbow.wAxis, -30, 30) 
        right_elbow.setRotateExtent(right_elbow.uAxis, -30, 30)
        right_elbow.setRotateExtent(right_elbow.vAxis, -30, 30)
        right_elbow.setRotateExtent(right_elbow.wAxis, -30, 30)

        # left_shoulder.addChild(left_arm1)
        # left_arm1.addChild(left_elbow)
        # left_elbow.addChild(left_arm2)
        # left_arm2.addChild(left_finger1)
        # left_arm2.addChild(left_finger2)

        left_arm1 = self.componentDict["left_arm1"] 
        left_arm1.setRotateExtent(left_arm1.uAxis, -90, 90)
        left_arm1.setRotateExtent(left_arm1.vAxis,  0, 180)
        left_arm1.setRotateExtent(left_arm1.wAxis, -90, 90)
        right_arm1 = self.componentDict["right_arm1"] 
        right_arm1.setRotateExtent(right_arm1.uAxis, -90, 90)
        right_arm1.setRotateExtent(right_arm1.vAxis, 0, 180)
        right_arm1.setRotateExtent(right_arm1.wAxis, -90, 90)

        left_arm2 = self.componentDict["left_arm2"] 
        left_arm2.setRotateExtent(left_arm2.uAxis, -90, 90)
        left_arm2.setRotateExtent(left_arm2.vAxis,  -90, 90)
        left_arm2.setRotateExtent(left_arm2.wAxis, -90, 90)
        right_arm2 = self.componentDict["right_arm2"] 
        right_arm2.setRotateExtent(right_arm2.uAxis, -90, 90)
        right_arm2.setRotateExtent(right_arm2.vAxis, -90, 90)
        right_arm2.setRotateExtent(right_arm2.wAxis, -90, 90)




        # Hip joint behavior (for both legs)
        left_hip = self.componentDict["left_hip"]
        right_hip = self.componentDict["right_hip"]
        left_hip.setRotateExtent(left_hip.uAxis, -30, 30) 
        left_hip.setRotateExtent(left_hip.vAxis, -30, 30) 
        left_hip.setRotateExtent(left_hip.wAxis, -30, 30) 
        right_hip.setRotateExtent(right_hip.uAxis, -30, 30) 
        right_hip.setRotateExtent(right_hip.vAxis, -30, 30) 
        right_hip.setRotateExtent(right_hip.wAxis, -30, 30) 

        # Thigh
        left_thigh = self.componentDict["left_thigh"]        
        right_thigh = self.componentDict["right_thigh"]
        left_thigh.setRotateExtent(left_thigh.uAxis, 0, 0) 
        left_thigh.setRotateExtent(left_thigh.vAxis, 0, 0) 
        left_thigh.setRotateExtent(left_thigh.wAxis, 0, 0)  
        right_thigh.setRotateExtent(right_thigh.uAxis, 0, 0) 
        right_thigh.setRotateExtent(right_thigh.vAxis, 0, 0) 
        right_thigh.setRotateExtent(right_thigh.wAxis, 0, 0) 

        # Knee joint behavior (for both legs)
        left_knee = self.componentDict["left_knee"]
        right_knee = self.componentDict["right_knee"]
        left_knee.setRotateExtent(left_knee.uAxis, -30, 30)  
        left_knee.setRotateExtent(left_knee.vAxis, -30, 30)    
        left_knee.setRotateExtent(left_knee.wAxis, -30, 30)     
        right_knee.setRotateExtent(right_knee.uAxis, -30, 30)    
        right_knee.setRotateExtent(right_knee.vAxis, -30, 30)  
        right_knee.setRotateExtent(right_knee.wAxis, -30, 30)  

        left_leg = self.componentDict["left_leg"]
        right_leg = self.componentDict["right_leg"]
        left_leg.setRotateExtent(left_leg.uAxis, 0, 0)  
        left_leg.setRotateExtent(left_leg.vAxis, 0, 0)  
        left_leg.setRotateExtent(left_leg.wAxis, 0, 0)  
        right_leg.setRotateExtent(right_leg.uAxis, 0, 0)  
        right_leg.setRotateExtent(right_leg.vAxis, 0, 0)  
        right_leg.setRotateExtent(right_leg.wAxis, 0, 0)  

        # Foot joint behavior (for both legs)
        left_foot = self.componentDict["left_foot"]
        right_foot = self.componentDict["right_foot"]
        left_foot.setRotateExtent(left_foot.uAxis, 0, 0)  
        left_foot.setRotateExtent(left_foot.vAxis, 0, 0)  
        left_foot.setRotateExtent(left_foot.wAxis, 0, 0)  
        right_foot.setRotateExtent(right_foot.uAxis, 0, 0)  
        right_foot.setRotateExtent(right_foot.vAxis, 0, 0)  
        right_foot.setRotateExtent(right_foot.wAxis, 0, 0)  

        # Finger joint behavior 
        left_finger1 = self.componentDict["left_finger1"]
        left_finger2 = self.componentDict["left_finger2"]
        right_finger1 = self.componentDict["right_finger1"]
        right_finger2 = self.componentDict["right_finger2"]

        left_finger1.setRotateExtent(left_finger1.uAxis, 0, 0)  
        left_finger1.setRotateExtent(left_finger1.vAxis, 0, 0) 
        left_finger1.setRotateExtent(left_finger1.wAxis, 0, 0)  
 
        left_finger2.setRotateExtent(left_finger2.uAxis, 0, 0)  
        left_finger2.setRotateExtent(left_finger2.vAxis, 0, 0)  
        left_finger2.setRotateExtent(left_finger2.wAxis, 0, 0)  


        right_finger1.setRotateExtent(right_finger1.uAxis, 0, 0)
        right_finger1.setRotateExtent(right_finger1.vAxis, 0, 0)  
        right_finger1.setRotateExtent(right_finger1.wAxis, 0, 0)  
  
        right_finger2.setRotateExtent(right_finger2.uAxis, 0, 0)  
        right_finger2.setRotateExtent(right_finger2.vAxis, 0, 0)  
        right_finger2.setRotateExtent(right_finger2.wAxis, 0, 0)  



        

        