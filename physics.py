import numpy as np
import math as math

G = 9.81        #m/s^2
water_density = 1000
PRESSUREAT0 = 101325

def calculate_buoyancy(V, density_fluid):       #m^3, kg/m^3
    """Calculates the buoyancy force exerted on a object submerged in water."""
    return V*density_fluid*G        #in Newtons, aka (kg*m)/s^2

#print(calculate_buoyancy(50, 4))

def will_it_float(V, mass):     #m^3, kg
    """Determines whether an object will float or sink in water."""
    obj_density = mass/V        #kg/m^3
    if obj_density > water_density:      #obj more dense than water
        return False        #sink
    else:
        return True     #float
    
def calculate_pressure(depth):      #m
    """Calculates the pressure at a given depth in water."""
    #Check depth is positive
    #At 0, the pressure should be 1 atm
    return (depth*water_density*G) + PRESSUREAT0

def calculate_acceleration(F, m):        #Newtons, kg
    """Calculates the acceleration of an object"""
    return F/m

def calculate_angular_acceleration(tau, I):      #torque in Newton-meters, intertia in kg*m^2
    """Calculates the angular acceleration of an object given the torque applied to it and its moment of inertia."""
    return tau/I

def calculate_torque(F_magnitude, F_degrees, r):      #Newtons, degrees, meters
    """Calculates the torque applied to an object given the force applied to it and the distance from the axis of rotation to the point where the force is applied."""
    return F_magnitude*r*np.sin(math.radians(F_degrees))

def calculate_moment_of_inertia(m, r):       #kilograms, meters
    """Calculates the moment of inertia of an object given its mass and the distance from the axis of rotation to the center of mass of the object."""
    return m*(r**2)


#Problem 8 Part 1
def calculate_auv_acceleration(F_magnitude, F_angle, mass = 100):     #Newtons, radians, kg       Keep in mind the angle should not be greater/less than 30/-30 degrees (so pi/6 or -pi/6 rad)
    """Calculate AUV acceleration in m/s^2."""
    #If not wanting separate components: simply return F_magnitude/mass
    accelo_comp_force = np.array(
        [F_magnitude * np.cos(F_angle), F_magnitude * np.sin(F_angle)]
        )
    print("The AUV is accelerating at a rate of " + str(np.linalg.norm(accelo_comp_force/mass)) + " m/s^2 at " + str(F_angle) + " radians.")
    return accelo_comp_force/mass

print(calculate_auv_acceleration(100, 30))

#Problem 8 Part 2
def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia = 1, thruster_distance = 0.5):        #Newtons, radians, kg*m^2, m
    """Calculate angular acceleration in rad/s^2."""
    #Find torque
    auv_torque = calculate_torque(F_magnitude, math.degrees(F_angle), thruster_distance)
    #Find inertia
    return calculate_angular_acceleration(auv_torque, inertia)
    
#Problem 9 Part 1
#T = np.array(
    [60, 70, 90, 40]        #[F_T1, F_T2, F_T3, F_T4] - forces of thrusters, current num are placeholders that should be numbers
#)

def calculate_auv2_acceleration(T, alpha, theta, mass):     #array, radians, radians, kg (100 default)
    """Calculate acceleration of the AUV with respect to the original axes, not relative to AUV. Don't forget to split forces into components."""
    auv_x_comp = (T[0]*np.cos(alpha)) + (T[1]*np.cos(alpha)) + (T[2]*np.cos(np.pi + alpha)) + (T[3]*np.cos(np.pi - alpha))      #T1, T2, T3, T4 - in that order. Calculate combination of component force in x direction. Relative to AUV.
    auv_y_comp = (T[0]*np.sin(alpha)) + (T[1]*np.sin(-alpha)) + (T[2]*np.sin(np.pi + alpha)) + (T[3]*np.sin(np.pi - alpha))       #T1, T2, T3, T4 - in that order. Calculate combination of component force in y direction. Relative to AUV.
    auv_comp_forces = np.array(
        [auv_x_comp, auv_y_comp]
    )
    rotation_matrix = np.array(
       [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
   ) #Account for theta

    return np.dot(rotation_matrix, auv_comp_forces)

calculate_auv2_acceleration([10, 1, 4, 0], 0.12, 0.5, 100)

"""
Then use rotation matrix to turn into global frame
"""





#Problem 9 Part 2
def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia):        #array, radians, meters (x-direction), meters (y-direction), kg*m^2 (default 100)
    """Calculate angular acceleration. Keep in mind that L is distance x-wise and l is distance y-wise from center of AUV to a thruster."""
    dist_from_center = np.sqrt(L**2 + l**2)

    torque_1 = calculate_torque(T[0], math.degrees(alpha), dist_from_center)      #Neg torque
    torque_2 = calculate_torque(T[1], math.degrees(alpha), dist_from_center)      #Pos torque
    torque_3 = calculate_torque(T[2], math.degrees(alpha), dist_from_center)      #Neg torque
    torque_4 = calculate_torque(T[3], math.degrees(alpha), dist_from_center)      #Pos torque

    total_torque = (-1*torque_1) + torque_2 + (-1*torque_3) + torque_4

    ang_accelo = total_torque/inertia

    print("The AUV's angular acceleration is " + str(ang_accelo) + " rad/s^2.")
    return ang_accelo

    """
    prob linear accelo
    F_xnet = T1cos(alpha)-T4cos(alpha)+T2cos(alpha)-T3cos(alpha)
    F_ynet = T1sin(alpha)-T2sn(alpha)-T3sin(alpha)+T4sin(alpha)
    (F_xnet, F_ynet) --> mult by rotation matrix
    
    """



calculate_auv2_angular_acceleration([10, 1, 4, 0], 0.5, np.sqrt(2), np.sqrt(2), 100)

#Problem 10 Part 1
def simulate_auv2_motion(T, alpha, L ,l ,mass, inertia, dt, t_final, x0, y0, theta0):
    """Given an AUV with origial configurations, what happens over time when T forces are applied?"""
    t = np.array([])        #t: an np.ndarray of the time steps of the simulation in seconds.
    x = np.array([])        #x: an np.ndarray of the x-positions of the AUV in meters.
    y = np.array([])        #y: an np.ndarray of the y-positions of the AUV in meters.
    theta = np.array([])    #theta: an np.ndarray of the angles of the AUV in radians.
    v = np.array([])        #v: an np.ndarray of the velocities of the AUV in meters per second.
    omega = np.array([])    #omega: an np.ndarray of the angular velocities of the AUV in radians per second.
    a = np.array([])        #a: an np.ndarray of the accelerations of the AUV in meters per second squared.

    initial_ang_velocity = 0

    for i in np.arange(0, t_final, dt):
        time_passed = i
        accelo, direction_angle = calculate_auv2_acceleration(T, alpha, theta0, mass)     #Gives accelo and direction
        ang_accelo = calculate_auv2_angular_acceleration(T, alpha, L, l, inertia)        #Gives angular acceleration
        torque = ang_accelo*inertia
        
        displacement = 0.5*accelo*(dt**2)           #Tells how much moved before last dt
        x_new = displacement*np.cos(direction_angle) + x0
        y_new = displacement*np.sin(direction_angle) + y0

        velocity = displacement/dt

        new_angle = theta0 + ((torque*dt*dt)/(2*inertia))       #Tells ang velocity and ang measure
        new_ang_velocity = initial_ang_velocity + ((torque*dt)/inertia)

        t = np.append(t, time_passed)       #Add all calculated values to array to keep track of data
        x = np.append(x, x_new)
        y = np.append(y, y_new)
        v = np.append(v, velocity)
        theta = np.append(theta, new_angle)
        omega = np.append(omega, new_ang_velocity)
        a = np.append(a, accelo)

        theta0 = new_angle
        x0 = x_new
        y0 = y_new
        initial_ang_velocity = new_ang_velocity
    
    return t, x, y, v, theta, omega, a