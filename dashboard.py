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

# 期間を設定（例：過去7日分）
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).isoformat()
end_date = today.isoformat()

# データ取得ボタン
if st.button("📥 体重データを取得"):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # 正しい体重取得エンドポイント（URL確認済）
    url = "https://test-connect.calomeal.com/api/v2/anthropometric"
    params = {
        "from": start_date,
        "to": end_date
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        weight_data = response.json()
        st.success("✅ 体重データの取得に成功しました！")
        st.json(weight_data)
    else:
        st.error("❌ データ取得に失敗しました")
        st.text(f"status: {response.status_code}")
        st.write(response.text)
