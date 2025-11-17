# pip install streamlit
import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

# load the mobile phone price model
model = load_model("mobilephonemodel.keras")

# category names for predictions
categories = ['1: Cheap', '2: Avg-', '3: Avg+', '4: Expensive']

# these are the fields we need to get from the UI
# in order to use our model
# tester_row = {
#     'battery_power': 800, 
#     'fc': 12, 
#     'int_memory': 2,  
#     'mobile_wt': 300, 
#     'n_cores': 4, 
#     'pc': 36,
#     'px_width': 1890,
#     'px_height': 1222, 
#     'ram': 8096,
#     'sc_h': 13, 
#     'sc_w': 4, 
#     'talk_time': 19
# }

# quickly test that the model works as in the Jupyter
# convert to pandas-format
# this works okay!
# tester_row = pd.DataFrame([tester_row])
# result = model.predict(tester_row)[0]
# result_text = categories[np.argmax(result)]
# print(result_text)

# STREAMLIT APP START
# https://www.geeksforgeeks.org/python/a-beginners-guide-to-streamlit/
# title of the streamlit app
st.title("Mobile phone prices model")

# title of the sidebar for inputs
st.sidebar.title("Input features")

continuous_var1 = st.sidebar.slider("Battery power", min_value=500.0, max_value=2500.0, value=1200.0, step=50.0)
continuous_var2 = st.sidebar.slider("Front camera (MP)", min_value=0.0, max_value=20.0, value=4.0, step=1.0)
continuous_var3 = st.sidebar.slider("Primary camera (MP)", min_value=0.0, max_value=24.0, value=10.0, step=1.0)
continuous_var4 = st.sidebar.slider("Internal memory (Gb)", min_value=2.0, max_value=64.0, value=16.0, step=1.0)
continuous_var5 = st.sidebar.slider("No. cores", min_value=1.0, max_value=8.0, value=4.0, step=1.0)
continuous_var6 = st.sidebar.slider("RAM (Mb)", min_value=256.0, max_value=8096.0, value=2048.0, step=8.0)
continuous_var7 = st.sidebar.slider("Height (px)", min_value=256.0, max_value=2560.0, value=768.0, step=8.0)
continuous_var8 = st.sidebar.slider("Width (px)", min_value=256.0, max_value=2560.0, value=960.0, step=8.0)
continuous_var9 = st.sidebar.slider("Screen height (cm)", min_value=5.0, max_value=20.0, value=12.0, step=0.5)
continuous_var10 = st.sidebar.slider("Screen width (cm)", min_value=4.0, max_value=20.0, value=8.0, step=0.5)
continuous_var11 = st.sidebar.slider("Talk time (h)", min_value=2.0, max_value=25.0, value=11.0, step=1.0)
continuous_var12 = st.sidebar.slider("Weight (g)", min_value=80.0, max_value=200.0, value=130.0, step=5.0)

# wrap up the variables in the original order
# in NumPy -array format

# FOLLOW THE SAME ORDER AS IN THE ORIGINAL TESTER ROW
input_data = np.array([[
    continuous_var1,
    continuous_var2,
    continuous_var4,
    continuous_var12,
    continuous_var5,
    continuous_var3,
    continuous_var8,
    continuous_var7,
    continuous_var6,
    continuous_var9,
    continuous_var10,
    continuous_var11
]], dtype=float)

st.image("smartphone.jpg", caption="Smartphone", use_container_width=True)

# the button that predicts through the model
if st.button("Predict"):
    st.subheader("Prediction:")
    # tester_row = pd.DataFrame([tester_row])
    result = model.predict(input_data)[0]
    result_text = categories[np.argmax(result)]
    st.write(result_text)


# to run this app, use this command:
# if your app is in a subfolder, change into that subfolder first
# or run the app from root, and adjust the file paths above

# streamlit run streamlit_ui_example.py

# if using from root, try:
# streamlit run /lecture11_transformers_and_gui/streamlit_ui_example.py