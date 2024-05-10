# Conversational QNA chatbot

import streamlit as st
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

# Streamlit UI
st.set_page_config(page_title='Conversational QNA chatbot')
st.header("Hey, Let's chat")

from constants import openai_key

chat_model = ChatOpenAI(temperature=0, openai_api_key=openai_key)

if 'flowmessages' not in st.session_state: # this is to make sure we dont have any messages then by default it will throw systemmessage 
    st.session_state['flowmessages'] = [SystemMessage(content='You are a comidian AI assistant')
]

def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question)) # to appened all the humanmessages
    answer = chat_model(st.session_state['flowmessages']) # to get the answer of all the flowmessages
    st.session_state['flowmessages'].append(AIMessage(content=answer.content)) # to appened all the AImessages
    return answer.content

input = st.text_input("Input:", key = "input")
response = get_chatmodel_response(input)

submit = st.button('Ask the question')

# if submit button is clicked

if submit:
    st.subheader('The resonse is')
    st.write(response)







