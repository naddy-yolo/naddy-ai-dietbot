import urllib.parse

base_url = "https://test-connect.calomeal.com/auth/request"
params = {
    "response_type": "code",
    "client_id": "naddy_yolo",
    "state": "securetoken_20250626_naddy1234567890abcd5678efgh",  # 英数字32文字以上
    "redirect_uri": "https://naddy-yolo.streamlit.app/callback",
    "scope": "meal image anthropometric exercise"
}

url = f"{base_url}?{urllib.parse.urlencode(params)}"
print("🔗 認証URL：", url)
