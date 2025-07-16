import streamlit as st
import requests
import datetime
import json

st.set_page_config(page_title="体重データ取得", page_icon="⚖️")
st.title("⚖️ カロミルAPI：体重データ取得")

# アクセストークンの取得
if "access_token" not in st.secrets:
    st.error("❌ st.secrets に access_token が登録されていません。")
    st.stop()

access_token = st.secrets["access_token"]

# 取得範囲（直近7日間）
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).isoformat()
end_date = today.isoformat()

# ボタン押下で実行
if st.button("📥 体重データを取得"):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "from": start_date,
        "to": end_date
    }
    url = "https://test-connect.calomeal.com/api/anthropometric"

    response = requests.get(url, headers=headers, params=params)

    st.subheader("✅ レスポンス")
    st.text(f"ステータスコード: {response.status_code}")

    try:
        st.json(response.json())
    except Exception:
        st.write(response.text)
