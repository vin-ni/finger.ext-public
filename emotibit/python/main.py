import threading
import numpy as np
import time
from osc_receiver import server, dispatcher
from visualizer import setup_plot, update_plot
from data_processor import process_eda
import neurokit2 as nk
import tkinter as tk
import subprocess

# This will store our incoming EDA data
eda_data = []
total_eda_cleaned = []
total_eda_phasic = []

# Bash commands for touch simulation
def like():
    subprocess.run("adb shell input tap 1000 1416 ", shell=True)

def swipe():
    subprocess.run("adb shell input swipe 500 1200 500 800 100", shell=True)

def eda_handler(address, *args):
    # Assuming the data is sent as a list of EDA values
    eda_data.extend(args)

def start_server():
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("OSC Server closed.")

def main_loop():
    time.sleep(1.5)
    fig, ax = setup_plot()
    # set range of plot
    ax.set_ylim(0, 4)

    while True:
        # if the lenght of eda_data is greater 15

        if True:
        # if eda_data:
            # Ensure no NaN values before processing
            # cleaned_data = [x for x in eda_data if not np.isnan(x)]
           
            eda_cleaned, eda_phasic =  process_eda(eda_data)

            # Append the processed data to the total
            total_eda_cleaned.extend(eda_cleaned)
            total_eda_phasic.extend(eda_phasic)

            # get the last 150 samples 
            last_150_samples = total_eda_cleaned[-150:]

            # update plot
            # update_plot(ax, last_150_samples)
            #nk.eda_plot(eda_phasic, sampling_rate=15)
            eda_signals, eda_info = nk.eda_process(eda_data, sampling_rate=15)
                
                # Plot the EDA signal with detected peaks
            nk.eda_plot(eda_signals, eda_info, static=True)

            
            # Check for peaks in the phasic component
            try:
                peaks, _ = nk.eda_peaks(eda_phasic, sampling_rate=15, method="neurokit")
                peak_indices = np.where(peaks["SCR_Peaks"] == 1)[0]
                print(peak_indices)
                #peak_indices = peak_indices[peak_indices < len(last_150_samples)]
                update_plot(ax, last_150_samples)

                if len(peak_indices) > 0:
                    print("Peak detected!")
            except ValueError:
                print("No peaks detected.")

            # Clear the data after processing
            # eda_data.clear()

        time.sleep(0.1)  # Adjust sleep time as needed for your data rate

if __name__ == "__main__":
    # Setup OSC data reception
    dispatcher.map("/EmotiBit/0/EDA", eda_handler)
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    print("started server")

    # Set up interface
    root = tk.Tk()
    button1 = tk.Button(root, text="Like", command=like)
    button1.pack()
    button2 = tk.Button(root, text="Swipe", command=swipe)
    button2.pack()
    print("Setup Interface")

    # Start the main processing loop
    main_loop()  

    # this is not running right now.
    root.mainloop()
