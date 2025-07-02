import streamlit as st
import requests
import json
import os

st.title("ナディ式ダッシュボード - 体重データ取得")

# トークンの読み込み
if not os.path.exists("token.json"):
    st.error("❌ トークンが存在しません。先に認証を完了してください。")
    st.stop()

with open("token.json", "r") as f:
    tokens = json.load(f)

access_token = tokens.get("access_token")

# ヘッダー設定
headers = {
    "Authorization": f"Bearer {access_token}"
}

# APIエンドポイント
weight_url = "https://test-connect.calomeal.com/api/v2/anthropometric"

if st.button("📊 体重データを取得"):
    res = requests.get(weight_url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        st.success("✅ データ取得成功！")
        st.json(data)
    else:
        st.error(f"❌ データ取得失敗（status: {res.status_code}）")
        st.json(res.json())
