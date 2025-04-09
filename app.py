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
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="خريطة الألغام البحرية", layout="wide")

# إخفاء عناصر Streamlit الافتراضية
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# صورة الخلفية
background_url = "https://i.imgur.com/9dPTUrb.jpeg"

# بيانات الألغام
locations = [
    {"name": "لغم 1", "x": 23, "y": 45},
    {"name": "لغم 2", "x": 38, "y": 60},
    {"name": "لغم 3", "x": 58, "y": 65},
    {"name": "لغم 4", "x": 72, "y": 50},
]

# زر المغامرة
show_path = st.button("🚀 ابدأ المغامرة")

# HTML الأساسي
html_code = f"""
<div style="
    position: relative;
    width: 100vw;
    height: 100vh;
    background-image: url('{background_url}');
    background-size: cover;
    background-position: center;
    overflow: hidden;
">

    <!-- عنوان -->
    <div style="
        text-align: center;
        color: white;
        padding-top: 30px;
        font-size: 38px;
        font-weight: bold;
        text-shadow: 2px 2px 8px #000;
    ">🌊 خريطة الألغام البحرية</div>

    <div style="
        text-align: center;
        color: white;
        margin-top: 5px;
        font-size: 20px;
        text-shadow: 1px 1px 4px #000;
    ">علامات تشير إلى أماكن الألغام في رحلة أعماق البحر</div>

    <!-- SVG للمسار والعلامات -->
    <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0;">
"""

# إذا تم الضغط على الزر، أضف الخطوط والعلامات بتأثير تدريجي
if show_path:
    html_code += "<style> .fadein {{ animation: fadein 2s ease-in forwards; opacity: 0; }} @keyframes fadein {{ from {{opacity: 0;}} to {{opacity: 1;}} }} </style>"
    html_code += "<g class='fadein'>"

    for i in range(len(locations) - 1):
        x1 = locations[i]['x']
        y1 = locations[i]['y']
        x2 = locations[i+1]['x']
        y2 = locations[i+1]['y']
        html_code += f"""
        <line x1="{x1}%" y1="{y1}%" x2="{x2}%" y2="{y2}%" 
              stroke="aqua" stroke-width="3" stroke-dasharray="8,6"
              style="filter: drop-shadow(2px 2px 2px #000);" />
        """

    html_code += "</g></svg>"

    # إضافة العلامات بعد SVG
    for loc in locations:
        html_code += f"""
        <div title="{loc['name']}" class='fadein' style="
            position: absolute;
            left: {loc['x']}%;
            top: {loc['y']}%;
            transform: translate(-50%, -100%);
            font-size: 45px;
            color: deeppink;
            filter: drop-shadow(2px 2px 4px black);
        ">📍</div>
        """

else:
    html_code += "</svg>"

html_code += "</div>"

# عرض داخل Streamlit
components.html(html_code, height=800)
