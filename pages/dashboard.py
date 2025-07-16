import streamlit as st
import requests
import datetime

st.set_page_config(page_title="体重データの取得", page_icon="📊")
st.title("📊 カロミルAPI：体重・体脂肪率データ取得")

# アクセストークンを secrets から取得
if "access_token" not in st.secrets:
    st.error("❌ st.secrets に access_token がありません。")
    st.stop()

access_token = st.secrets["access_token"]

# 日付範囲の設定
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).strftime("%Y/%m/%d")
end_date = today.strftime("%Y/%m/%d")

if st.button("▶️ 体重データを取得"):
    url = "https://test-connect.calomeal.com/api/anthropometric"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # ✅ GETのパラメータは "params" に渡す（重要！）
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "unit": "day"
    }

    response = requests.get(url, headers=headers, params=params)

    st.subheader("✅ レスポンス")
    st.text(f"ステータスコード: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        if data:
            st.json(data)
        else:
            st.warning("⚠️ 取得期間中に体重データが入力されていません。")
    else:
        st.error("❌ データ取得に失敗しました")
        st.write(response.text)
