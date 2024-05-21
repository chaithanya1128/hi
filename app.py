import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('mobile_price_model.pkl')

# Load the label encoders
label_encoders = {}  # Load your label encoders similarly if needed

# Define the input fields
st.title('Mobile Price Prediction')
battery_capacity = st.number_input('Battery capacity (mAh)')
screen_size = st.number_input('Screen size (inches)')
touchscreen = st.selectbox('Touchscreen', [0, 1])  # Assuming 0 for No and 1 for Yes
resolution_x = st.number_input('Resolution x')
resolution_y = st.number_input('Resolution y')
processor = st.number_input('Processor')
ram = st.number_input('RAM (MB)')
internal_storage = st.number_input('Internal storage (GB)')
rear_camera = st.number_input('Rear camera (MP)')
front_camera = st.number_input('Front camera (MP)')
operating_system = st.selectbox('Operating system', [0, 1])  # Example values
wifi = st.selectbox('Wi-Fi', [0, 1])
bluetooth = st.selectbox('Bluetooth', [0, 1])
gps = st.selectbox('GPS', [0, 1])
num_sims = st.number_input('Number of SIMs')
three_g = st.selectbox('3G', [0, 1])
four_g = st.selectbox('4G/ LTE', [0, 1])

# Make prediction
if st.button('Predict'):
    input_data = pd.DataFrame({
        'Battery capacity (mAh)': [battery_capacity],
        'Screen size (inches)': [screen_size],
        'Touchscreen': [touchscreen],
        'Resolution x': [resolution_x],
        'Resolution y': [resolution_y],
        'Processor': [processor],
        'RAM (MB)': [ram],
        'Internal storage (GB)': [internal_storage],
        'Rear camera': [rear_camera],
        'Front camera': [front_camera],
        'Operating system': [operating_system],
        'Wi-Fi': [wifi],
        'Bluetooth': [bluetooth],
        'GPS': [gps],
        'Number of SIMs': [num_sims],
        '3G': [three_g],
        '4G/ LTE': [four_g]
    })
    
    # Transform categorical variables using label encoders if needed
    for column in input_data.select_dtypes(include=['object']).columns:
        le = label_encoders.get(column)
        if le:
            input_data[column] = le.transform(input_data[column])

    # Make prediction
    prediction = model.predict(input_data)
    st.write(f'Predicted Price: {prediction[0]:.2f}')
