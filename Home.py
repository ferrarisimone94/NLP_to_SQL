import streamlit as st
import openai
import os
#import requests

# Set your OpenAI API key here
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Sidebar with social profiles and model parameters
st.sidebar.markdown("Check my profiles:")
st.sidebar.markdown(
    """<a href="https://github.com/ferrarisimone94/NLP_to_SQL/edit/main/Home.py"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="60px"></a>
    <a href="https://www.linkedin.com/in/simonepaoloferrari/" target="_blank"><img src="https://cdn1.iconfinder.com/data/icons/logotypes/32/circle-linkedin-512.png" alt="LinkedIn" width="60px"></a>
   """,
    unsafe_allow_html=True,
)

# Function to interact with the GPT-3.5-turbo model with tunable parameters
def generate_response(prompt):
    #def generate_response(prompt, temperature, max_tokens, top_p, n, stop, frequency_penalty, presence_penalty, chat_history):
    #if chat_history is None:
    #    chat_history = []
    messages = [
       #{"role": "system", "content": "You are a Public Company Accounting Oversight Board (PCAOB) inspector. Here the rules: AS 1001: Responsibilities and Functions of the Independent Auditor. Distinction Between Responsibilities of Auditor and Management includes:  .02 The auditor has a responsibility to plan and perform the audit to obtain reasonable assurance about whether the financial statements are free of material misstatement, whether caused by error or fraud.1 Because of the nature of audit evidence and the characteristics of fraud, the auditor is able to obtain reasonable, but not absolute, assurance that material misstatements are detected.2 The auditor has no responsibility to plan and perform the audit to obtain reasonable assurance that misstatements, whether caused by errors or fraud, that are not material to the financial statements are detected. .03 The financial statements are management's responsibility. The auditor's responsibility is to express an opinion on the financial statements. Management is responsible for adopting sound accounting policies and for establishing and maintaining internal control that will, among other things, initiate, record, process, and report transactions (as well as events and conditions) consistent with management's assertions embodied in the financial statements. The entity's transactions and the related assets, liabilities, and equity are within the direct knowledge and control of management. The auditor's knowledge of these matters and internal control is limited to that acquired through the audit. Thus, the fair presentation of financial statements in conformity with generally accepted accounting principles3 is an implicit and integral part of management's responsibility. The independent auditor may make suggestions about the form or content of the financial statements or draft them, in whole or in part, based on information from management during the performance of the audit. However, the auditor's responsibility for the financial statements he or she has audited is confined to the expression of his or her opinion on them. Professional Qualifications includes: .04 The professional qualifications required of the independent auditor are those of a person with the education and experience to practice as such. They do not include those of a person trained for or qualified to engage in another profession or occupation. For example, the independent auditor, in observing the taking of a physical inventory, does not purport to act as an appraiser, a valuer, or an expert in materials. Similarly, although the independent auditor is informed in a general manner about matters of commercial law, he does not purport to act in the capacity of a lawyer and may appropriately rely upon the advice of attorneys in all matters of law. .05 In the observance of the standards of the PCAOB, the independent auditor must exercise his judgmentHis judgment is required to be the informed judgment of a qualified professional person. Detection of Fraud includes: .06 - .09 Paragraphs deleted. Responsibility to the Profession include: .10 Paragraph deleted. .11 The auditor should be aware of and consider auditing interpretations applicable to his or her audit. If the auditor does not apply the auditing guidance included in an applicable auditing interpretation, the auditor should be prepared to explain how he or she complied with the provisions of the auditing standard addressed by such auditing guidance.  in determining which auditing procedures are necessary in the circumstances to afford a reasonable basis for his opinion."},
        {"role": "system", "content": ""},
        {"role": "user", "content": prompt},
    ]
    #messages.extend(chat_history)
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
    return response.choices[0].message.content

st.write("NLP to SQL!")

# Main app where user enters prompt and gets the response
user_input = st.text_area("")
input_button = st.button("Ask")

if input_button:
    st.write("Assistant:")
    st.write(generate_response(user_input))

# HTML sidebar to fine-tune model's parameters to customize the bot's responses.
#st.sidebar.markdown("# Model Parameters")
#temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
#max_tokens = st.sidebar.number_input("Max Tokens", 50, 500, 256, step=50)
#top_p = st.sidebar.slider("Top P", 0.1, 1.0, 0.9, 0.1)
#n = st.sidebar.number_input("N", 1, 5, 2, step=1)
#stop = st.sidebar.text_input("Stop", "")
#frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 1.0, 0.9, 0.1)
#presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 1.0, 0.9, 0.1)

# Chat history
#messages = []
#if user_input.strip() != "":
#    messages.append({"role": "user", "content": user_input})
#    response = generate_response(user_input, temperature, max_tokens, top_p, n, stop, frequency_penalty, presence_penalty)
#    messages.append({"role": "assistant", "content": response})

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

#st.subheader("Chat History")
#for message in messages:
#    if message["role"] == "user":
#        st.text_area("You:", value=message["content"], height=50, max_chars=200, key="user_history", disabled=True)
#    else:
#        st.text_area("Jarvis:", value=message["content"], height=500, key="chatbot_history")
