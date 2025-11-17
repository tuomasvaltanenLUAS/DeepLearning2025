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


# # Creating the GUI window.
# window = tkinter.Tk()
# window.title("Title here")
# window.geometry("800x100")

# # Creating our text widget.
# sample_text = tkinter.Entry(window)
# sample_text.pack()

# # Creating the function to set the text 
# # with the help of button
# def set_text_by_button():

#     # Delete is going to erase anything
#     # in the range of 0 and end of file,
#     # The respective range given here
#     sample_text.delete(0,"end")
    
#     # Insert method inserts the text at
#     # specified position, Here it is the
#     # beginning
#     sample_text.insert(0, "Text set by button")

# # Setting up the button, set_text_by_button() 
# # is passed as a command
# set_up_button = tkinter.Button(window, height=1, width=10, text="Set", 
#                     command=set_text_by_button)

# set_up_button.pack()

# window.mainloop()