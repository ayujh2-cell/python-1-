EARTH_GRAVITY = 9.81
MOON_GRAVITY = 1.62

def calculate_weight(mass, gravity):
    return mass * gravity

# User input
mass = float(input("Enter the mass of the object in kg: "))

weight_earth = calculate_weight(mass, EARTH_GRAVITY)
weight_moon = calculate_weight(mass, MOON_GRAVITY)

layout = f"An object with a mass of {mass} kg weighs:\n- {weight_earth:.2f} N on Earth\n- {weight_moon:.2f} N on the Moon"
