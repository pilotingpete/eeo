import numpy as np
import matplotlib.pyplot as plt

# Frequency range
f = np.logspace(0, 6, 1000)

# Transfer function coefficients
gm1 = 0.25e-3
gm2 = 0.25e-3
gm5 = 2.5e-3
ro2 = 400e3
ro4 = 400e3
ro5 = 40e3
C1 = 0.1e-12
Cc = 2e-12
RL = 1e3

# Transfer function without compensation (U)
H_U = gm1 * gm2 * gm5 / ((1 + 1j * f / (gm5 * ro5)) * (1 + 1j * f / (gm2 * ro2)) * (1 + 1j * f / (gm1 * (ro4 + RL))) * (1 + 1j * f * C1 / gm1))

# Transfer function with compensation (C)
H_C = gm1 * gm2 * gm5 / ((1 + 1j * f / (gm5 * ro5)) * (1 + 1j * f / (gm2 * ro2)) * (1 + 1j * f / (gm1 * (ro4 + RL + Cc))) * (1 + 1j * f * C1 / gm1))

# Magnitude plot
plt.figure()
plt.semilogx(f, 20 * np.log10(np.abs(H_U)), label='Uncompensated (U)')
plt.semilogx(f, 20 * np.log10(np.abs(H_C)), label='Compensated (C)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Bode Plot - Magnitude Response')
plt.grid(True)
plt.legend()

# Phase plot
plt.figure()
plt.semilogx(f, np.angle(H_U, deg=True), label='Uncompensated (U)')
plt.semilogx(f, np.angle(H_C, deg=True), label='Compensated (C)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.title('Bode Plot - Phase Response')
plt.grid(True)
plt.legend()

plt.show()
