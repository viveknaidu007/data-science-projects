import streamlit as st
import pandas as pd

st.title("Abalano dataset")

length = st.number_input("length")
diameter = st.number_input("diameter")
height = st.number_input("height")
whole_weight = st.number_input("whole_weight")
shucked_weight = st.number_input("shucked_weight")
viscera_weight = st.number_input("viscera_weight")
shell_weight = st.number_input("shell weight")
rings = st.number_input("rings")

dictionary = {
'length' : length,
'diameter' : diameter,
'height' : height,
'whole_weight' : whole_weight,
'shucked_weight' : shucked_weight,
'viscera_weight' : viscera_weight,
'shell_weight' : shell_weight,
'rings' : rings
}
data = pd.DataFrame(data=dictionary, index=[0])
st.dataframe(data)


if st.button("Model run"):
    import pickle
    model = pickle.load(open("../model/model.pkl", "rb"))
    st.write(f"The ouput of the Model :- {model.predict(data.values)[0]}")