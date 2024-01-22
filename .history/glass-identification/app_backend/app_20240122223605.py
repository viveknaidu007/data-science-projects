import streamlit as st

st.title("Glass-Identification")


id = st.number_input("id")
ri = st.number_input("ri")
Na = st.number_input("Na")
Al = st.number_input("Al")
Si = st.number_input("Si")
K = st.number_input("K")
Ca = st.number_input("Ca")
Ba = st.number_input("Ba")
Fe = st.number_input("Fe")


dictionary = {
    'id' : id, 'ri' : ri, 'Na' : Na, 'Al' : Al, 
    'Si' : Si, 'K' : K, 'Ca' : Ca, 'Ba' : Ba, 'Fe' : Fe
}

import pandas as pd

data = pd.DataFrame(data=dictionary, index=[0])
st.dataframe(data)

if st.button("Model Run"):
    import pickle
    model = pickle.load(open("../model/model.pkl", "rb"))

    st.write(f"The Model Predicted Value is :- {model.predict(data)[0]}")