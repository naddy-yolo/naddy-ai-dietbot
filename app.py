import streamlit as st
import requests

st.title("カロミル認証コールバック")

# URLパラメータから認証コード取得
params = st.experimental_get_query_params()

if "code" in params:
    code = params["code"][0]
    st.success(f"✅ 認証コードを取得： {code}")

    if st.button("アクセストークンを取得"):
        token_url = "https://test-connect.calomeal.com/auth/accesstoken"
        payload = {
            "grant_type": "authorization_code",
            "client_id": st.secrets["client_id"],
            "client_secret": st.secrets["client_secret"],
            "redirect_uri": "https://naddy-yolo.streamlit.app/callback",
            "code": code
        }
        res = requests.post(token_url, data=payload)
        if res.status_code == 200:
            token_data = res.json()
            st.json(token_data)
            st.success("✅ アクセストークン取得成功！")
        else:
            st.error("❌ アクセストークン取得失敗")
            st.json(res.json())
else:
    st.info("URLに `?code=xxx` が含まれていません。認証からやり直してください。")
