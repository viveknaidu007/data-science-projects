import streamlit as st


st.title("Communities-Crime")

PctIlleg = st.number_input("PctIlleg", min_value=1, max_value=100, step=1)
PctKids2Par = st.number_input("PctKids2Par", min_value=1, max_value=100, step=1)
racePctWhite = st.number_input("racePctWhite", min_value=1, max_value=100, step=1)
PctFam2Par = st.number_input("PctFam2Par", min_value=1, max_value=100, step=1)


dictionary = {
    'PctIlleg' : PctIlleg, 'PctKids2Par' : PctKids2Par, 
    'racePctWhite' : racePctWhite, 'PctFam2Par' : PctFam2Par
}


import pandas as pd

data = pd.DataFrame(data=dictionary, index=[0])
st.dataframe(data)
if st.button("Run Model"):
    import pickle
    model = pickle.load(open("../model/model.pkl", "rb"))
    st.write(f"The Model Predited is :- {model.predict(data)[0]}")