import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="خريطة أعماق المحيط", layout="wide")

st.markdown("<h1 style='text-align: center;'>🌊 خريطة الألغام البحرية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>علامات تشير إلى أماكن الألغام في رحلة أعماق البحر</p>", unsafe_allow_html=True)

# خريطة تفاعلية داخل صورة
locations = [
    {"name": "لغم 1", "x": 18, "y": 30},
    {"name": "لغم 2", "x": 40, "y": 45},
    {"name": "لغم 3", "x": 63, "y": 55},
    {"name": "لغم 4", "x": 80, "y": 70},
]

# HTML لعرض الصورة مع العلامات
pins_html = """
<div style="position: relative; width: 100%; max-width: 800px; margin: auto;">
  <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/map.png" style="width: 100%; border-radius: 12px;" />
"""

# إضافة العلامات على الصورة
for loc in locations:
    pins_html += f"""
    <div style="
        position: absolute;
        left: {loc['x']}%;
        top: {loc['y']}%;
        transform: translate(-50%, -50%);
        font-size: 24px;
        color: red;"
        title="{loc['name']}">📍</div>
    """

pins_html += "</div>"

# عرض الـ HTML
components.html(pins_html, height=600)

# زر تفاعلي
if st.button("🚀 ابدأ المغامرة"):
    st.success("انطلقتِ في رحلتك نحو أعماق المحيط! احذري الألغام!")

