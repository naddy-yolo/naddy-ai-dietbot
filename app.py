import streamlit as st
import requests
import json
import os

# トークン保存ファイル名
TOKEN_FILE = "token.json"

st.title("カロミル認証コールバック")

# クエリパラメータからcodeを取得
query_params = st.query_params
code = query_params.get("code")

if code:
    st.success(f"✅ 認証コードを取得：\n{code}")

    # アクセストークン取得処理
    if st.button("アクセストークンを取得"):
        payload = {
            "grant_type": "authorization_code",
            "client_id": st.secrets["client_id"],
            "client_secret": st.secrets["client_secret"],
            "redirect_uri": "https://naddy-yolo.streamlit.app/callback",
            "code": code
        }

        res = requests.post("https://test-connect.calomeal.com/auth/token", data=payload)

        st.subheader("payload:")
        st.json(payload)

        if res.status_code == 200:
            token_data = res.json()
            st.success("✅ アクセストークン取得成功！")
            st.json(token_data)

            # ファイル保存
            with open(TOKEN_FILE, "w") as f:
                json.dump(token_data, f)
            st.info("📁 トークンを token.json に保存しました。")
        else:
            st.error("❌ アクセストークン取得失敗")
            try:
                st.json(res.json())
            except Exception:
                st.text(res.text)
else:
    st.warning("URLに ?code=xxx が含まれていません。認証からやり直してください。")
    st.text(f"認証コード: {code}")
