import streamlit as st
import requests
import datetime

st.set_page_config(page_title="体重データの取得テスト", page_icon="⚖️")
st.title("⚖️ カロミルAPI：体重データ取得（GET）")

# アクセストークンの取得
if "access_token" not in st.secrets:
    st.error("❌ st.secrets に access_token が登録されていません。")
    st.stop()

access_token = st.secrets["access_token"]

# 期間を設定（過去7日）
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).isoformat()
end_date = today.isoformat()

# データ取得ボタン
if st.button("📥 体重データを取得"):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    url = "https://test-connect.calomeal.com/api/anthropometric"
    params = {
        "start_date": start_date.replace("-", "/"),
        "end_date": end_date.replace("-", "/"),
        "unit": "day"
    }

    response = requests.get(url, headers=headers, params=params)

    st.subheader("✅ レスポンス")
    st.text(f"ステータスコード: {response.status_code}")
    try:
        st.json(response.json())
    except Exception:
        st.write(response.text)
