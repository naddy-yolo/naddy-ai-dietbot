import streamlit as st
import requests
import json
import os

st.set_page_config(page_title="ユーザー情報の取得テスト", page_icon="🧪")
st.title("🧪 カロミルAPI：ユーザー情報の取得テスト")

# アクセストークンの読み込み
token_file = "token.json"
if not os.path.exists(token_file):
    st.error("❌ アクセストークンが保存されていません。まず認証を完了してください。")
    st.stop()

with open(token_file, "r") as f:
    token_data = json.load(f)

access_token = token_data.get("access_token")

# テスト用ボタン
if st.button("▶️ ユーザー情報を取得"):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    url = "https://test-connect.calomeal.com/api/user_info"
    response = requests.post(url, headers=headers)

    st.subheader("✅ レスポンス")
    st.text(f"ステータスコード: {response.status_code}")
    try:
        st.json(response.json())
    except Exception:
        st.write(response.text)
