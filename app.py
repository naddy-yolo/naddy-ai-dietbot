import streamlit as st
import requests
import json
import os

st.title("カロミル認証コールバック")

# URLからcodeパラメータを取得
params = st.query_params  # ← 新しい推奨メソッド

# 初期化
code = None
payload = None

if "code" in params:
    code = params["code"]
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
            st.json(token_data)
            st.success("✅ アクセストークン取得成功！")

            # 🔽 トークンをファイルに保存
            with open("token.json", "w") as f:
                json.dump(token_data, f)
            st.info("💾 トークンを token.json に保存しました")

        else:
            st.error("❌ アクセストークン取得失敗")
            st.json(res.json())
else:
    st.info("URLに `?code=xxx` が含まれていません。認証からやり直してください。")

st.write("認証コード:", code)  # 確認用
