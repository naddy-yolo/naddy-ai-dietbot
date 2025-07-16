import streamlit as st
import requests
import datetime

st.set_page_config(page_title="カロミルAPIテスト", page_icon="🩺")

st.title("🖋️ カロミルAPI：ユーザー情報の取得テスト")

# 認証情報（Streamlit Secretsから取得）
client_id = st.secrets["client_id"]
client_secret = st.secrets["client_secret"]
access_token = st.secrets["access_token"]
refresh_token = st.secrets["refresh_token"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

# ------------------------
# ✅ ユーザー情報の取得
# ------------------------
with st.expander("📘 ユーザー情報を取得"):
    if st.button("▶ ユーザー情報を取得"):
        userinfo_url = "https://public-api.calomeal.com/api/v1/users/current"
        response = requests.get(userinfo_url, headers=headers)

        st.markdown("✅ **レスポンス**")
        st.code(response.status_code)
        st.json(response.json())


# ------------------------
# ✅ 体重・体脂肪率データの取得
# ------------------------
st.markdown("---")
st.title("📊 カロミルAPI：体重・体脂肪率の取得")

with st.expander("📘 過去7日間のデータ取得"):
    if st.button("▶ 体重データを取得"):
        # 過去7日間の日付を取得
        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=7)

        url = "https://public-api.calomeal.com/api/v1/anthropometric"
        params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.get(url, headers=headers, params=params)

        st.markdown("✅ **レスポンス（ステータス: {}）**".format(response.status_code))
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("データ取得に失敗しました")
