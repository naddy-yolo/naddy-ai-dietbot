import streamlit as st
import requests

st.title("カロミル認証コールバック")

# URLパラメータから認証コード取得
params = st.query_params

# 初期化
code = None
payload = None

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

        st.write("payload:", payload)  # デバッグ用に表示

        res = requests.post(token_url, data=payload)
        if res.status_code == 200:
            token_data = res.json()

            # ✅ セッションに保存
            st.session_state["access_token"] = token_data["access_token"]
            st.session_state["refresh_token"] = token_data["refresh_token"]

            st.success("✅ アクセストークン取得成功！")
            st.json(token_data)
        else:
            st.error("❌ アクセストークン取得失敗")
            st.json(res.json())

else:
    st.info("URLに `?code=xxx` が含まれていません。認証からやり直してください。")

# 確認用の表示（オプション）
st.write("認証コード:", code)
if "access_token" in st.session_state:
    st.write("✅ アクセストークンがセッションに保存されています。")
