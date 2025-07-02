import streamlit as st
import requests
import json
import os
import datetime

st.set_page_config(page_title="カロミル体重データの取得", page_icon="📊")
st.title("📊 カロミル体重データの取得")

token_file = "token.json"
if not os.path.exists(token_file):
    st.error("❌ アクセストークンが保存されていません。まず認証を完了してください。")
    st.stop()

with open(token_file, "r") as f:
    token_data = json.load(f)

access_token = token_data.get("access_token")

# 過去7日分のデータを取得
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).strftime("%Y/%m/%d")
end_date = today.strftime("%Y/%m/%d")

if st.button("📥 体重データを取得（POST）"):
    url = "https://test-connect.calomeal.com/api/anthropometric"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "start_date": start_date,
        "end_date": end_date,
        "unit": "day"  # 例: "detail", "day", "week", "month", "end_of_month"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        st.success("✅ 体重データ取得成功！")
        st.json(response.json())
    else:
        st.error("❌ データ取得に失敗しました")
        st.text(f"status: {response.status_code}")
        st.write(response.text)
