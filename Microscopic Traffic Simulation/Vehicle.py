#This module represents a vehicle and its different properties
from Environment import *
from Driver import *

class Vehicle:
    def __init__(self,id,fixed,typeOfDriver,type,direction):
        self.id=id
        self.type=type
        self.fixed=fixed
        self.driver=Driver(typeOfDriver)
        self.appliedPressure=2
        self.direction=direction
        self.instantaneousAcceleration=self.driver.accelerationCoefficient*self.appliedPressure
        self.instantaneousVelocity=self.driver.accelerationCoefficient*(pow(self.appliedPressure,2))
        self.instantaneousPosition=self.driver.accelerationCoefficient*(pow(self.appliedPressure,3)) 
        if(direction=="north" or direction=="south"):
            self.position=[fixed,self.instantaneousPosition]
        if(direction=="east" or direction=="west"):
            self.position=[self.instantaneousPosition,fixed]
                                                                                                      
    def selfSense(self):
         return {"id":self.id,"type":self.type,"driver":self.driver.type,"appliedPressure":self.appliedPressure,"instantaneousAcceleration":self.instantaneousAcceleration,"instantaneousVelocity":self.instantaneousVelocity,"instantaneousPosition":self.instantaneousPosition}

    def getVisibilityRectangle(self):
        positionMap=getVehiclePositions()

    def print(self):
        print(self.id)
        print(self.type)
        print(self.driver.type)
        print(self.driver.gapLimit)
        print(self.direction)
        print(self.instantaneousAcceleration)
        print(self.instantaneousVelocity)
        print(self.instantaneousPosition)
        print(self.position)

v1=Vehicle(24244,-2,"aggressive","car","north")
a=v1.print()
a=v1.selfSense()
print(a)
