import streamlit as st
import pandas  as pd

st.title("Chess")

wk_file = st.number_input("wk_file", min_value=1, max_value=3, step=1)
wk_rank = st.number_input("wk_rank", min_value=1, max_value=4, step=1)
wr_file = st.number_input("wr_file", min_value=1, max_value=7, step=1)
wr_rank = st.number_input("wr_rank", min_value=1, max_value=8, step=1)
bk_file = st.number_input("bk_file", min_value=1, max_value=7, step=1)
bk_rank = st.number_input("bk_rank", min_value=1, max_value=8, step=1)


dictionary = {
    "wk_file" : wk_file,
    "wk_rank" : wk_rank,
    "wr_file" : wr_file,
    "wr_rank" : wr_rank,
    "bk_file" : bk_file,
    "bk_rank" : bk_rank
}

data = pd.DataFrame(data=dictionary, index=[0])
st.dataframe(data)

if st.button("Model Run"):
    import pickle 
    model = pickle.load(open("../model/model.pkl", "rb"))
    st.write(F"The RESULT IS :- {model.predict(data.values)[0]}")