import streamlit as st
import requests
import datetime

st.set_page_config(page_title="体重・体脂肪率データの取得", page_icon="⚖️")
st.title("⚖️ カロミルAPI：体重・体脂肪率の取得")

# アクセストークン取得（secretsから）
if "access_token" not in st.secrets:
    st.error("❌ st.secrets に access_token が登録されていません。")
    st.stop()

access_token = st.secrets["access_token"]

# 日付範囲を計算（過去7日分）
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).strftime("%Y/%m/%d")
end_date = today.strftime("%Y/%m/%d")

# ボタンでデータ取得
if st.button("📥 体重・体脂肪率データを取得"):
    url = f"https://test-connect.calomeal.com/api/anthropometric?start_date={start_date}&end_date={end_date}&unit=day"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    st.subheader("📊 レスポンス")
    st.text(f"ステータスコード: {response.status_code}")
    try:
        st.json(response.json())
    except Exception:
        st.write(response.text)
