import numpy as np

# Planck's constant J/s
h = 6.62607015e-34

# Define 1 eV in Joules
eV_to_Joules = 1.60219e-19

def calculate_de_broglie_wavelength(mass_kg, kinetic_energy_J):
    # Calculate momentum from kinetic energy and mass
    momentum = np.sqrt(2 * mass_kg * kinetic_energy_J)
    # Calculate Broglie wavelength using momentum
    wavelength = h / momentum
    return wavelength

# Input parameters
mass_proton_kg = 1.6726219e-27  # Mass of a proton in kilograms
mass_electron_kg = 9.10938356e-31  # Mass of an electron in kilograms
energies = [1.0, 100.0]  # Kinetic energy in electronvolts

for kinetic_energy_eV in energies:
    # Convert kinetic energy from eV to Joules
    kinetic_energy_J = kinetic_energy_eV * eV_to_Joules

    # Calculate Broglie wavelengths
    wavelength_electron = calculate_de_broglie_wavelength(mass_electron_kg, kinetic_energy_J)
    wavelength_proton = calculate_de_broglie_wavelength(mass_proton_kg, kinetic_energy_J)

    # Print results
    print(f"Broglie wavelength for an electron with {kinetic_energy_eV} eV kinetic energy: {wavelength_electron:.6e} meters")
    print(f"Broglie wavelength for a proton with {kinetic_energy_eV} eV kinetic energy: {wavelength_proton:.6e} meters")
