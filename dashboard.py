import streamlit as st
import requests
import json
import os
import datetime

st.set_page_config(page_title="カロミル体重データの取得", page_icon="📊")
st.title("📊 カロミル体重データの取得")

# アクセストークンの読み込み
token_file = "token.json"
if not os.path.exists(token_file):
    st.error("❌ アクセストークンが保存されていません。まず認証を完了してください。")
    st.stop()

with open(token_file, "r") as f:
    token_data = json.load(f)

access_token = token_data.get("access_token")

# 期間を設定（過去7日分）
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).isoformat()
end_date = today.isoformat()

# データ取得ボタン
if st.button("📥 体重データを取得"):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # POST送信するformデータ（YYYY/MM/DD形式で送信）
    payload = {
        "start_date": start_date.replace("-", "/"),
        "end_date": end_date.replace("-", "/"),
        "unit": "day"
    }

    # 正しいエンドポイント
    url = "https://test-connect.calomeal.com/api/anthropometric"

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        weight_data = response.json()
        st.success("✅ 体重データの取得に成功しました！")
        st.json(weight_data)
    else:
        st.error("❌ データ取得に失敗しました")
        st.text(f"status: {response.status_code}")
        st.write(response.text)
