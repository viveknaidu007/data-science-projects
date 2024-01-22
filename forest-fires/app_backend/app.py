import streamlit as st


st.title("Forest-Fires")


X = st.number_input("X", min_value=1, max_value=100, step=1)
Y = st.number_input("Y", min_value=1, max_value=100, step=1)
FFMC = st.number_input("FFMC")
DMC = st.number_input("DMC")
DC = st.number_input("DC") 
ISI = st.number_input("ISI")
temp = st.number_input("TEMP") 
RH = st.number_input("RH", min_value=1, max_value=100, step=1)
wind = st.number_input("WIND")
rain = st.number_input("RAIN")

dictionary = {
    'X' : X, 'Y' : Y, 'FFMC' : FFMC, 'DMC' :DMC, 'DC':DC, 'ISI':ISI, 'temp':temp, 'RH':RH,
       'wind':wind, 'rain':rain
}

import pandas as pd
data = pd.DataFrame(data=dictionary, index=[0])
st.dataframe(data)

if st.button("Model Run"):
    import pickle
    model = pickle.load(open("../model/model.pkl", "rb"))
    st.write(f"The Predicted Value is : {model.predict(data)[0]}")