import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# إعداد صفحة Streamlit
st.set_page_config(page_title="رحلة أعماق المحيط", layout="wide")

# --- العنوان ---
st.title("🌊 خريطة الألغام البحرية")
st.markdown("تتبعي المسار في أعماق البحر وتعرفي على أماكن الألغام! 💣")

# --- تحميل وعرض صورة الخريطة كخلفية ---
image_path = "map.png"  # تأكدي إن الصورة بنفس الاسم وفي نفس المجلد
image = Image.open(image_path)
st.image(image, use_column_width=True, caption="رحلة عبر أعماق المحيط 🐳")

# --- تحديد المواقع على الصورة (تمثيل افتراضي للمواقع) ---
locations = [
    {"name": "لغم 1", "x": 20, "y": 30},
    {"name": "لغم 2", "x": 45, "y": 50},
    {"name": "لغم 3", "x": 70, "y": 60},
]

# --- عرض المواقع باستخدام HTML مخصص مع CSS ---
st.markdown("### ⚠️ مواقع الألغام:")

# HTML لعرض صورة مع علامات Pin
pins_html = f"""
<div style="position: relative; width: 100%; max-width: 800px;">
  <img src="map.png" style="width: 100%;" />
"""

# إضافة كل نقطة كموقع Pin
for loc in locations:
    pins_html += f"""
    <div style="
        position: absolute;
        left: {loc['x']}%;
        top: {loc['y']}%;
        transform: translate(-50%, -50%);
        color: red;
        font-size: 24px;
        font-weight: bold;"
        title="{loc['name']}">📍</div>
    """

pins_html += "</div>"

# تضمين HTML داخل Streamlit
components.html(pins_html, height=600)

# زر بدء الرحلة
if st.button("🚀 ابدأ الرحلة"):
    st.success("🚨 الرحلة بدأت! راقبي الألغام وتقدمي بحذر...")

