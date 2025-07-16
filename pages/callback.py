# pages/callback.py

import streamlit as st

st.set_page_config(page_title="認証完了", page_icon="🔐")
st.title("🔐 カロミル認証：完了ページ")

query_params = st.experimental_get_query_params()

if "code" in query_params:
    code = query_params["code"][0]
    st.success("✅ 認証コードを取得しました！")
    st.code(code, language="text")
    st.session_state["auth_code"] = code  # 任意で保持
else:
    st.error("❌ 認証コードがURLに含まれていません。")
