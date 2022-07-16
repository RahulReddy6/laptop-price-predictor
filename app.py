import pickle

import numpy as np
import streamlit as st

pipe = pickle.load(open('pipe.pkl', 'rb'))
data = pickle.load(open('data.pkl', 'rb'))

st.title('Laptop Price Predictor')

Company = st.selectbox('Company brand', data['Company'].unique())

Laptop_type = st.selectbox('Type', data['TypeName'].unique())

Ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 32, 64])

Weight = st.number_input('Weight of laptop')

Touch_Screen = st.selectbox('Touch Screen', ['YES', 'NO'])

IPS = st.selectbox('IPS', ['YES', 'NO'])

Screen_size = st.number_input('Screen Size')

Resolution = st.selectbox('Screen Resolution', ['2560x1600', '1440x900', '1920x1080', '2880x1800', '1366x768',
                                                '2304x1440', '3200x1800', '1920x1200', '2256x1504', '3840x2160',
                                                '2160x1440', '2560x1440', '1600x900', '2736x1824', '2400x1600'])

CPU = st.selectbox('CPU', data['CPU type'].unique())

HDD = st.selectbox('HDD (in GB)', [0, 256, 512, 1024])

SSD = st.selectbox('SSD (in GB)', data['SSD'].unique())

GPU = st.selectbox('GPU', data['GPU'].unique())

Operating_System = st.selectbox('Operating System', data['OS type'].unique())

if st.button('Predict Price '):

    x_resolution = int(Resolution.split('x')[0])
    y_resolution = int(Resolution.split('x')[1])

    PPI = ((x_resolution ** 2) + (y_resolution ** 2)) ** 0.5 / Screen_size

    if Touch_Screen == 'YES':
        Touch_Screen = 1
    else:
        Touch_Screen = 0
    if IPS == 'YES':
        IPS = 1
    else:
        IPS = 0

    query = np.array([Company, Laptop_type, Ram, Weight, Touch_Screen, IPS, PPI, CPU, HDD, SSD, GPU, Operating_System])

    query = query.reshape(1, 12)

    st.title(" The price of selected laptop is " + str(int(np.exp(pipe.predict(query)[0]))))
