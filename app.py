import streamlit as st
import requests
import urllib.parse
import json
import os
import datetime

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
            st.text(f"status: {res.status_code}")
            st.text(res.text)  # ← エラー詳細を確認するために追加
else:
    st.warning("URLに ?code=xxx が含まれていません。認証からやり直してください。")
    st.text(f"認証コード: {code}")

# ----------------------------
# 体重データの取得処理
# ----------------------------
st.header("📊 カロミル体重データの取得")

# token.json が存在する場合に読み込み
if os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, "r") as f:
        token_data = json.load(f)
        access_token = token_data.get("access_token")

        if access_token:
            today = datetime.date.today()
            start_date = (today - datetime.timedelta(days=7)).isoformat()
            end_date = today.isoformat()

            headers = {
                "Authorization": f"Bearer {access_token}"
            }
            params = {
                "from": start_date,
                "to": end_date
            }

            if st.button("📥 体重データを取得"):
                res = requests.get("https://test-connect.calomeal.com/api/v2/anthropometric",
                                   headers=headers, params=params)

                if res.status_code == 200:
                    data = res.json()
                    st.success("✅ 体重データの取得に成功しました！")
                    st.json(data)
                else:
                    st.error("❌ データ取得に失敗しました")
                    st.text(f"status: {res.status_code}")
                    st.write(res.text)  # ← こちらもエラーの内容確認用
        else:
            st.warning("⚠️ access_token が取得できません。")
else:
    st.info("ℹ️ token.json が存在しません。先に認証を完了してください。")
