import streamlit as st
import os
import segno
import qrcode
from datetime import datetime
from PIL import Image
import streamlit as st
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask



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

st.title("🇰🇷 partisan QR Code Gen 🇰🇷")


def gen_img_full_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), file_name)


generated_qrcodes_path = gen_img_full_path("generated_qrcodes") + "/"


def generate_qrcode(url: str):
    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=2
                        )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=HorizontalGradiantColorMask())

    current_ts = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    qrcode_path = generated_qrcodes_path + "qrcode_" + str(current_ts) + ".png"
    img.save(qrcode_path)
    return qrcode_path


main_image = Image.open(gen_img_full_path("hong.jpeg"))
st.image(main_image, use_column_width='auto', caption="특별기를 통해 2021년 8월 15일 서울공항에 도착한 홍범도 장군의 유해가 하기 되고 있다. 항일 무장투쟁을 펼쳤던 홍범도 장군(1868~1943)이 광복절인 15일 태극기와 함께 귀환했다. 홍범도 장군의 유해 봉환은 사망 연도 기준 78년만이자, 봉오동ㆍ청산리 전투(1920년) 승리 이후 101년 만이다.")

url = st.text_input("Enter your URL please 👇")

if url is not None and url != "":
    with st.spinner(f"Generating QR Code... 💫"):
        qrcode_path = generate_qrcode(str(url))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        image = Image.open(qrcode_path)
        st.image(image, caption='Here\'s the Generated QR Code ✅')

    with col3:
        with open(qrcode_path, "rb") as file:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name="myqr.png",
                mime="image/png"
            )
else:
    st.warning('⚠ Please enter your URL! 😯')


st.markdown("""
<br>
<hr>
<center>
    Made with 🇰🇷 by 
    <a href='mailto:data.mario24@gmail.com?subject=Inquiries about QR code generators as descendants of the Independent Army'>
        <strong>dMario24</strong>
    </a>
</center><hr>""", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
