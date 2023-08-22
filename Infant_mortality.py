#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Loading the saved model
with open("random_forest_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# Creating a function for Prediction
def mortality_prediction(input_data):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        st.image('high.png')
        return 'Zip Code Infant Mortality is High'
    else:
        st.image('low.png')
        return 'Zip Code Infant Mortality is low'

def main():
    # Giving a title
    st.title('Welcome ealy infant mortality Prediction Web App based on Zip Code in South Carolina')
    st.markdown("<span style='font-size: 20px;'><strong>By Sohel Ahmed</strong></span>", unsafe_allow_html=True)
    image = Image.open("south_infant.png")
    st.image(image, use_column_width=True)
    # Getting the input data from the user
    PCPs = st.text_input('PCPs per 1000')
    OBGYNs = st.text_input('OB GYNs per 1000')
    PCP30min = st.text_input('Percentage 30 Minutes from PCP')
    OBGYN30min = st.text_input('Percentage 30 Minutes from OBGYN')
    Hospital30min = st.text_input('Percentage 30 Minutes from Hospital')
    Hospital30minOB = st.text_input('Percentage from 30 Minutes from OB Hospital Unit')
    Hospital = st.text_input('Number of Hospital')
    AmbSurgical = st.text_input('Number of Ambulance Surgical Centers')
    Homehealth = st.text_input('Number of Home Health Agencies')
    Hospice = st.text_input('Number of Hospice')
    Birthing = st.text_input('Number of Birthing Centers')
    Midwives = st.text_input('Number of Midwives')
    Dialysis = st.text_input('Number of Dialysis Facilities')
    Nursing=st.text_input('Number of Nursing Homes')
    Treatment = st.text_input('Number of Treatment facilities')
    FQHC = st.text_input('Number of FQHC RHC')
    Other = st.text_input('Number of Other Facilities')
    Labor = st.text_input('Percent Labor Force Participation')
    Unemployed = st.text_input('Percent Unemployed')
    Uninsured = st.text_input('Percent Uninsured')
    Capita = st.text_input('Per Capita Income')
    Poverty= st.text_input('Percent in Poverty')
    Kids = st.text_input('Percent With Kids in Poverty')
    SNAP = st.text_input('Percent With SNAP Benefits')

    # Code for Prediction
    diagnosis = ''

    # Creating a button for Prediction
    if st.button('Infant Mortality'):
        diagnosis = mortality_prediction([PCPs, OBGYNs, PCP30min, OBGYN30min, Hospital30min, Hospital30minOB,
                                          Hospital, AmbSurgical, Homehealth, Hospice, Birthing,  Midwives, Dialysis, Nursing,
                                           Treatment,FQHC,Other, Labor, Unemployed, Uninsured, Capita, Poverty, Kids, SNAP ])

    st.success(diagnosis)

if __name__ == '__main__':
    main()

