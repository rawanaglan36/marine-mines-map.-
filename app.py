# import streamlit as st
# import streamlit.components.v1 as components

# # إعداد الصفحة
# st.set_page_config(page_title="خريطة الألغام البحرية", layout="wide")

# # إخفاء عناصر Streamlit الافتراضية
# hide_st_style = """
#     <style>
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
#     </style>
# """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# # صورة الخلفية
# background_url = "https://i.imgur.com/bam6oj8.png"

# # بيانات الألغام
# locations = [
#     {"name": "لغم 1", "x": 23, "y": 45},
#     {"name": "لغم 2", "x": 38, "y": 60},
#     {"name": "لغم 3", "x": 58, "y": 65},
#     {"name": "لغم 4", "x": 72, "y": 50},
# ]

# # HTML
# html_code = f"""
# <div style="
#     position: relative;
#     width: 100vw;
#     height: 100vh;
#     background-image: url('{background_url}');
#     background-size: cover;
#     background-position: center;
#     overflow: hidden;
# ">

#     <!-- عنوان -->
#     <div style="
#         text-align: center;
#         color: white;
#         padding-top: 30px;
#         font-size: 38px;
#         font-weight: bold;
#         text-shadow: 2px 2px 8px #000;
#     ">🌊 خريطة الألغام البحرية</div>

#     <div style="
#         text-align: center;
#         color: white;
#         margin-top: 5px;
#         font-size: 20px;
#         text-shadow: 1px 1px 4px #000;
#     ">علامات تشير إلى أماكن الألغام في رحلة أعماق البحر</div>

#     <!-- خريطة SVG -->
#     <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0;">
# """

# # إضافة خطوط بين النقاط
# for i in range(len(locations) - 1):
#     x1 = locations[i]['x']
#     y1 = locations[i]['y']
#     x2 = locations[i+1]['x']
#     y2 = locations[i+1]['y']
#     html_code += f"""
#     <line x1="{x1}%" y1="{y1}%" x2="{x2}%" y2="{y2}%" 
#           stroke="aqua" stroke-width="3" stroke-dasharray="8,6"
#           style="filter: drop-shadow(2px 2px 2px #000);" />
#     """

# html_code += "</svg>"

# # إضافة علامات اللغم
# for loc in locations:
#     html_code += f"""
#     <div title="{loc['name']}" style="
#         position: absolute;
#         left: {loc['x']}%;
#         top: {loc['y']}%;
#         transform: translate(-50%, -100%);
#         font-size: 45px;
#         color: deeppink;
#         filter: drop-shadow(2px 2px 4px black);
#     ">📍</div>
#     """

# html_code += "</div>"

# # عرض داخل Streamlit
# components.html(html_code, height=800)

# # زر المغامرة
# if st.button("🚀 ابدأ المغامرة"):
#     st.success("✨ بالتوفيق في رحلتك نحو أعماق البحر! 🌊")


import streamlit as st
from PIL import Image
import base64
import time

st.set_page_config(layout="wide")

# إعداد الصورة الخلفية مع تغطية كاملة
page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64.b64encode(open("https://i.imgur.com/bam6oj8.png", "rb").read()).decode()}" );
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .title-text {{
        position: absolute;
        top: 30px;
        left: 50%;
        transform: translateX(-50%);
        color: white;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        z-index: 10;
        text-shadow: 2px 2px 5px #000;
    }}
    .fade-in {{
        animation: fadeIn 2s ease-in forwards;
        opacity: 0;
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    .bottom-button {{
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 20;
        text-align: center;
    }}
    .bottom-button button {{
        font-size: 20px;
        padding: 10px 24px;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 8px;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
        cursor: pointer;
    }}
    .bottom-button button:hover {{
        background-color: #0056b3;
    }}
    </style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# العنوان الرئيسي فقط
st.markdown('<div class="title-text">MARINE MINES MAP</div>', unsafe_allow_html=True)

# زر إظهار المسار
button_html = """
<div class="bottom-button">
    <form action="" method="post">
        <button type="submit">🚀 Start Adventure</button>
    </form>
</div>
"""

show_path = st.button("🚀 Start Adventure")
st.markdown(button_html, unsafe_allow_html=True)

# عرض المسار فقط عند الضغط على الزر، مع تأثير تدريجي
if show_path:
    with st.container():
        time.sleep(0.3)
        st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
        st.image("/mnt/data/with_path_and_pins.png", use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.image("/mnt/data/map_cleaned.png", use_column_width=True)
