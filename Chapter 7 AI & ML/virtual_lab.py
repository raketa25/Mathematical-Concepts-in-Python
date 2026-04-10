print(" ================================  Virtual Laboratory in python ===============================", "\n\n")

# Libraries
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("grayscale")

# Parameters definition
# x = np.linspace(-10, 10, 1000)
n = 1.0                            # mole quantity in moles
R = 8.314                          # ideal gas constant in J/(mol*K)

# Functions definition

# pressure as a function of temperature and volume
def pressure(T, V):
    return n * R * T / V

# temperature as a function of pressure and volume
def temperature(P, V):
    return P * V / (n * R)

# volume as a function of pressure and temperature
def volume(T, P):
    return n * R * T / P

# Normal conditions of pressure and temperature
P0 = 101325                        # standard atmospheric pressure in Pa
T0 = 273.15                        # standard temperature in K

# Let's conduct some experiences in our virtual laboratory with those functions above, using the normal conditions as reference:
# Volume in normal conditions
V0 = volume(T0, P0)
print(f"Volume in normal conditions: {V0} m^3")
print("\n\n")

# Checking that the temperature in normal conditions is correct
T_check = temperature(P0, volume(T0, P0))
print(f"Temperature check: {T_check} K")
print("\n\n")

# Doubling the presure and checking the new temperature
P_double = 2 * P0
T_double = temperature(P_double, volume(T0, P0))
print(f"Temperature when pressure is doubled: {T_double} K")
print("\n\n")


# Plotting the functions
vs = np.linspace(0.01, 1, 100)        # Volume range for plotting

plt.figure(figsize=(13, 6))

# Pressure as a function of volume at constant temperature
plt.subplot(1, 3, 1)
plt.plot(vs, 
        [pressure(T0, v) for v in vs],
        label="P(T) at V=1")
plt.xlabel("Volume (m^3)")
plt.ylabel("Pressure (Pa)")
plt.title("Pressure vs Volume")
plt.legend()

# Temperature as a function of pressure at constant volume
ps = np.linspace(0, 100, 120000)        # Pressure range for plotting
plt.subplot(1, 3, 2)
plt.plot(ps, 
         [temperature(p, P0) for p in ps], 
         label="T(P) at V=1")
plt.xlabel("Pressure (Pa)")
plt.ylabel("Temperature (K)")
plt.title("Temperature vs Pressure")
plt.legend()

# Temperature as a function of volume at constant pressure
plt.subplot(1, 3, 3)
# V = np.linspace(0.001, 1000000, 1000)
plt.plot(vs, 
         [temperature(P0, v) for v in vs], 
         label="T(V) at P=1")
plt.xlabel("Volume (m^3)")
plt.ylabel("Temperature (K)")
plt.title("Temperature vs Volume")
plt.legend()
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.show()