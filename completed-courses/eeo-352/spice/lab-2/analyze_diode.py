import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/home/pete/code/eeo/eeo-352/spice/lab-2/diode.csv', delimiter=';')

# Find the columns that contain 'Id(D1)' or similar names for current
current_column = next((col for col in df.columns if 'Id(D1)' in col), None)

if current_column is None:
    print("Column with diode current data not found in the CSV file.")
else:
    # Extract relevant columns
    time = df['Time']
    current = df[current_column]
    voltage = df['V(Vin)']

    # Plot the current-voltage characteristic
    plt.figure(figsize=(10, 6))
    plt.plot(voltage, current, label='Diode Current')
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    plt.title('Diode Current vs. Voltage Characteristic')
    plt.grid(True)
    plt.legend()

    # Find the index where current is closest to 20mA (0.02A)
    desired_current = 0.02
    index_20ma = (current - desired_current).abs().idxmin()
    voltage_20ma = voltage[index_20ma]

    # Calculate dynamic resistance using the derivative method (finite difference)
    delta_voltage = voltage_20ma - voltage[index_20ma - 1]
    delta_current = current[index_20ma] - current[index_20ma - 1]
    dynamic_resistance = delta_voltage / delta_current

    print(f'Voltage at 20mA: {voltage_20ma} V')
    print(f'Dynamic Resistance at 20mA: {dynamic_resistance:.2f} ohms')

    # Show the plot
    plt.show()