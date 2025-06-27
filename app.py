import streamlit as st
import requests

st.set_page_config(page_title="カロミル認証コールバック", layout="centered")

st.title("カロミル認証コールバック")

query_params = st.query_params  # ✅ 新API推奨
code = query_params.get("code", None)

if code:
    st.success("✅ 認証コードを取得しました")
    st.code(code)

    # アクセストークンを取得する処理
    token_url = "https://test-connect.calomeal.com/auth/accesstoken"
    payload = {
        "grant_type": "authorization_code",
        "client_id": st.secrets["client_id"],
        "client_secret": st.secrets["client_secret"],
        # redirect_uri は省略
        "code": code
    }

    st.write("📦 payload:", payload)

    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        st.success("✅ アクセストークンを取得しました")
        st.json(response.json())
    else:
        st.error(f"❌ アクセストークン取得エラー: {response.status_code}")
        st.json(response.json())

else:
    st.warning("URLに ?code=xxx が含まれていません。認証からやり直してください。")
    st.code("code: None")
