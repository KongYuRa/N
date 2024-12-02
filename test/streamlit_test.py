# import streamlit as st
# from streamlit_chat import message
# from streamlit.components.v1 import html


# from langchain.chat_models import ChatOpenAI
# from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory

# import numpy as np

# import os
# import requests


# #모듈 가져오기
# import sys

# sys.path.append(os.path.dirname(os.path.abspath('https://github.com/AI-8th-11m/11m-jira/llm_chatbot/llm_module.git')))


# from llm_module.docs_utils import *
# from llm_module.db_utils import *
# from llm_module.script_utils import *
# from llm_module.llm_utils import *
# from llm_module.translator_module import translator



# import random
# import time

# json_files = [
#     "./llm_chatbot/documents/filtered_unsolved_cases.json",
#     "./llm_chatbot/documents/korea_crime.json",
# ]
# titles = title_json_data(json_files)
# sample_titles = titles[0:11]
# path = "./llm_chatbot/db/script_db"
# db_name = "script_db"
# script_db = load_vstore(db_name, path)
# LANG_CODE = False

# # 세션 관련 초기화
# if "history" not in st.session_state:
#     st.session_state.history = {}


# # 세팅 페이지 구현
# def setting_page():
#     st.title("유저 설정 화면")

#     # 세션 ID와 언어 설정
#     session_id = st.text_input("세션 ID를 입력하세요", placeholder="예: session123")
#     language = st.selectbox(
#         "사용할 언어를 선택하세요", options=["한국어", "English", "日本語"]
#     )

#     if st.button("저장 후 넘어가기"):
#         if session_id:
#             # 세션 정보 저장
#             st.session_state.session_id = session_id
#             st.session_state.language = language
#             st.session_state.current_session = session_id
#             st.session_state.LANG = (
#                 "korean" if language == "한국어" else language.lower()
#             )
#             st.session_state.history[session_id] = []  # 새로운 세션 초기화
#             # 세팅 완료 후 체크 페이지로 이동
#             st.session_state.page = "check"  # 체크 페이지로 이동
#             st.rerun()
#         else:
#             st.warning("세션 ID를 입력해주세요!")


# # 점수 구간 설정
# MIN_SCORE = 80
# MAX_SCORE = 85
# NEXT_SCORE = 95

# # 초기 점수 설정
# if "score" not in st.session_state:
#     st.session_state.score = 0


# # 체크 페이지 구현
# def check_page():
#     st.title("체크 페이지")
#     query = st.text_input("어떤 이야기가 듣고 싶으신가요?")

#     if query:
#         relavence = evaluator(query, script_db)
#         st.write(f"관련도 점수: {relavence[0]}")
#         st.session_state.score += relavence[0]

#         if relavence[0] < 80:
#             st.write("모르는 이야기입니다.")
#             st.write("종료 : exit, 다시 물어보기 : return, 생성하기 : create")

#             user_input = st.text_input("입력하세요.")
#             if user_input.lower() == "exit":
#                 st.session_state.page = "settings"  # 세팅 페이지로 이동
#                 st.rerun()
#             elif user_input.lower() == "return":
#                 st.session_state.page = "check"  # 체크 페이지로 돌아감
#                 st.rerun()
#             elif user_input.lower() == "create":
#                 st.session_state.page = "create"  # 생성 페이지로 이동
#                 st.rerun()

#         elif relavence[0] < 95 and relavence[0] >= 80:
#             st.write("더 자세히 이야기 해주세요.")
#             st.rerun()

#         elif relavence[0] >= 95:
#             script = relavence[1]
#             st.session_state.page = "chat"  # 채팅 페이지로 이동
#             st.session_state.query = query
#             st.session_state.script = script
#             st.rerun()


# # 생성 페이지 구현
# def create_page():
#     st.title("생성 페이지")
#     st.write("새로운 스크립트를 입력할 수 있습니다.")

#     text_input = st.text_area("URL 또는 텍스트를 입력해주세요.")
#     if text_input:
#         new_script = script_maker(text_input)
#         st.write(f"생성된 스크립트: {new_script}")
#         script_db = load_vstore("script_db", "./llm_chatbot/db/script_db")
#         add_to_vstore(new_script, script_db)

#     if st.button("돌아가기"):
#         st.session_state.page = "check"
#         st.rerun()


# # 채팅 페이지 구현
# # Streamlit 상태 관리 초기화
# if "page" not in st.session_state:
#     st.session_state.page = "settings"
# if "history" not in st.session_state:
#     st.session_state.history = {}  # 세션별 대화 기록 저장
# if "current_session" not in st.session_state:
#     st.session_state.current_session = None  # 현재 세션 ID

# # 페이지 전환 함수
# def go_to_chat():
#     st.session_state.page = "chat"

# def go_to_settings():
#     st.session_state.page = "settings"

# # 대화 기록 저장 함수
# def save_message(session_id, user_message, bot_message):
#     if session_id not in st.session_state.history:
#         st.session_state.history[session_id] = []  # 새로운 세션 초기화
#     st.session_state.history[session_id].append((user_message, bot_message))




# # 유저 설정 화면
# if st.session_state.page == "settings":
#     # 중앙 정렬
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         st.title("꼬꼬무")
#         st.subheader("사용자 정보 입력")

#         # 사용자 입력
#         session_id = st.text_input("세션 이름을 입력하세요", placeholder="예: session123")
#         language = st.selectbox("사용할 언어를 선택하세요", options=["한국어", "English", "日本語"])

#         # 버튼: 저장 후 넘어가기
#         if st.button("채팅 시작하기"):
#             if session_id:
#                 st.session_state.session_id = session_id
#                 st.session_state.language = language
#                 st.session_state.current_session = session_id
#                 st.session_state.history[session_id] = []  # 새로운 세션 초기화
#                 go_to_chat()
#             else:
#                 st.warning("세션 ID를 입력해주세요!")

# # 채팅 화면

# elif st.session_state.page == "chat":
#     # 사이드바: 세션 ID 선택
#     st.sidebar.title("세션 관리")
#     session_list = list(st.session_state.history.keys())
#     selected_session = st.sidebar.selectbox("저장된 세션 ID", options=["현재 세션"] + session_list)

#     if selected_session != "현재 세션":
#         st.session_state.current_session = selected_session

#     if "message" not in st.session_state:
#         st.session_state.messages = [{"role":"assistant","content":"채팅을 시작해주세요."}]


#     # 중앙 정렬
#     col1, col2, col3 = st.columns([1, 17, 1])
#     with col2:
#         # st.title("채팅 화면")

#         # 현재 세션 정보 표시
#         st.title("꼬꼬무")
#         st.write(
#     "미해결 사건에 대해 이야기를 하는 챗봇 입니다." 
#     "대화를 시작하고 싶으시다면, 채팅을 시작해주세요."
# )



#     #챗봇 만들기


# # Streamlit UI


# # # 채팅 입력창
# # if user_input := st.chat_input("Type your message here..."):
# #     # 모델 예측
# #     response = model.predict(user_input)

# #     # 응답 표시
# #     st.chat_message("user").markdown(user_input)
# #     st.chat_message("assistant").markdown(response)


# #------------

#         # session_state 초기화
#         st.session_state.setdefault('past', [])
#         st.session_state.setdefault('generated', [])

#         def on_input_change():
#             user_input = st.session_state.user_input
#             st.session_state.past.append(user_input)
#             st.session_state.generated.append("The messages from Bot\nWith new line")
#             st.session_state.user_input = ""  # 입력 후 텍스트 초기화

#         def on_btn_click():
#             del st.session_state.past[:]
#             del st.session_state.generated[:]


#         chat_placeholder = st.empty()

#         # 채팅 내역 표시
#         with chat_placeholder.container():    
#             for i in range(len(st.session_state['generated'])):                
#                 message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
#                 message(
#                     st.session_state['generated'][i], 
#                     key=f"{i}", 
#                     allow_html=True,
#                     is_table=False
#                 )

#                 # st.button("Clear message", on_click=on_btn_click)


#         # 채팅 입력란 최하단 고정 (채팅을 좌우로 나누는 코드 자체에 채팅 입력란이 채팅과 붙어있는 현상이 있어 최하단 고정이 안됨)
#         if user_input := st.chat_input("Type your message here..."):
#             st.session_state.past.append(user_input)
#             st.session_state.generated.append(f"{user_input}")




# if "page" not in st.session_state:
#     st.session_state.page = "settings"

# if st.session_state.page == "settings":
#     setting_page()
# elif st.session_state.page == "check":
#     check_page()
# elif st.session_state.page == "create":
#     create_page()
# elif st.session_state.page == "chat":
#     chat_page(st.session_state.script)








# #####Streamlit 




# #--------
#     # # 입력란을 위한 컨테이너

#     # with st.container():
#     #     st.text_input(
#     #         "User Input:", 
#     #         on_change=on_input_change, 
#     #         key="user_input", 
#     #         placeholder="Type your message here..."
#     #     )


# #모델 연결 시 사용
#     # if prompt := st.chat_input("메시지를 입력하세요."):
#     #     with st.chat_message("user"):
#     #             st.markdown(prompt)
#     #     st.session_state.chat_history.append({"role": "user", "message": prompt})
#     #     with st.chat_message("ai"):                
#     #         bot_response = f"챗봇 응답 예시 ({chat_bot},)"  # 실제 모델 연동 가능
#     #         save_message(st.session_state.current_session, prompt, bot_response)
#     #         # st.experimental_rerun()  # 화면 갱신



import streamlit as st

# 제목
st.title("🕸️꼬꼬무")
st.write(
    "미해결 사건에 대해 이야기를 하는 챗봇 입니다." 
    "대화를 시작하고 싶으시다면, 채팅을 시작해주세요."
)

#Streamlit 앱이 다시 로드될 때 상태를 유지하거나 초기화
if "user_name" not in st.session_state:
    st.session_state.user_name = "Guest"
name = st.text_input("Your Name:", st.session_state.user_name)
if st.button("Save Name"):
    st.session_state.user_name = name
st.write(f"Hello, {st.session_state.user_name}!")


#챗봇 만들기
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  

for content in st.session_state.chat_history:
    with st.chat_message(content["role"]):
        st.markdown(content['message'])    

if prompt := st.chat_input("메시지를 입력하세요."):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "message": prompt})

    with st.chat_message("ai"):                
        response = f'{prompt}...? 나는 아직 네가 하는 말 반복하는 것 밖에 못 해. 아직 구현이 안 됐거든. 조금만 기다려줘!'
        st.markdown(response)
        st.session_state.chat_history.append({"role": "ai", "message": response})


