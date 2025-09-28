from dotenv import load_dotenv
load_dotenv()


import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
#操作方法をユーザーに明示するためのテキスト
st.title("医薬品情報検索")
st.write("質問の種類を選択し、一般名・販売名（医薬品の名称）の名称を入力してください。")

#入力テキストボックスとラジオボタンでの選択肢の作成
option = st.radio(
    "質問の種類を選んでください",
    ('薬の薬効・作用の一般情報', 'その成分を含む製剤の製造企業に関する情報'))  

user_input = st.text_input("質問を入力してください", "")
if user_input:
    if option == '薬の薬効・作用の一般情報':
        messages = [
            SystemMessage(content="あなたは薬の薬効に詳しい専門家です。作用機構や効能、副作用について詳しく説明してください。"),
            HumanMessage(content=user_input)
        ]
        result = llm.invoke(messages) 
        st.write(result.content)
    elif option == 'その成分を含む製剤の製造企業に関する情報':
        messages = [
            SystemMessage(content="あなたは製薬会社に詳しい専門家です。入力された製剤を製造している製薬会社を列記し、しく説明してください。"),
            HumanMessage(content=user_input)
        ]
        result = llm.invoke(messages) 
        st.write(result.content)

