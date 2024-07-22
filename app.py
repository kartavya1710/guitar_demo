import streamlit as st
import google.generativeai as genai

# Configure API key outside of the conditional block
api_key = "AIzaSyBBQguUqfwXIH2GXeOx7ziJVVEw8DGj6II"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
st.image('guitar.jpg', width=400)
guitar_response = st.radio(
    "Have you ever played guitar before ?",
    ["Yes", "No"],
    index=None,
)

if guitar_response == "Yes":
    guitar_res = "I have Played guitar before in my life."
    level_response = st.radio(
    "What is your level ? ",
    ["Beginner", "Intermidiate","Expert"],
    index=None,
)
else:
    guitar_res = "I have never played guitar before."



hour_response = st.slider("How many hour in week could you dedicate to learn guitar : ", 1, 50, 10)

submit_button = st.button("submit")

if submit_button:
    
    try:
        user_prompt = f"{guitar_res}. And i am {level_response} at playing guitar. I can dedicate {hour_response} hours in week so give me 1 week plan to learn guitar accordingly."
    except:
        user_prompt = f"{guitar_res}. I can dedicate {hour_response} hours in week so give me 1 week plan to learn guitar accordingly."
    agent_prompt = f"""You are professional guitar artist.You need to curate a guitar learning path. Consider yourself as a master of guitar. 
    The user information is given below 
    
    user's information : {user_prompt}
    
    Task:
    Provide a precise path of what to do and the exact time to invest in each part or skill. There is no time constraint to complete the path in a certain number of months. Avoid specifying it in terms of weeks, but do include all the skills that need to be acquired.
    If user hasn't played guitar before then give path from scratch and make a path to scale up his skills or else if user has played guitar before then according to his level, give him path. 
        """

    response = model.generate_content(agent_prompt)
    st.write(response.text)
