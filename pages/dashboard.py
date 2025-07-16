import streamlit as st
import requests
import datetime
from urllib.parse import urlencode

st.set_page_config(page_title="体重データ取得", page_icon="⚖️")
st.title("⚖️ カロミルAPI：体重・体脂肪率データ取得")

# アクセストークンの取得
if "access_token" not in st.secrets:
    st.error("❌ st.secrets に access_token が登録されていません。")
    st.stop()

access_token = st.secrets["access_token"]

# 取得範囲（直近7日間）
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).strftime("%Y/%m/%d")
end_date = today.strftime("%Y/%m/%d")

if st.button("📥 体重・体脂肪率データを取得"):
    url = "https://connect.calomeal.com/api/anthropometric"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "start_date": start_date,
        "end_date": end_date,
        "unit": "day"
    }

    encoded_data = urlencode(data)  # ← ここ重要！

    response = requests.post(url, headers=headers, data=encoded_data)

    st.subheader("✅ レスポンス")
    st.text(f"ステータスコード: {response.status_code}")

    try:
        st.json(response.json())
    except Exception:
        st.write(response.text)
