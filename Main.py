import streamlit as st

st.title("First Website Created With Python")
st.header("Created by Aaron")

col1, col2 = st.columns(2)

with col1:
    st.subheader("User Info")
    name = st.text_input("Name: ")
    age = st.slider("How Old Are You? ", min_value = 10, max_value=100)
with col2:
    st.subheader("Preferences")
    colour = st.radio("What's your favourite colour? ", ("blue","green","red"))
    hours = st.number_input("how many hours do you study per day?", min_value = 0, max_value = 24)

st.markdown("---")
st.subheader("Summary")

if st.button("Submit"):
    if name:
        st.write(f"Hello {name}")
        st.write(f"You are {age} years old")
        st.write(f"Your favourite colour is {colour}")
        st.write(f"you study for {hours} hours")

if st.button("Encourage"):
    if hours > 5:
        st.success("Amazing Effort")
    elif hours > 2:
        st.warning("Nice work, but you can improve")
    else:
        st.error("Try to study more!!!")

st.caption("Made with Streamlit")