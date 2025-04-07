import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="خريطة الألغام البحرية", layout="wide")

st.markdown("<h1 style='text-align: center;'>🌊 خريطة الألغام البحرية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>علامات تشير إلى أماكن الألغام في رحلة أعماق البحر</p>", unsafe_allow_html=True)

# بيانات العلامات
locations = [
    {"name": "لغم 1", "x": 18, "y": 30},
    {"name": "لغم 2", "x": 35, "y": 45},
    {"name": "لغم 3", "x": 52, "y": 55},
    {"name": "لغم 4", "x": 68, "y": 66},
]

# HTML
pins_html = """
<div style="position: relative; width: 100%; max-width: 1000px; margin: auto;">
  <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/map.png"
       style="width: 100%; height: auto; display: block; border-radius: 12px;" />
"""

# إضافة العلامات
for loc in locations:
    pins_html += f"""
    <div style="
        position: absolute;
        left: {loc['x']}%;
        top: {loc['y']}%;
        transform: translate(-50%, -100%);
        font-size: 28px;
        color: hotpink;"
        title="{loc['name']}">📍</div>
    """

pins_html += "</div>"

# عرض الكود داخل Streamlit
components.html(pins_html, height=700)

# زر التفاعل
if st.button("🚀 ابدأ المغامرة"):
    st.success("انطلقتِ في رحلتك نحو أعماق البحر! 🐚✨")
