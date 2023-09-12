import numpy as np
import matplotlib.pyplot as plt

# Given parameters
Eg_0 = 1.17  # Bandgap energy at absolute zero temperature (in eV)
alpha = 4.73e-4  # Alpha parameter (in eV/K)
beta = 636  # Beta parameter (in K)

# Temperature range from 0 to 600 K
T = np.linspace(0, 600, 601)  # Temperature values from 0 to 600 K

# Calculate bandgap energy for each temperature using the Varshni equation
Eg = Eg_0 - (alpha * T**2) / (T + beta)

# Plot Eg vs T
plt.figure(figsize=(8, 6))
plt.plot(T, Eg, label='Bandgap Energy ($E_g$)')
plt.xlabel('Temperature (K)')
plt.ylabel('Bandgap Energy (eV)')
plt.title('Bandgap Energy vs Temperature for a Semiconductor')
plt.grid(True)
plt.legend()

# Show the bandgap energy at T = 300 K
T_300K = 300
Eg_300K = Eg_0 - (alpha * T_300K**2) / (T_300K + beta)
plt.scatter([T_300K], [Eg_300K], color='red', label=f'T = {T_300K} K: {Eg_300K:.2f} eV')
plt.legend()

plt.show()
