import streamlit as st
st.title("First Streamlit App")
st.write("welcome you for the first time")

name = st.text_input("Enter your name:")
if st.button("Say Hello"):
    st.write(f"Hello {name}, nice to meet you!")
if st.button("Say Bye"):
    st.write(f"Bye-Bye {name}")


