import streamlit as st
import google.generativeai as genai

# Configure API key outside of the conditional block
api_key = "AIzaSyBBQguUqfwXIH2GXeOx7ziJVVEw8DGj6II"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

guitar_response = st.radio(
    "Have you ever played guitar before ?",
    ["Yes", "No"],
    index=None,
)

if guitar_response == "yes":
    guitar_res = "I have Played guitar before in my life."
else:
    guitar_res = "I have never played guitar before."

level_response = st.radio(
    "What is your level ? ",
    ["Beginner", "Intermidiate","Expert"],
    index=None,
)

hour_response = st.slider("How many hour in week could you dedicate to learn guitar : ", 1, 50, 10)

submit_button = st.button("submit")

if submit_button:
    user_prompt = f"{guitar_res}. And my i am {level_response}. I can dedicate {hour_response} hours in week so give me 1 week plan to learn guitar accordingly."
    agent_prompt = f"""You are professional guitar artist.You need to curate a guitar learning path. Consider yourself as a master of guitar. 
    The user information is given below 
    
    user's information : {user_prompt}
    
    Task:
    Provide a precise path of what to do and the exact time to invest in each part or skill. There is no time constraint to complete the path in a certain number of months. Avoid specifying it in terms of weeks, but do include all the skills that need to be acquired.
        """

    response = model.generate_content(agent_prompt)
    st.write(response.text)