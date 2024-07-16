import streamlit as st
from openai import OpenAI
import time

# 코드스니펫 - 제목
st.title('[스파르타] 제품 홍보 포스터 생성기')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")

client = OpenAI(api_key=st.secrets["API_KEY"])

# 코드스니펫 - 버튼
if st.button('생성 :fire:'):
    with st.spinner('생성 중입니다.'):
        time.sleep(3)
        chat_completion = client.chat.completions.create(
          messages=[{
              "role": "user",
              "content": keyword,
          }],
          model="gpt-4o",
        )
        chat_result = chat_completion.choices[0].message.content
        st.write(chat_result)




