import streamlit as st
import requests

st.set_page_config(page_title="ユーザー情報の取得テスト", page_icon="🧪")
st.title("🧪 カロミルAPI：ユーザー情報の取得テスト")

# アクセストークンの取得（secrets から）
if "access_token" not in st.secrets:
    st.error("❌ st.secrets に access_token が登録されていません。")
    st.stop()

access_token = st.secrets["access_token"]

# テスト用ボタン
if st.button("▶️ ユーザー情報を取得"):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"  # 念のため JSON 指定
    }

    url = "https://test-connect.calomeal.com/api/user_info"
    response = requests.post(url, headers=headers)

    st.subheader("✅ レスポンス")
    st.text(f"ステータスコード: {response.status_code}")
    try:
        st.json(response.json())
    except Exception:
        st.write(response.text)
