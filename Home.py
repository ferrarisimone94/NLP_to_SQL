import streamlit as st
import openai
import os
#import requests

# Set your OpenAI API key here
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets["OPENAI_API_KEY"]
# Function to interact with the GPT-3.5-turbo model with tunable parameters
def generate_response(prompt, temperature=0.7, max_tokens=256, top_p=0.9, n=2, stop=None, frequency_penalty=0.9, presence_penalty=0.9, chat_history=None):
    if chat_history is None:
        chat_history = []

    messages = [
       {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]
    messages.extend(chat_history)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        n=2,
        stop="None",
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['message']['content']

st.write("NLP to SQL!")


# Sidebar with social profiles and model parameters
st.sidebar.markdown("Check my profiles:")
st.sidebar.markdown(
    """<a href="https://github.com/ferrarisimone94/NLP_to_SQL/edit/main/Home.py"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="60px"></a>
    <a href="https://www.linkedin.com/in/simonepaoloferrari/" target="_blank"><img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="LinkedIn" width="60px"></a>
   """,
    unsafe_allow_html=True,
)

# HTML sidebar to fine-tune model's parameters to customize the bot's responses.
#st.sidebar.markdown("# Model Parameters")
#temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
#max_tokens = st.sidebar.number_input("Max Tokens", 50, 500, 256, step=50)
#top_p = st.sidebar.slider("Top P", 0.1, 1.0, 0.9, 0.1)
#n = st.sidebar.number_input("N", 1, 5, 2, step=1)
#stop = st.sidebar.text_input("Stop", "")
#frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 1.0, 0.9, 0.1)
#presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 1.0, 0.9, 0.1)

# Main app where user enters prompt and gets the response
user_input = st.text_area("You:", "", key="user_input")
generate_button = st.button("Generate Response")

# Chat history
messages = []
if user_input.strip() != "":
    messages.append({"role": "user", "content": user_input})
    response = generate_response(user_input, temperature, max_tokens, top_p, n, stop, frequency_penalty, presence_penalty)
    messages.append({"role": "assistant", "content": response})

#TAKEN FROM SNOWFLAKE
#response = openai.chat.completions.create(
#        model = "gpt-3.5-turbo"
#        , messages = [
#        {"role": "system",
#        "content": "I have a table called fruit in the database sf_llm. No need to mention the database in the SQL. The table has 2 columns. The first is called fruit_id and the second is called fruit_name. The column fruit_id contains integers, the column fruit_name contain text.fruit_id is integer that you can pick randomly between 1 to 1000."},
#        {"role": "user",
#        "content": prompt}
#        ])
#    return response.choices[0].message.content

st.subheader("Chat History")
for message in messages:
    if message["role"] == "user":
        st.text_area("You:", value=message["content"], height=50, max_chars=200, key="user_history", disabled=True)
    else:
        st.text_area("Jarvis:", value=message["content"], height=500, key="chatbot_history")

# Additional styling to make the app visually appealing
st.markdown(
    """
    <style>
        body {
            font-family: Montserrat, sans-serif;
        }
        .stTextInput>div>div>textarea {
            background-color: #f0f0f0;
            color: #000;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        .stTextArea>div>textarea {
            resize: none;
        }
        .st-subheader {
            margin-top: 20px;
            font-size: 16px;
        }
        .stTextArea>div>div>textarea {
            height: 100px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
