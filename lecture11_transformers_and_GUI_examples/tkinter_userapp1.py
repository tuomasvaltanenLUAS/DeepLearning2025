# Import the tkinter module
# code template originally from:
# https://www.geeksforgeeks.org/python/how-to-set-text-of-tkinter-text-widget-with-a-button/
import tkinter
import pandas as pd
import numpy as np
import tensorflow as tf
import keras

# load model
model = keras.saving.load_model("mobilephonemodel.keras")

# category names for predictions
categories = ['1: Cheap', '2: Avg-', '3: Avg+', '4: Expensive']

# ALSO ALWAYS TEST THE MODEL LOAD BEFORE GOING ANY FURTHER WITH UI
# these are the fields we need to get from the UI
# let's try with some new imaginary data
# modify this as needed regarding your own dataset
# tester_row = {
#     'battery_power': 1021, 
#     'fc': 0, 
#     'int_memory': 53, 
#     'mobile_wt': 136, 
#     'n_cores': 3, 
#     'pc': 6,
#     'px_height': 905, 
#     'px_width': 1988, 
#     'ram': 3031, 
#     'sc_h': 17, 
#     'sc_w': 3, 
#     'talk_time': 7 
# }

# # convert to pandas-format
# tester_row = pd.DataFrame([tester_row])
# result = model.predict(tester_row)[0]
# result_text = categories[np.argmax(result)]

# # switch to decimal representation 
# np.set_printoptions(precision=9, suppress=True)

# # 0 cheapest, 3 most expensive
# print(f"Predicted price range: {result_text}")
# print()
# print("Probabilities by class:")
# print(categories)
# print(result)


# Creating the GUI window.
window = tkinter.Tk()
window.title("Mobile phone Price Predicterator v.1.0341246abf")
window.geometry("500x780")
window.option_add("*font", "lucida 12 bold")

# labels and entries for each variable in the model

# create text label for the Entry with some vertical padding (pady)
label1 = tkinter.Label(window, text="Battery Power (mAh)")
label1.pack(pady=4)

# create entry for battery
entry_battery = tkinter.Entry(window)
entry_battery.pack(pady=0)
 
# create text label for the Entry with some vertical padding (pady)
label2 = tkinter.Label(window, text="Front camera (MP)")
label2.pack(pady=4)

# create entry for battery
entry_frontcam = tkinter.Entry(window)
entry_frontcam.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label3 = tkinter.Label(window, text="Primary camera (MP)")
label3.pack(pady=4)

# create entry for battery
entry_primarycam = tkinter.Entry(window)
entry_primarycam.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label4 = tkinter.Label(window, text="Internal memory (Gb)")
label4.pack(pady=4)

# create entry for battery
entry_intmemory = tkinter.Entry(window)
entry_intmemory.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label5 = tkinter.Label(window, text="RAM (Mb)")
label5.pack(pady=4)

# create entry for battery
entry_ram = tkinter.Entry(window)
entry_ram.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label6 = tkinter.Label(window, text="Weight (g)")
label6.pack(pady=4)

# create entry for battery
entry_weight = tkinter.Entry(window)
entry_weight.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label7 = tkinter.Label(window, text="Width (px)")
label7.pack(pady=4)

# create entry for battery
entry_width_px = tkinter.Entry(window)
entry_width_px.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label8 = tkinter.Label(window, text="Height (px)")
label8.pack(pady=4)

# create entry for battery
entry_height_px = tkinter.Entry(window)
entry_height_px.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label9 = tkinter.Label(window, text="Width (cm)")
label9.pack(pady=4)

# create entry for battery
entry_width_cm = tkinter.Entry(window)
entry_width_cm.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label10 = tkinter.Label(window, text="Height (cm)")
label10.pack(pady=4)

# create entry for battery
entry_height_cm = tkinter.Entry(window)
entry_height_cm.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label11 = tkinter.Label(window, text="Number of cores")
label11.pack(pady=4)

# create entry for battery
entry_cores = tkinter.Entry(window)
entry_cores.pack(pady=0)

# create text label for the Entry with some vertical padding (pady)
label12 = tkinter.Label(window, text="Talk time (h)")
label12.pack(pady=4)

# create entry for battery
entry_talktime = tkinter.Entry(window)
entry_talktime.pack(pady=0)

# Creating the function to set the text 
# with the help of button
def set_prediction_result():
    tester_row = {
        'battery_power': int(entry_battery.get()), 
        'fc': int(entry_frontcam.get()), 
        'int_memory': int(entry_intmemory.get()), 
        'mobile_wt': int(entry_weight.get()),
        'n_cores': int(entry_cores.get()),
        'pc': int(entry_primarycam.get()),
        'px_width': int(entry_width_px.get()),
        'px_height': int(entry_height_px.get()), 
        'ram': int(entry_ram.get()),
        'sc_h': int(entry_height_cm.get()), 
        'sc_w': int(entry_width_cm.get()), 
        'talk_time': int(entry_talktime.get()), 
    }

    categories = ['1: Cheap', '2: Avg-', '3: Avg+', '4: Expensive']

    tester_row = pd.DataFrame([tester_row])
    result = model.predict(tester_row)[0]
    result_text = categories[np.argmax(result)]
    
    result_string.set(f"Prediction: {result_text}")

# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = tkinter.Button(window, height=1, width=10, text="Set", 
                    command=set_prediction_result)

set_up_button.pack()

result_string = tkinter.StringVar()
result_string.set("Waiting for user input...")

# connect the string variable into a label
label_result = tkinter.Label(window, textvariable=result_string, fg="red")
label_result.pack()

window.mainloop()