import numpy as np
import math as math

def calculate_buoyancy(V, density_fluid):       #m^3, kg/m^3
    """Write a Python function, calculate_buoyancy, that calculates the buoyancy force exerted on a object submerged in water."""
    g = 9.81        #m/s^2
    return V*density_fluid*g        #in Newtons, aka (kg*m)/s^2

#print(calculate_buoyancy(50, 4))

def will_it_float(V, mass):     #m^3, kg
    """Write a Python function, will_it_float, that determines whether an object will float or sink in water."""
    obj_density = mass/V        #kg/m^3
    if obj_density > 1000:      #obj more dense than water
        return False        #sink
    else:
        return True     #float
    
def calculate_pressure(depth):
    """Write a Python function, calculate_pressure, that calculates the pressure at a given depth in water."""
    g = 9.81
    return depth*1000*g

def calculate_acceleration(F, m):        #Newtons, kg
    """Write a Python function, calculate_acceleration, that calculates the acceleration of an object"""
    return F/m

def calculate_angular_acceleration(tau, I)      #torque in Newton-meters, intertia in kg*m^2
    """Write a Python function, calculate_angular_acceleration, that calculates the angular acceleration of an object given the torque applied to it and its moment of inertia."""
    return tau/I

def calclate_torque(F_magnitude, F_degrees, r):      #Newtons, degrees, meters
    """Write a Python function, calculate_torque, that calculates the torque applied to an object given the force applied to it and the distance from the axis of rotation to the point where the force is applied."""
    return F_magnitude*r*math.sin(math.radians(F_degrees))

def calculate_moment_of_inertia(m, r):       #kilograms, meters
    """Write a Python function, calculate_moment_of_inertia, that calculates the moment of inertia of an object given its mass and the distance from the axis of rotation to the center of mass of the object."""
    return m*r*r


#Problem 8 Part 1
def calculate_auv_acceleration(F_magnitude, F_angle, mass):     #Newtons, radians, kg
    forward_comp_force = F_magnitude * math.cos(F_angle)
    return calculate_acceleration(forward_comp_force, mass)

print(calculate_auv_acceleration(100, 30, 100))
    
