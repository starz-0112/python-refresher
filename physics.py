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
    
