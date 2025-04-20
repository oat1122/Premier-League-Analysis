import streamlit as st
import joblib
import numpy as np

# โหลดโมเดลที่ฝึกมาแล้ว
clf = joblib.load('./model/xg_modeltest.pkl')  # ไม่ต้องโหลด label encoder แล้ว

# ส่วนหัวของหน้าเว็บ
st.set_page_config(page_title="xG Football Predictor", page_icon="⚽")
st.title("⚽ Football Match Result Predictor")
st.markdown("ทำนายผลการแข่งขันจากค่า Expected Goals (xG) โดยใช้โมเดล Machine Learning")

# รับข้อมูลจากผู้ใช้
st.subheader("📥 ป้อนข้อมูลการแข่งขัน")

home_team = st.text_input("🏠 ชื่อทีมเหย้า", "")
away_team = st.text_input("🛫 ชื่อทีมเยือน", "")
home_xg = st.number_input("🔢 ค่า homeXG (โอกาสทำประตูเจ้าบ้าน)", min_value=0.0, step=0.1, format="%.2f")
away_xg = st.number_input("🔢 ค่า awayXG (โอกาสทำประตูทีมเยือน)", min_value=0.0, step=0.1, format="%.2f")

# เมปค่าที่คาดการณ์เป็นข้อความ
result_map = {
    'H': '🏠 ทีมเหย้าชนะ',
    'A': '🛫 ทีมเยือนชนะ',
    'D': '🤝 เสมอกัน'
}

# เมื่อผู้ใช้กดปุ่ม
if st.button("🔍 ทำนายผลการแข่งขัน"):
    if not home_team or not away_team:
        st.warning("⚠️ กรุณากรอกชื่อทีมให้ครบทั้งสองทีม")
    else:
        xg_diff = home_xg - away_xg
        input_data = np.array([[home_xg, away_xg, xg_diff]])
        prediction = clf.predict(input_data)
        result = prediction[0]  # ไม่ใช้ le.inverse_transform แล้ว
        result_text = result_map.get(result, "ผลลัพธ์ไม่ชัดเจน")

        st.success(f"🔮 ผลการแข่งขันระหว่าง **{home_team}** vs **{away_team}**")
        st.markdown(f"### 👉 ผลที่คาดการณ์: **{result_text}**")

        # เอฟเฟกต์แสดงผล
        if result == "H":
            st.balloons()
        elif result == "A":
            st.snow()
        else:
            st.info("เกมที่สูสีกันมาก! 🤝")
