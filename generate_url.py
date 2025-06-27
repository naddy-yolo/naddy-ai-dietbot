import urllib.parse

base_url = "https://test-connect.calomeal.com/auth/request"
params = {
    "response_type": "code",
    "client_id": "naddy_yolo",
    "state": "securetoken_20250627_demo9876543210naddyok"
    # redirect_uri は不要なため削除
}

url = f"{base_url}?{urllib.parse.urlencode(params)}"
print("🔗 認証URL：", url)
