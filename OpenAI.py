import streamlit as st
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["api_key"]

st.title("나는 이미지 생성기 입니당당당")

# 입력 받는 곳
with st.form("form"):
    user_input = st.text_input("그리고 싶은 그림은?")
    size = st.selectbox("size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [
        {
            "role": "system",
            "content": "Imagine the detail appeareance of the input.Response it shortly around 15 words",
        }
    ]

    gpt_prompt.append({"role": "user", "content": user_input})

    client = OpenAI()
    with st.spinner("Waitting for ChatGPT ..."):
        gpt_response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=gpt_prompt
        )

    print(gpt_response.choices[0].message.content)

    dalle_prompt = gpt_response.choices[0].message.content

    # st.json(gpt_prompt)[1]['content']

    st.write("dall-e prompt: ", dalle_prompt)

    with st.spinner("Waitting ..."):
        dalle_response = client.images.generate(
            model="dall-e-2", prompt=dalle_prompt, size="1024x1024"
        )

        st.image(dalle_response.data[0].url)

st.button("클릭!!")


#####################################
# gpt_prompt = [{
#     'role': 'system', #'시스템'이라는 역할을 줌
#     'content':'Imagine the detail appeareance of the input.Response it shortly around 15 words', #입력 텍스트(영어로 해줘야 더 잘 됨)

# }]


# gpt_prompt.append(
#     {
#         'role': 'user', # '사용자'라는 역할을 줌
#         'content': user_input
#     }
# )
