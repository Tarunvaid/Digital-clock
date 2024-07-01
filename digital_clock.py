import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Define the clock update function
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # Update the time every 1 second (1000 milliseconds)

# Create and configure the label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='white', foreground='black')
label.pack(anchor='center')

# Call the time function to initiate the clock
time()

# Run the main loop
root.mainloop()
