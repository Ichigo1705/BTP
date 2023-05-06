import pybullet as p
import pybullet_data
import math
p.connect(p.GUI)  #or p.SHARED_MEMORY or p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)
carpos = [0, 0, 0]

car = p.loadURDF("husky/husky.urdf", carpos[0], carpos[1], carpos[2])
numJoints = p.getNumJoints(car)
for joint in range(numJoints):
  print(p.getJointInfo(car, joint))
targetVel = 10  #rad/s
maxForce = 100 #Newton
v1 = 0.1
v2 = -0.1
#p.applyExternalForce(car,3,[100,0,0],)

#l1 = [[1, 10], [3, 45], [3, 90], [5]]
#print(l1)
def simulate(X):
    for i in range(len(X)):
        a = X[i]
        print(a)
        if(a[0] == 1):
            j = 0
            while(j<24000):
                targetVel = a[1]*0.01
                for joint in range(2, 6):
                    p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, targetVelocity =targetVel,force = maxForce)
                    
                p.stepSimulation()
                j += 1
        elif(a[0] == 2):
            j = 0
            while(j<24000):
                targetVel = a[1]*0.01
                for joint in range(2, 6):
                    p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, targetVelocity = -targetVel,force = maxForce)
                    
                p.stepSimulation()
                j += 1
        elif(a[0] == 5):
            j = 0
            while(j<24000):
                targetVel = 0
                for joint in range(2, 6):
                    p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, targetVelocity =targetVel,force = maxForce)
                    
                p.stepSimulation()
                j += 1
        elif(a[0] == 3):
            x = a[1]*(math.pi)*2500/(180*0.5)
            Vel1 = 0.4
            Vel2 = -0.1
            j = 0
            while(j <= x):
                p.setJointMotorControl2(car, 2, p.VELOCITY_CONTROL,targetVelocity = Vel1,force = maxForce)
                p.setJointMotorControl2(car, 4, p.VELOCITY_CONTROL,targetVelocity = Vel1,force = maxForce)
                p.setJointMotorControl2(car, 3, p.VELOCITY_CONTROL,targetVelocity = Vel2,force = maxForce)
                p.setJointMotorControl2(car, 5, p.VELOCITY_CONTROL,targetVelocity = Vel2,force = maxForce)
                            
                p.stepSimulation()
                j += 1
            j=0
            while(j<24000):
                targetVel = 0.1
                for joint in range(2, 6):
                    p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, targetVelocity =targetVel,force = maxForce)
                    
                p.stepSimulation()
                j += 1
        elif(a[0] == 4):
            x = a[1]*(math.pi)*2500/(180*0.5)
            Vel1 = 0.4
            Vel2 = -0.1
            j = 0
            while(j <= x):
                p.setJointMotorControl2(car, 2, p.VELOCITY_CONTROL,targetVelocity = Vel2,force = maxForce)
                p.setJointMotorControl2(car, 4, p.VELOCITY_CONTROL,targetVelocity = Vel2,force = maxForce)
                p.setJointMotorControl2(car, 3, p.VELOCITY_CONTROL,targetVelocity = Vel1,force = maxForce)
                p.setJointMotorControl2(car, 5, p.VELOCITY_CONTROL,targetVelocity = Vel1,force = maxForce)
                            
                p.stepSimulation()
                j += 1
            j=0
            while(j<24000):
                targetVel = 0.1
                for joint in range(2, 6):
                    p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL, targetVelocity =targetVel,force = maxForce)
                    
                p.stepSimulation()
                j += 1
        else:
            p.disconnect()
