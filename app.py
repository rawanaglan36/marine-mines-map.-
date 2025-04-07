# import streamlit as st
# import folium
# from streamlit_folium import st_folium

# # بيانات المواقع
# locations = [
#     (24.7136, 46.6753),  # Riyadh
#     (21.4858, 39.1925),  # Jeddah
# ]

# # إعداد الخريطة
# m = folium.Map(location=locations[0], zoom_start=6)

# # إضافة نقاط
# for loc in locations:
#     folium.Marker(location=loc).add_to(m)

# # رسم خط يربط بينهم
# folium.PolyLine(locations, color='blue').add_to(m)

# # عرض على ستريملت
# st.title("رحلتي على الخريطة")
# st_folium(m, width=700, height=500)

import streamlit as st
import folium
from streamlit_folium import st_folium

# قائمة مواقع الألغام (مثال لمواقع وسط البحر)
mine_locations = [
    (25.0, 50.0),  # موقع 1
    (25.5, 50.5),  # موقع 2
    (26.0, 51.0),  # موقع 3
]

# إنشاء خريطة بطابع بحري
m = folium.Map(location=[25.5, 50.5], zoom_start=6, tiles="CartoDB dark_matter")

# إضافة الألغام كأيقونات مخصصة
for i, loc in enumerate(mine_locations, 1):
    folium.Marker(
        location=loc,
        icon=folium.Icon(icon="exclamation-sign", color="red"),  # شكل تحذير
        popup=f"لغم رقم {i}"
    ).add_to(m)

# إضافة خطوط لو حبيتي تمثلي مسار معين
folium.PolyLine(mine_locations, color='red', dash_array='5').add_to(m)

# عرض داخل Streamlit
st.title("مواقع الألغام البحرية 💣🌊")
st.markdown("خريطة تفاعلية توضح أماكن الألغام المكتشفة في البحر.")

# عرض الخريطة
st_folium(m, width=700, height=500)
