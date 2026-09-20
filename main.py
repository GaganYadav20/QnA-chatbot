from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st



llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# while True:
#     query=input("User : ")
#     if query.lower() in ["exit","bye","stop"]:
#         print("Good Bye 👋")
#         break
#     response = model.invoke(query)
#     print("AI : ",response.text)


st.title("🤖 AskBuddy - AI QnA Chatbot")
st.markdown("My QnA Bot with langchain and Google Gemini !")

if "messages" not in st.session_state:
    st.session_state.messages=[]
    
for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)

query=st.chat_input("Ask anything ?")

if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    st.chat_message("ai").markdown(res.text)
    st.session_state.messages.append({"role":"ai","content":res.text})
    