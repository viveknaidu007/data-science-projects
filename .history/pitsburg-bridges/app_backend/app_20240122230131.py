import streamlit as st
import pandas as pd

st.title("PitsBurgh-Bridges")


identifier = st.number_input("identifier", min_value=0, max_value=107, step=1)
river = st.number_input("river", min_value=0, max_value=3, step=1)
location = st.number_input("location", min_value=0, max_value=53, step=1)
erected_year = st.number_input("erected_year", min_value=0, max_value=69, step=1)
purpose = st.number_input("purpose", min_value=0, max_value=3, step=1)
length = st.number_input("length", min_value=0, max_value=64, step=1)
lanes = st.number_input("lanes", min_value=0, max_value=3, step=1)
clear_g = st.number_input("clear_g", min_value=0, max_value=1, step=1)
t_or_d = st.number_input("t_or_d", min_value=0, max_value=1, step=1)
material = st.number_input("material", min_value=0, max_value=2, step=1)
span = st.number_input("span", min_value=0, max_value=2, step=1)
rel = st.number_input("rel", min_value=0, max_value=2, step=1)


dictionary = {
    'identifier' : identifier, 'river': river, 'location': location, 'erected_year': erected_year, 'purpose': purpose, 'length': length,
       'lanes': lanes, 'clear-g': clear_g, 't-or-d': t_or_d, 'material': material, 'span': span, 'rel' : rel
}

data = pd.DataFrame(data=dictionary, index=[0])
st.dataframe(data)

if st.button("Model Run"):
    import pickle
    model = pickle.load(open("../model/model.pkl", "rb"))
    pred = model.predict(data)
    st.write(f"The Predicted Value is :- {pred[0]}")