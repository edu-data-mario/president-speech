import streamlit as st
import os

# https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    page_title="빨찌산큐알",
    page_icon="kr",
    initial_sidebar_state="collapsed",
    layout="centered",
    menu_items={
        'Get Help': 'https://github.com/edu-data-mario/president-speech',
        'Report a bug': "https://github.com/edu-data-mario/president-speech/issues",
        'About': """## 독립군가
```
신대한국 독립군의 백만 용사여
조국의 부르심을 네가 아느냐
삼천 리 삼천만의 우리 동포들
건질 이 너와 나로다

원수들이 강하다고 겁을 낼 건가?
우리들이 약하다고 낙심할 건가?
정의의 날쌘 칼이 비끼는 곳에
이길 이 너와 나로다

너 살거든 독립군의 용사가 되고
나 죽으면 독립군의 혼령이 됨이
동지여 너와 나의 소원 아니냐
빛낼 이 너와 나로다

압록강과 두만강을 뛰어 건너라
악독한 원수 무리 쓸어 몰아라
잃었던 조국 강산 회복하는 날
만세를 불러보세

나가! 나가! 싸우러 나가!
나가! 나가! 싸우러 나가!
독립문의 자유종이 울릴 때까지
싸우러 나가세!
```
"""
    }
)


def gen_img_full_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


with open(gen_img_full_path("hong.jpeg"), "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="hong.jpeg",
            mime="image/jpeg"
          )
