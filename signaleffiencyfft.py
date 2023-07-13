'''ignore this way '''

import numpy as np
import matplotlib.pyplot as plt

# Generate a sample audio signal
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration in seconds
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
frequency = 440  # Frequency of the audio signal
audio_signal = np.sin(2 * np.pi * frequency * t)

# Perform FFT on the audio signal
fft_result = np.fft.fft(audio_signal)

# Calculate the frequencies corresponding to the FFT result
frequencies = np.fft.fftfreq(len(audio_signal), 1.0 / sample_rate)

# Plot the frequency spectrum
plt.plot(frequencies[:len(frequencies)//2], np.abs(fft_result[:len(frequencies)//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.show()


import pandas as pd

# Assuming you have a list of timestamps and corresponding signal values
timestamps = ['2023-07-01 00:00:00', '2023-07-01 00:15:00', '2023-07-01 00:30:00']
signal_values = [10, 20, 30]

# Create a DataFrame with the timestamps and signal values
df = pd.DataFrame({'Timestamp': pd.to_datetime(timestamps), 'Signal': signal_values})

# Set the timestamp column as the DataFrame index
#df.set_index('Timestamp', inplace=True)
import pandas as pd

# Assuming you have a list of timestamps and corresponding signal values
timestamps = ['2023-07-01 00:00:00', '2023-07-01 00:15:00', '2023-07-01 00:30:00']
signal_values = [10, 20, 30]

# Create a DataFrame with the timestamps and signal values
df = pd.DataFrame({'Timestamp': pd.to_datetime(timestamps), 'Signal': signal_values})

# Set the timestamp column as the DataFrame index
df.set_index('Timestamp', inplace=True) # basically with this instead of having index column and timestam and signal your index is your timestamp

# Convert the DataFrame into a time series
time_series = df['Signal'] # converting signal in he dataframe

# Print the resulting time series
print(time_series)

'''now for many signals'''

import pandas as pd

# Assuming you have a list of timestamps and corresponding signal values for each of the 500 signals
timestamps_list = [
    ['2023-07-01 00:00:00', '2023-07-01 00:15:00', '2023-07-01 00:30:00'],  # Timestamps for Signal 1
    ['2023-07-01 00:01:00', '2023-07-01 00:16:00', '2023-07-01 00:31:00'],  # Timestamps for Signal 2
    ['2023-07-01 00:02:00', '2023-07-01 00:17:00', '2023-07-01 00:32:00']   # Timestamps for Signal 3
]  # List of lists, where each inner list represents the timestamps for a signal
signal_values_list = [[10, 20, 30],
                      [40, 50, 60],
                      [70, 80, 90]]  # List of lists, where each inner list represents the signal values for a signal

# Create a dictionary to hold the data for each signal
data_dict = {'Timestamp': pd.to_datetime(timestamps_list[0])}  # Use the timestamps from the first signal as the base

# Add each signal as a separate column in the dictionary
for i in range(len(signal_values_list)):
    data_dict[f'Signal{i+1}'] = signal_values_list[i]

# Create the DataFrame from the dictionary
df = pd.DataFrame(data_dict)

# Set the timestamp column as the DataFrame index
df.set_index('Timestamp', inplace=True)

'''now iterate to convert- this bit is wrong for what i want to do '''

signal_series_list = []

# Iterate over the columns and extract the signal values as series
for column in df.columns:
    if column != 'Timestamp':
        signal_series = df[column]
        signal_series_list.append(signal_series)

import pandas as pd
timestamps_list = [
    ['2023-07-01 00:00:00', '2023-07-01 00:15:00', '2023-07-01 00:30:00'],  # Timestamps for Signal 1
    ['2023-07-01 00:01:00', '2023-07-01 00:16:00', '2023-07-01 00:31:00'],  # Timestamps for Signal 2
    ['2023-07-01 00:02:00', '2023-07-01 00:17:00', '2023-07-01 00:32:00']   # Timestamps for Signal 3
]  # List of lists, where each inner list represents the timestamps for a signal
signal_values_list = [[10, 20, 30],
                      [40, 50, 60],
                      [70, 80, 90]]

signal_series_list = []

# Iterate over the lists of timestamps and signal values
for timestamps, signal_values in zip(timestamps_list, signal_values_list):
    signal_series = pd.Series(signal_values, index=timestamps)
    signal_series_list.append(signal_series)


import pandas as pd
import timeit

# Assuming you have a list of timestamps and corresponding signal values for each of the 500 signals
timestamps_list = [
    ['2023-07-01 00:00:00', '2023-07-01 00:15:00', '2023-07-01 00:30:00'],  # Timestamps for Signal 1
    ['2023-07-01 00:01:00', '2023-07-01 00:16:00', '2023-07-01 00:31:00'],  # Timestamps for Signal 2
    ['2023-07-01 00:02:00', '2023-07-01 00:17:00', '2023-07-01 00:32:00']   # Timestamps for Signal 3
]  # List of lists, where each inner list represents the timestamps for a signal
signal_values_list = [[10, 20, 30],
                      [40, 50, 60],
                      [70, 80, 90]]

signal_series_list = [pd.Series(signal_values, index=timestamps) for timestamps, signal_values in zip(timestamps_list, signal_values_list)]


''''execution time '''
import timeit
import pandas as pd

timestamps_list = [
    ['2023-07-01 00:00:00', '2023-07-01 00:15:00', '2023-07-01 00:30:00'],  # Timestamps for Signal 1
    ['2023-07-01 00:01:00', '2023-07-01 00:16:00', '2023-07-01 00:31:00'],  # Timestamps for Signal 2
    ['2023-07-01 00:02:00', '2023-07-01 00:17:00', '2023-07-01 00:32:00']   # Timestamps for Signal 3
]  # List of lists, where each inner list represents the timestamps for a signal
signal_values_list = [[10, 20, 30],
                      [40, 50, 60],
                      [70, 80, 90]]

code = """
import pandas as pd

timestamps_list = [
    ['2023-07-01 00:00:00', '2023-07-01 00:15:00', '2023-07-01 00:30:00'],  # Timestamps for Signal 1
    ['2023-07-01 00:01:00', '2023-07-01 00:16:00', '2023-07-01 00:31:00'],  # Timestamps for Signal 2
    ['2023-07-01 00:02:00', '2023-07-01 00:17:00', '2023-07-01 00:32:00']   # Timestamps for Signal 3
]  # List of lists, where each inner list represents the timestamps for a signal
signal_values_list = [[10, 20, 30],
                      [40, 50, 60],
                      [70, 80, 90]]

signal_series_list = []

# Iterate over the lists of timestamps and signal values
for timestamps, signal_values in zip(timestamps_list, signal_values_list):
    signal_series = pd.Series(signal_values, index=timestamps)
    signal_series_list.append(signal_series)

"""

# Number of repetitions for timing
repetitions = 1000

# Calculate the execution time
execution_time = timeit.timeit(code, number=repetitions, globals=globals())

# Print the execution time
print("Execution time:", execution_time)


import timeit
import pandas as pd

timestamps_list = [
    ['2023-07-01 00:00:00', '2023-07-01 00:15:00', '2023-07-01 00:30:00'],  # Timestamps for Signal 1
    ['2023-07-01 00:01:00', '2023-07-01 00:16:00', '2023-07-01 00:31:00'],  # Timestamps for Signal 2
    ['2023-07-01 00:02:00', '2023-07-01 00:17:00', '2023-07-01 00:32:00']   # Timestamps for Signal 3
]  # List of lists, where each inner list represents the timestamps for a signal
signal_values_list = [[10, 20, 30],
                      [40, 50, 60],
                      [70, 80, 90]]

code = """
import pandas as pd

timestamps_list = [
    ['2023-07-01 00:00:00', '2023-07-01 00:15:00', '2023-07-01 00:30:00'],  # Timestamps for Signal 1
    ['2023-07-01 00:01:00', '2023-07-01 00:16:00', '2023-07-01 00:31:00'],  # Timestamps for Signal 2
    ['2023-07-01 00:02:00', '2023-07-01 00:17:00', '2023-07-01 00:32:00']   # Timestamps for Signal 3
]  # List of lists, where each inner list represents the timestamps for a signal
signal_values_list = [[10, 20, 30],
                      [40, 50, 60],
                      [70, 80, 90]]
signal_series_list = [pd.Series(signal_values, index=timestamps) for timestamps, signal_values in zip(timestamps_list, signal_values_list)]
"""

# Number of repetitions for timing
repetitions = 1000

# Calculate the execution time
execution_time = timeit.timeit(code, number=repetitions, globals=globals())

# Print the execution time
print("Execution time:", execution_time)