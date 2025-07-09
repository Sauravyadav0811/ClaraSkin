import streamlit as st
from agent.beauty_agent import agent

st.set_page_config(page_title="ClaraSkin ", layout="centered")
st.title("💄 ClaraSkin – AI Skincare Assistant")

# User input fields
skin_type = st.selectbox("Select your skin type:", ["Oily", "Dry", "Sensitive", "Combination"])
concern = st.text_input("What is your skincare concern?", placeholder="e.g., acne, pigmentation")
budget = st.slider("Choose your budget (INR)", min_value=100, max_value=2000, value=1000)


# Handle form submission
if st.button("Get My Routine"):
    if not concern:
        st.warning("Please enter a skincare concern.")
    else:
        query = f"{skin_type} skin routine for {concern} under ₹{budget}"
        st.write("🤖 ClaraSkin is preparing your routine...")
        with st.spinner("💬 ClaraSkin is thinking..."):
            response = agent.run(query)
            st.success("Here's your personalized routine:")
            st.markdown(response)