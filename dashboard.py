import streamlit as st
import requests
import json
import os

st.set_page_config(page_title="カロミル体重データの取得", page_icon="📊")

st.title("📊 カロミル体重データの取得")

# アクセストークンの読み込み
token_file = "token.json"
if not os.path.exists(token_file):
    st.error("❌ アクセストークンが保存されていません。認証からやり直してください。")
    st.stop()

with open(token_file, "r") as f:
    token_data = json.load(f)

access_token = token_data.get("access_token")

# ボタンでデータ取得を実行
if st.button("📥 体重データを取得"):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # カロミルAPIの体重データ取得エンドポイント（仮の例。実際のURLに差し替えてください）
    url = "https://test-connect.calomeal.com/api/v2/anthropometric/weight"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        weight_data = response.json()
        st.success("✅ データ取得成功！")
        st.json(weight_data)
    else:
        st.error("❌ データ取得に失敗しました")
        st.text(f"status: {response.status_code}")
