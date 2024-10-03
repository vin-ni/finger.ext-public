import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import neurokit2 as nk
from tkinter import Tk, filedialog

# Hide the root window
root = Tk()
root.withdraw()

# Ask the user to select a file
file_path = filedialog.askopenfilename(title="Select the info.json file", filetypes=[("JSON files", "*.json")])

if not file_path:
    print("No file selected.")
    exit()

# Extract the data directory and base filename
data_dir = os.path.dirname(file_path)
base_filename = os.path.basename(file_path).replace('_info.json', '')

# Full path to the info.json file
info_json_path = file_path

# Read the info.json file
with open(info_json_path, 'r') as f:
    info_json = json.load(f)

# Find the EDA, HR, and Temperature channel information
eda_info = None
hr_info = None
temp_info = None
for item in info_json:
    if item['info']['name'] == 'ElectrodermalActivity':
        eda_info = item
    if item['info']['name'] == 'HeartRate':
        hr_info = item
    if item['info']['name'] == 'Temperature1':
        temp_info = item

# Check if the necessary data was found
if eda_info is None:
    print('ElectrodermalActivity data not found in info.json')
    exit()

if hr_info is None:
    print('HeartRate data not found in info.json')
    exit()

if temp_info is None:
    print('Temperature data not found in info.json')
    exit()

# Extract typeTags
eda_typeTag = eda_info['info']['typeTags'][0]
hr_typeTag = hr_info['info']['typeTags'][0]
temp_typeTag = temp_info['info']['typeTags'][0]

# File paths for EDA, HR, and Temperature data
eda_filename = f'{base_filename}_{eda_typeTag}.csv'
hr_filename = f'{base_filename}_{hr_typeTag}.csv'
temp_filename = f'{base_filename}_{temp_typeTag}.csv'

eda_filepath = os.path.join(data_dir, eda_filename)
hr_filepath = os.path.join(data_dir, hr_filename)
temp_filepath = os.path.join(data_dir, temp_filename)

# Read EDA data
eda_data = pd.read_csv(eda_filepath)

# Read Heart Rate data
hr_data = pd.read_csv(hr_filepath)

# Read Temperature data
temp_data = pd.read_csv(temp_filepath)

# Convert 'LocalTimestamp' to human-readable datetime
if 'LocalTimestamp' in eda_data.columns:
    eda_data['LocalTimestamp'] = pd.to_datetime(eda_data['LocalTimestamp'], unit='ms')  # Assuming it's in milliseconds
    x_eda = eda_data['LocalTimestamp']
else:
    x_eda = eda_data.index

if 'LocalTimestamp' in hr_data.columns:
    hr_data['LocalTimestamp'] = pd.to_datetime(hr_data['LocalTimestamp'], unit='ms')
    x_hr = hr_data['LocalTimestamp']
else:
    x_hr = hr_data.index

if 'LocalTimestamp' in temp_data.columns:
    temp_data['LocalTimestamp'] = pd.to_datetime(temp_data['LocalTimestamp'], unit='ms')
    x_temp = temp_data['LocalTimestamp']
else:
    x_temp = temp_data.index

# Process the EDA signal using NeuroKit2
eda_signal = eda_data[eda_typeTag]
signals, info = nk.eda_process(eda_signal, sampling_rate=1000)  # Adjust sampling_rate as needed

# Create the plot with subplots for EDA, Heart Rate, and Temperature
fig, ax = plt.subplots(5, 1, figsize=(19.2, 10.8))  # 5 rows for raw EDA, tonic, phasic, HR, and Temp

# Raw EDA signal
ax[0].plot(x_eda, signals["EDA_Raw"], label='Raw EDA')
ax[0].set_title('Raw EDA Signal')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('EDA (microsiemens)')
ax[0].legend()
ax[0].grid(True)

# Tonic EDA component
ax[1].plot(x_eda, signals["EDA_Tonic"], label='Tonic Component', color='green')
ax[1].set_title('Tonic EDA Component')
ax[1].set_xlabel('Time')
ax[1].set_ylabel('EDA (microsiemens)')
ax[1].legend()
ax[1].grid(True)

# Phasic EDA component
ax[2].plot(x_eda, signals["EDA_Phasic"], label='Phasic Component', color='orange')
ax[2].set_title('Phasic EDA Component')
ax[2].set_xlabel('Time')
ax[2].set_ylabel('EDA (microsiemens)')
ax[2].legend()
ax[2].grid(True)

# Heart Rate plot
ax[3].plot(x_hr, hr_data[hr_typeTag], label='Heart Rate', color='red')
ax[3].set_title(f'Heart Rate Over Time')
ax[3].set_xlabel('Time')
ax[3].set_ylabel('Heart Rate (bpm)')
ax[3].legend()
ax[3].grid(True)

# Temperature plot
ax[4].plot(x_temp, temp_data[temp_typeTag], label='Temperature', color='blue')
ax[4].set_title(f'Temperature Over Time')
ax[4].set_xlabel('Time')
ax[4].set_ylabel('Temperature (°C)')
ax[4].legend()
ax[4].grid(True)

# Adjust layout and save the figure
plt.tight_layout()
save_path = os.path.join(data_dir, f'_{base_filename}_eda_hr_temp_phasic_tonic.png')
fig.savefig(save_path, dpi=100)  # Save the figure

print(f"EDA, Heart Rate, and Temperature plot saved as {save_path}")

# Open the file in Mac Preview (optional)
os.system(f'open "{save_path}"')

# plt.show()  # Display the plot if running interactively
