import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
from pathlib import Path


def generate_bode_plot(csv_filepath):
    # Load the data from the CSV file
    data = pd.read_csv(csv_filepath)
    time = data["Time(s)"].to_numpy()
    input_waveform = data["CH1(V)"].to_numpy()
    output_waveform = data["CH2(V)"].to_numpy()

    # Check for and remove NaN values
    valid_indices = ~np.isnan(input_waveform) & ~np.isnan(output_waveform)
    time = time[valid_indices]
    input_waveform = input_waveform[valid_indices]
    output_waveform = output_waveform[valid_indices]

    # Check for sufficient time resolution
    if len(time) < 2 or (time[-1] - time[0]) == 0:
        print("Insufficient time data or zero time difference.")
        return

    # Calculate the sampling frequency from time data
    fs = 1.0 / (time[-1] - time[0])  # Sample rate, calculated from time data

    # Calculate the frequency response
    frequencies, response = signal.freqz(output_waveform, input_waveform, fs=fs)

    # Calculate magnitude and phase in degrees
    magnitude = 20 * np.log10(np.abs(response))
    phase = np.angle(response, deg=True)

    # Find the -3dB point
    minus_3dB_index = np.argmin(np.abs(magnitude + 3.0))
    minus_3dB_frequency = frequencies[minus_3dB_index]

    # Create the Bode plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    plt.subplots_adjust(hspace=0.5)

    # Magnitude plot
    ax1.semilogx(frequencies, magnitude)
    ax1.set_title("Bode Plot - Magnitude Response")
    ax1.set_xlabel("Frequency (Hz)")
    ax1.set_ylabel("Magnitude (dB)")
    ax1.grid()

    # Mark the -3dB point on the magnitude plot
    ax1.plot(
        frequencies[minus_3dB_index],
        magnitude[minus_3dB_index],
        "ro",
        label="-3dB Point",
    )
    ax1.legend()

    # Add text annotation for the -3dB value
    ax1.annotate(
        f"-3dB at {minus_3dB_frequency:.2f} Hz",
        xy=(frequencies[minus_3dB_index], magnitude[minus_3dB_index]),
        xytext=(frequencies[minus_3dB_index], magnitude[minus_3dB_index] - 10),
        arrowprops=dict(arrowstyle="->"),
    )

    # Phase plot
    ax2.semilogx(frequencies, phase)
    ax2.set_title("Bode Plot - Phase Response")
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Phase (degrees)")
    ax2.grid()

    plt.show()


if __name__ == "__main__":
    csv_filepath = Path("C:/eeo/eeo-352/assignments/scope-data/lpf2.csv")
    generate_bode_plot(csv_filepath)
