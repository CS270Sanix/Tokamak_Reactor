
import unittest

class Particle(unittest.TestCase):
    #ffffffffffffffffffff
    def initial(self, color, electrons, protons, neutrons, charge, direction, xpos, ypos, zpos, energies, mass):
        #tracks all necessary attributes of the Particles in our modelled system, for each type of Particle (quantity, appearance, position, velocity, energy, and charge#
        #additionally tracks some amount of the last positions in order to provide a motion trail for the Particle visualization#
        self.color = color #Particle associated color#
        self.electrons = electrons #electron count present in Particle#
        self.protons = protons #proton count present in Particle#
        self.neutrons = neutrons #neutron count present in Particle#
        self.charge = charge #overall charge on the Particle #
        self.direction = direction #direction of travel for the Particle in this reaction #
        self.xpos = xpos #X value for position of Particle #
        self.ypos = ypos #Y value for position of Particle #
        self.zpos = zpos #Z value for position of Particle #
        self.energies = energies #overall energy possessed within the Particle#
        self.mass = mass #Particle mass calculated by protons + neutrons #
        self.tempMass = mass #place holder used to ensure mass change in Decomposition and Fusion#
   
    def Decompose(self, mass):#decomposes the Particles and reduces their overall mass #
        self.tempMass = self.mass #temp mass is a place holder so that the past mass is recorded and can be recorded to see changes#
        self.mass = self.mass/2 
   
    def Fuse(self,Particle1,Particle2, Particle):
        self.tempMass = self.mass #temp mass is a place holder so that the past mass is recorded and can be recorded to see changes#
        self.mass = Particle1.mass+Particle2.mass 
        self.assertTrue(Particle1!=None)
        self.assertTrue(Particle2!=None)
       #Takes elements of a reaction in the event that fusion is taking place, and changes the reactants of the reaction into the products#
   
    def ChangePosition(self, x, y, z):#changes at least one of the x,y,z coordinates of the Particle#
        self.xpos=x
        self.ypos=y
        self.zpos=z

    def test_Particle(self):
        self.Particle = Particle
        self.initial("red", 15, 5, 20, 10, "up", 25, 50, 75, 3, 1)
        self.assertTrue(self.mass>0)
        Particle.Decompose(self,self.mass)
        self.assertTrue(self.mass<self.tempMass) #ensures that decomposition has been carried out and the overall mass has been reduced#
        self.Fuse(self,self, self)
        self.assertTrue(self.mass>self.tempMass) #ensures that fusion has been carried out and the overall mass has been increased #
        newX=25
        newY=25
        newZ=25
        self.assertTrue(self.xpos != newX  or self.ypos != newY or self.zpos != newZ);
        self.ChangePosition(newX,newY,newZ)
        self.assertTrue(self.xpos == newX  or self.ypos == newY or self.zpos == newZ);

class Simulation(unittest.TestCase):
    
    def initial(self,Particles,temperature,density):# tracks the important physical characteristics of the tokamak simulation and the fusion triple constraint (density, time contained (implied variable), composite of Particle energies (temperature))#
        self.Particles = Particles #Particle count in simulation #
        self.donut = Donut_Chamber #of type Donut in order to use functions from that class #
        self.temperature = temperature #measurement of Kelvin in the simulation #
        self.density = density # density of Particles in simulation #
        self.but=Button
        self.gui = GUI
        self.gui.initial(self.gui,1,4,False,70)
    
    def StartReaction(self): #starts the reaction by triggering the start reaction button#
        if(self.gui.isRunning is False):
            self.gui.initial(self.gui,1,4,True,70)
        else:
            print("Simulation has already started.")
        self.assertTrue(self.gui.isRunning==True)
        self.assertTrue(self.gui.speed>=0.5) #secondary test that is run in order to ascertain that the reaction is running at a speed at least equal to the minimum speed#
        self.assertTrue(self.gui.speed<=1.5) #third test that is run in order to ascertain that the reaction is running at a speed less than or equivalent to the maximum speed#
    #implements the proper response from the interaction with GUI (normal time step)#
    
    def StopSimulation(self): #stops the simulation as it is running in order for the user to be able to look at and discern information about what is going on by using the pause simulation or end simulation button#
        if(self.gui.isRunning is True):
            self.gui.initial(self.gui,0,4,False,70,)
        else:
            print("Simulation has already Stopped.")
        self.assertTrue(self.gui.isRunning==False)
        self.assertTrue(self.gui.speed<0.5) #test that is run in order to ascertain that the reaction is running at a speed that is less than the minimum speed#
        #implements the proper response from the interaction with GUI (stop time step)#
    
    def ChangeSpeed(self,speed): # uses the inheritance heirarchy with gui and button to use the change speed method residing in the buttons call of change speed#
        self.gui.tempSpeed = self.gui.speed
        self.gui.speed = speed
        self.assertTrue(self.gui.speed!=self.gui.tempSpeed)
        self.assertTrue(self.gui.speed>=0)
    #implements the proper response from the interaction with GUI (increase or decrease time step)#
   
    def test_simulation(self):
        parts = []
        parts.append(Particle)
        self.initial(parts,75,20)
        self.assertTrue(self.temperature!=None)
        self.StartReaction()
        self.StopSimulation()
        self.ChangeSpeed(1.5)

class Donut_Chamber(unittest.TestCase):

    def _init_(self, magnetic_force, min_magnetic_force, min_required_power):
        self.magnetic_force = magnetic_force #provides the magnetic force levels in the Simulation that will be passed in as a parameter#
        self.min_magnetic_force = min_magnetic_force #this will the value calculated based on a specific function ran in order to determine the minimum required magnetic force value to contain the plasma#
        self.min_required_power = min_required_power #this will hold the minimum required power value required for each Particle to be ionized# 
        self.power=0
        #The Donut chamber is responsible for generating the magnetic force applied by the central solenoid
        
    def changeMagnetism(self,magnetism):#governs the magnetic force based on specific reaction occcurring, the magnetic force must be great enough so that the controlled and formed plasma is not to become uncontained#
        self.magnetism = magnetism
    
    def increasePower(self,amount):#regulates the strength of power introduced into the donut chamber which controlls and is responsible for ionizing the input Particles into a plasma #
        if(self.power==None or self.power<self.min_required_power):
            self.power = self.min_required_power + amount
            self.amount = amount
        else:
            self.power += amount
            self.amount = amount


    def decreasePower(self,amount):#also regulates the power whilst maintaining that the power cannot fall below the required power value in order for the simulation to run and have any reaction occur #
        if(self.power==None or self.power<self.min_required_power):
            self.power = self.min_required_power
            self.amount = amount
        elif((self.power-amount)>= self.min_required_power):
            self.power -= amount
            self.amount = amount
        

    def determineRequiredPower(self,Particle, min_required_power):
        self.min_required_power = min_required_power
    
    def absorbParticles(self,Particle,heat,output):#absorbs the chargeless Particles that are released from the reaction, breeding necessary fuel#
        self.heat = heat
        self.output = output
    
    def test_donut(self):
        self._init_(3,0,0)
        self.assertTrue(self.magnetic_force != None)
        self.changeMagnetism(5)
        self.assertTrue(self.magnetism>0)
        self.assertTrue(self.min_magnetic_force<=self.magnetic_force)
        self.increasePower(3)
        self.assertTrue(self.amount>0)
        self.assertTrue(self.power>=self.min_required_power)
        self.decreasePower(3)
        self.assertTrue(self.amount>0)
        self.assertTrue(self.power>=self.min_required_power)
        self.determineRequiredPower(0,0)
        self.assertTrue(self.min_required_power>=0)
        self.absorbParticles(0,5,True)
        self.assertTrue(self.heat>=0)
        self.assertTrue(self.output==True)        

class Button(unittest.TestCase):
    
    def initial(self, locX,locY):
        self.On = True #On is a boolean variable that tells if the (x,y) for the button is on screen#
        self.gui = GUI #creates a GUI object so that the buttons that appear on the screen can be run using their requiste functions laid out in the GUI class#
        self.locX = locX #X axis location of Button on screen #
        self.locY = locY #Y axis location of Button on screen #
        self.assertTrue(locX!=None)
        self.assertTrue(locY!=None)

    def OnClick(self,simulation):#once the button is pressed, this passes in the simulation variable with attributes of the simulation class #
        self.sim = simulation
        self.assertTrue(simulation!=None)
    
    def getOn(self):
        if(self.On==False):#will restore the locX of the button to the center of the screen if the button was not previously on screen #
            locX=50 
            locY=50
            self.On=True
        self.assertTrue(self.On)

    #return the On Boolean value to make sure that the button is on the screen, if it is not then the button will be restored to a set position#
    def test_button(self):
        self.initial(25,25)
        temp = Simulation
        self.OnClick(temp)
        self.getOn()

class GUI(unittest.TestCase):
    def initial(self,speed,zoom,isRunning,temperature):
        self.buttons = Button #of type Button in order to use functions from that class #
        self.simulation = Simulation #of type Simulation in order to use functions from that class #
        self.speed = speed #shows speed of Particles in the simulation reaction #
        self.zoom = zoom #adjustable zoom percentage#
        self.isRunning = isRunning # boolean to describe state of simulation #
        self.temperature = temperature # record of simulation temperature at any given time#
        self.tempZoom = zoom #place holder used to ensure change in Zoom level#
        self.tempSpeed = speed #place holder used to ensure change in speed#

    def displayTemperature(self,temperature):
        print(temperature)
        self.assertTrue(isRunning==True) # in order for a temperature value to be produced, the simulation must be running, as if it is not the temperature will be that of 0#
        self.assertTrue(temperature>0)  # proves that the system is running and that the temperature measuring diode is functioning properly#

    def ChangeSpeed(self,speed):
        self.speed = speed
        self.assertTrue(speed>=0.5) # asserts that the speed of the on screen reaction is occurring at a rate which is fast enough that it will not be a value that is too low that the user will not be able to see exactly what is happening in the system#
        self.assertTrue(speed<=1.5) # asserts that the speed of the reaction is running at a rate which allows the user to see the simulation occur compared to it just being over as soon as it is started#
        #the speed variable ranges from 0.5-1.5 which will effect the percentage value of speed of reaction in the simulation from 0.5=50% and 1.5=150%#
        self.tempSpeed = self.speed
        self.assertTrue(self.speed!=tempSpeed)
    #changes speed from a range of 0.5 to 1.5 billion times the real speed#

    def PauseReaction(self):
        self.tempSpeed = self.speed #will hold the speed at which the simulation was previously being displayed in order to have it when the simulation is restarted#
        self.speed = 0
        self.isRunning = False
        self.assertTrue(isRunning==False) #shows that the simulation is running as it is required to be running in order to be paused#
        self.assertTrue(self.speed==0)
    #if the reaction is running this method will pause it at its current stage#

    def StartReaction(self):
        self.speed = self.tempSpeed
        self.isRunning = True
        self.assertTrue(isRunning==True) #tells that the reaction was not running when the user tries to start the simulation #
        self.assertTrue(self.speed==tempSpeed) # if coming off a pause this ensures that the previous speed value is restored#
        self.assertTrue(speed>0) #if speed is equal to 0 then the reaction has never been run, and can be started, but if it was less than 0 then the speed value must be reset to 0 in order to have it start#
    #if the reaction is not already running this method will start it from the last marked stage#

    def EndReaction(self):
        pass
        self.assertTrue(isRunning)#shows that the simulation is running as it is required to be running in order to be ended#
        self.assertTrue(speed>=0.5) #secondary test that is run in order to ascertain that the reaction is running at a speed at least equal to the minimum speed#
        self.assertTrue(speed<=1.5) #third test that is run in order to ascertain that the reaction is running at a speed less than or equivalent to the maximum speed#
    #if the reaction is running then the reaction will be terminated entirely and will reset the initial variables to that of 0#

    def ChangeZoom(self,zoom):
        pass
        tempZoom = self.zoom # previously used zoom level is recorded in order to later be used to check if the zoom has actually been changed#
        self.zoom = zoom # updates the zoom level to represent the users new requested zoom value#
        self.assertTrue(self.zoom!=tempZoom) # new zoom level cannot be equivalent to the previous value as if it is then nothing can be changed#
        self.assertTrue(zoom>=0) # base level zoom can be 0 which is representative of a base 100% zoom#
        self.assertTrue(zoom<=150) #high level zoom can be 150 which is representative of a base 250% zoom#
    #changes the scale at which the simulation is rendered ranging from a base zoom of 0 to 150 times the base zoom #

    def test_GUI(self):
        self.initial(1,2,True,50)
        self.assertTrue(self.isRunning) 

class Zoom_In_Button(Button):
      
    def _init_(self):
        pass
        self.assertTrue(locX>=0)
        self.assertTrue(locX<=100)
        self.assertTrue(locY>=0)
        self.assertTrue(locY<=100)
        self.assertTrue(Button.getOn==true)# tells that the zoom in button is on screen and able to be used #
        if(On==False):#will restore the locX and locY of the button to the set location on the screen if the button was not previously on screen #
            locX=0 
            locY=0
    #inherits from button parent class and can have an (x,y) location that is any percentage of total screen combination from 0-100%#

class Zoom_Out_Button(Button):
    
    def _init_(self):
        pass
        self.assertTrue(locX>=0)
        self.assertTrue(locX<=100)
        self.assertTrue(locY>=0)
        self.assertTrue(locY<=100)
        self.assertTrue(Button.getOn==true)# tells that the zoom in button is on screen and able to be used #
        if(On==False):#will restore the locX and locY of the button to the set location on the screen if the button was not previously on screen #
            locX=0 
            locY=10
    #inherits from button parent class and can have an (x,y) location that is any percentage of total screen combination from 0-100%#

class SpeedUP_Button(Button):
    
    def _init_(self):
        pass
        self.assertTrue(Button.getOn==true)# tells that the speed change in button is on screen and able to be used #
        if(On==False):#will restore the locX and locY of the button to the set location on the screen if the button was not previously on screen #
            locX=100 
            locY=0
    #inherits from button parent class and can have an (x,y) location that is any percentage of total screen combination from 0-100%#

class SlowDown_Button(Button):
    
    def _init_(self):
        pass
        self.assertTrue(Button.getOn==true)# tells that the speed change in button is on screen and able to be used #
        if(On==False):#will restore the locX and locY of the button to the set location on the screen if the button was not previously on screen #
            locX=100 
            locY=10
    #inherits from button parent class and can have an (x,y) location that is any percentage of total screen combination from 0-100%#

class End_Button(Button):
    
    def _init_(self):
      pass
      self.assertTrue(Button.getOn==true)# tells that the end simulation button is on screen and able to be used #
      if(On==False):#will restore the locX and locY of the button to the set location on the screen if the button was not previously on screen #
            locX=100 
            locY=100
    #inherits from button parent class and can have an (x,y) location that is any percentage of total screen combination from 0-100%#

class Start_Button(Button):
    
    def _init_(self):
        pass
        self.assertTrue(Button.getOn==true)# tells that the speed change in button is on screen and able to be used #
        if(On==False):#will restore the locX and locY of the button to the set location on the screen if the button was not previously on screen #
            locX=50 
            locY=100
    #inherits from button parent class and can have an (x,y) location that is any percentage of total screen combination from 0-100%#

class Play_Button(Button):
    
    def _init_(self):
        pass
        self.assertTrue(Button.getOn==true)# tells that the speed change in button is on screen and able to be used #
        if(On==False):#will restore the locX and locY of the button to the set location on the screen if the button was not previously on screen #
            locX=100 
            locY=80
    #inherits from button parent class and can have an (x,y) location that is any percentage of total screen combination from 0-100%#

class Pause_Button(Button):
    
    def _init_(self):
        pass
        self.assertTrue(Button.getOn==true)# tells that the speed change in button is on screen and able to be used #
        if(On==False):#will restore the locX and locY of the button to the set location on the screen if the button was not previously on screen #
            locX=100 
            locY=90
        #Stops progress of the time step#
        #inherits from button parent class and can have an (x,y) location that is any percentage of total screen combination from 0-100%#

class Physics:
    
    def _init_(self, Weak_Nuclear_Force, Strong_Nuclear_Force, min_weak_force, min_strong_force, effect):
        self.Weak_Nuclear_Force = Weak_Nuclear_Force #sets the value of the force present in the simulation in order to make Particles repel each other#
        self.Strong_Nuclear_Force = Strong_Nuclear_Force #sets the value of the force present in the simulation in order to rip the Particles apart#
        self.assertTrue(Strong_Nuclear_Force>=min_strong_force)#checks to make sure there is enough strong nuclear force present for the Particles to be seperated#
        self.assertTrue(Weak_Nuclear_Force>=min_weak_force) #checks to make sure there is enough weak nuclear force present for the Particles to be repelled and not recombine#
        self.assertTrue(effect>0)#determines that the end result of energy produced is greater than zero so that we can see that the simulation was completed properly#
    #The physics class will, for every Particle, take the forces at the position of the Particle and affect its movement according to its mass, charge, and current velocity#

class Force(Physics):
    def effect(self):
        pass
        self.assertTrue(effect!=0)#makes sure that the reaction was run and completed properly producing an energy variable per each reaction simulation# 

class Weak_Nuclear_Force(Force,Particle):
    def _init_(self):
        self.Particle = Particle #uses Particle object to run fuctions of Particle class in order to calculate forces#
    def effect(self):
        pass
        self.assertTrue(Weak_Nuclear_Force!=0) #shows that the weak nuclear force used is not zero as it will produce an non functioning simulation#
        self.assertTrue(min_weak_force!=0) # if the min required force is zero then we can see that the overall reading and calculation of the weak force is malfunctioning#
    #Calculates the 'weak nuclear force' for each Particle on all other Particles#

class Strong_Nuclear_Force(Force,Particle):
    def _init_(self):
        self.Particle = Particle#uses Particle object to run fuctions of Particle class in order to calculate forces#
    def effect(self):
        pass
        self.assertTrue(Strong_Nuclear_Force!=0) #shows that the weak nuclear force used is not zero as it will produce an non functioning simulation as the molecules will still be combined#
        self.assertTrue(min_strong_force!=0) # if the min required force is zero then we can see that the overall reading and calculation of the strong force is malfunctioning#
    #Calculates the 'strong nuclear force' for each Particle on all other Particles#
    
    def Decompose(self,Particle1,Particle2,Particle):
        def _init_(self):
            self.Particle = Particle #uses Particle object to run fuctions of Particle class in order to calculate forces#
        pass
        self.assertTrue(Particle1!=None)
        self.assertTrue(Particle2!=None)
        self.assertTrue(Particle.mass>0)#ensures that the Particle has a mass therfore is in the reaction #

class Magnetic_Force(Force):
    
    def effect(self):
        pass
        self.assertTrue(Force!=0)
    #Calculates the 'electromagnetic force' for each Particle on all other Particles#

class Gravity(Force):
    
    def effect(self):
        pass
        self.assertTrue(Force!=0)
    #Calculates the 'gravitational force' for each Particle on all other Particles#

class Velocity:
    
    def _init_(self,xVelo,yVelo,zVelo):
        self.xVelo = xVelo #Velocity measurement in X direction#
        self.yVelo = yVelo #Velocity measurement in Y direction#
        self.zVelo = zVelo #Velocity measurement in Z direction#
        
        self.assertTrue(xVelo!=None)#tells that the Particle in the reaction is indeed moving and this provides accurate measurements of just how so in the X axis direction#
        self.assertTrue(yVelo!=None)#tells that the Particle in the reaction is indeed moving and this provides accurate measurements of just how so in the Y axis direction#
        self.assertTrue(zVelo!=None)#tells that the Particle in the reaction is indeed moving and this provides accurate measurements of just how so in the Z axis direction#
    #Holds speed for all axes #
    def Reverse(self,newXVelo,newYVelo,newZVelo):
        pass
        self.newXVelo = newXVelo
        self.newYVelo = newYVelo
        self.newZVelo = newZVelo
        self.assertTrue(xVelo) #shows that there is an X axis velocity measurement that can be reversed#
        self.assertTrue(newXVelo==(Xvelo*-1))#Shows that the velocity was actually reversed#
        self.assertTrue(yVelo) #shows that there is an Y axis velocity measurement that can be reversed#
        self.assertTrue(newYVelo==(Yvelo*-1))#Shows that the velocity was actually reversed#
        self.assertTrue(zVelo) #shows that there is an Z axis velocity measurement that can be reversed#
        self.assertTrue(newZVelo==(Zvelo*-1))#Shows that the velocity was actually reversed#
    #Will reverse the overall velocity by making the appropriate signage conversions to the x,y,z speeds#
    def slowDown(self, amount,newXVelo,newYVelo,newZVelo):
        pass
        self.newXVelo = newXVelo
        self.newYVelo = newYVelo
        self.newZVelo = newZVelo
        self.assertTrue(xVelo)#shows that there is an X axis velocity measurement that can be slowed#
        self.assertTrue(xVelo<newXVelo)#ensures that the velocity was indeed decreased#
        self.assertTrue(yVelo)#shows that there is an Y axis velocity measurement that can be slowed#
        self.assertTrue(yVelo<newYVelo)#ensures that the velocity was indeed decreased#
        self.assertTrue(zVelo)#shows that there is an Z axis velocity measurement that can be slowed#
        self.assertTrue(zVelo<newZVelo)#ensures that the velocity was indeed decreased#
    #Will reduce the velocity of at least one of the three velocities #
    def speedUp(self, amount,newXVelo,newYVelo,newZVelo):
        pass
        self.newXVelo = newXVelo
        self.newYVelo = newYVelo
        self.newZVelo = newZVelo
        self.assertTrue(xVelo)#shows that there is an X axis velocity measurement that can be sped up#
        self.assertTrue(xVelo<newXVelo)#shows that the velocity was increased#
        self.assertTrue(yVelo)#shows that there is an Y axis velocity measurement that can be sped up#
        self.assertTrue(yVelo<newYVelo)#shows that the velocity was increased#
        self.assertTrue(zVelo)#shows that there is an Z axis velocity measurement that can be sped up#
        self.assertTrue(zVelo<newZVelo)#shows that the velocity was increased#
    #Will increase the velocity of at least one of the three velocites #
if __name__ == '__main__':
    unittest.main()

    #Testing testing testing#
