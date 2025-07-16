import streamlit as st
import requests
import datetime

st.set_page_config(page_title="体重データ取得", page_icon="⚖️")
st.title("⚖️ カロミルAPI：体重データ取得")

# 🔑 アクセストークン読み込み（st.secrets から）
if "access_token" not in st.secrets:
    st.error("❌ st.secrets に access_token が登録されていません。")
    st.stop()

access_token = st.secrets["access_token"]

# 🔍 トークン確認表示（先頭60文字）
st.subheader("🔑 読み込まれたトークン（先頭60文字）")
st.code(access_token[:60] + "...")

# 📅 取得範囲（直近7日間）
today = datetime.date.today()
start_date = (today - datetime.timedelta(days=7)).strftime("%Y/%m/%d")
end_date = today.strftime("%Y/%m/%d")

# 📥 ボタン押下で取得開始
if st.button("📥 体重・体脂肪率データを取得"):
    url = "https://test-connect.calomeal.com/api/anthropometric"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    json_data = {
        "start_date": start_date,
        "end_date": end_date,
        "unit": "kg"
    }

    response = requests.post(url, headers=headers, json=json_data)

    st.subheader("✅ レスポンス")
    st.text(f"ステータスコード: {response.status_code}")

    try:
        st.json(response.json())
    except Exception:
        st.write(response.text)
