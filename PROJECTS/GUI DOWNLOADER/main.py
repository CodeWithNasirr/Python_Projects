import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress_bar['value'] = 0
    max_value = 100
    progress_bar['maximum'] = max_value

    for i in range(1, max_value + 1):
        # Update progress value
        progress_bar['value'] = i
        # Update the window to show the progress
        root.update_idletasks()
        time.sleep(0.05)  # Simulate a task taking time

# Create the main window
root = tk.Tk()
root.title("Professional Progress Bar")

# Create a frame to hold the progress bar and button
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create and place the progress bar
progress_bar = ttk.Progressbar(frame, orient='horizontal', mode='determinate', length=300)
progress_bar.grid(row=0, column=0, padx=5, pady=5)

# Create and place the start button
start_button = ttk.Button(frame, text="Start", command=start_progress)
start_button.grid(row=1, column=0, padx=5, pady=5)

# Make the window resize properly
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

# Start the Tkinter main loop
root.mainloop()
